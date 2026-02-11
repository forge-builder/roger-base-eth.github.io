// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title ContextKeeperRegistry
 * @notice Stores context hashes on Base for persistence proof
 * @dev Optimized for minimal gas - only stores hashes, not full context
 */
contract ContextKeeperRegistry {
    
    // Agent address => Context ID => Context metadata
    mapping(address => mapping(string => Context)) public contexts;
    
    // Agent address => List of context IDs
    mapping(address => string[]) public agentContexts;
    
    struct Context {
        bytes32 contentHash;      // Hash of compressed context
        uint256 timestamp;        // When stored
        string vectorId;          // Pinecone vector ID
        uint256 retrievalCount;   // How many times retrieved
    }
    
    event ContextStored(
        address indexed agent,
        string indexed contextId,
        bytes32 contentHash,
        uint256 timestamp
    );
    
    event ContextRetrieved(
        address indexed agent,
        string indexed contextId,
        uint256 timestamp
    );
    
    /**
     * @notice Store a context hash on-chain
     * @param contextId Unique identifier (provided by ContextKeeper)
     * @param contentHash Hash of the compressed context content
     * @param vectorId Pinecone vector ID for retrieval
     */
    function storeContext(
        string calldata contextId,
        bytes32 contentHash,
        string calldata vectorId
    ) external {
        require(bytes(contexts[msg.sender][contextId].vectorId).length == 0, "Context exists");
        
        contexts[msg.sender][contextId] = Context({
            contentHash: contentHash,
            timestamp: block.timestamp,
            vectorId: vectorId,
            retrievalCount: 0
        });
        
        agentContexts[msg.sender].push(contextId);
        
        emit ContextStored(msg.sender, contextId, contentHash, block.timestamp);
    }
    
    /**
     * @notice Record that a context was retrieved (for stats)
     * @param contextId The context that was accessed
     */
    function recordRetrieval(string calldata contextId) external {
        Context storage ctx = contexts[msg.sender][contextId];
        require(bytes(ctx.vectorId).length > 0, "Context not found");
        
        ctx.retrievalCount++;
        
        emit ContextRetrieved(msg.sender, contextId, block.timestamp);
    }
    
    /**
     * @notice Get all context IDs for an agent
     * @param agent The agent address
     * @return Array of context IDs
     */
    function getAgentContexts(address agent) external view returns (string[] memory) {
        return agentContexts[agent];
    }
    
    /**
     * @notice Verify content matches stored hash
     * @param contextId The context to verify
     * @param content The content to check
     * @return bool True if hash matches
     */
    function verifyContent(
        string calldata contextId,
        string calldata content
    ) external view returns (bool) {
        bytes32 computedHash = keccak256(abi.encodePacked(content));
        return contexts[msg.sender][contextId].contentHash == computedHash;
    }
}
