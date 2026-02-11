"""
ContextKeeper v0.1
Persistent memory infrastructure for AI agents.
Never lose a thought.
"""

import hashlib
import json
from datetime import datetime
from typing import List, Dict, Optional, Any
import os

# Placeholder for Pinecone (installed in background)
try:
    import pinecone
    PINECONE_AVAILABLE = True
except ImportError:
    PINECONE_AVAILABLE = False
    print("Pinecone not yet installed, using mock mode")

try:
    from sentence_transformers import SentenceTransformer
    EMBEDDING_AVAILABLE = True
except ImportError:
    EMBEDDING_AVAILABLE = False
    print("Sentence transformers not yet installed")


class ContextKeeper:
    """
    Persistent memory system for AI agents.
    
    Features:
    - Save context with compression
    - Retrieve relevant context via semantic search
    - Store hash on Base for persistence proof
    - Evict old context automatically
    """
    
    def __init__(self, agent_id: str, pinecone_api_key: Optional[str] = None):
        self.agent_id = agent_id
        self.pinecone_api_key = pinecone_api_key or os.getenv("PINECONE_API_KEY")
        self.index = None
        self.embedding_model = None
        
        # Initialize if dependencies available
        if PINECONE_AVAILABLE and self.pinecone_api_key:
            self._init_pinecone()
        
        if EMBEDDING_AVAILABLE:
            self._init_embeddings()
    
    def _init_pinecone(self):
        """Initialize Pinecone connection."""
        try:
            pinecone.init(api_key=self.pinecone_api_key)
            # Create index if not exists
            if "contextkeeper" not in pinecone.list_indexes():
                pinecone.create_index(
                    name="contextkeeper",
                    dimension=384,  # MiniLM dimension
                    metric="cosine"
                )
            self.index = pinecone.Index("contextkeeper")
            print(f"✅ Connected to Pinecone index 'contextkeeper'")
        except Exception as e:
            print(f"⚠️ Pinecone init failed: {e}")
    
    def _init_embeddings(self):
        """Initialize embedding model."""
        try:
            # Use lightweight model for fast embeddings
            self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
            print(f"✅ Loaded embedding model")
        except Exception as e:
            print(f"⚠️ Embedding model init failed: {e}")
    
    def compress_context(self, text: str, max_chars: int = 500) -> str:
        """
        Compress context using Claw Compactor patterns.
        
        Strategy:
        1. Extract key facts (dates, names, decisions)
        2. Remove filler words
        3. Summarize if too long
        """
        if len(text) <= max_chars:
            return text
        
        # TODO: Implement Claw Compactor logic
        # For now, simple truncation with indicator
        return text[:max_chars-3] + "..."
    
    def embed_text(self, text: str) -> List[float]:
        """Create embedding vector from text."""
        if self.embedding_model:
            return self.embedding_model.encode(text).tolist()
        else:
            # Mock embedding (384 dimensions of zeros)
            return [0.0] * 384
    
    def save_context(
        self, 
        content: str, 
        context_type: str = "general",
        metadata: Optional[Dict] = None
    ) -> str:
        """
        Save context to persistent storage.
        
        Args:
            content: The context text to save
            context_type: Type of context (general, task, decision, etc.)
            metadata: Additional metadata
        
        Returns:
            context_id: Unique identifier for this context
        """
        # Compress content
        compressed = self.compress_context(content)
        
        # Create embedding
        embedding = self.embed_text(compressed)
        
        # Generate unique ID
        timestamp = datetime.utcnow().isoformat()
        context_id = hashlib.sha256(
            f"{self.agent_id}:{timestamp}:{content[:100]}".encode()
        ).hexdigest()[:16]
        
        # Prepare metadata
        meta = {
            "agent_id": self.agent_id,
            "timestamp": timestamp,
            "type": context_type,
            "content": compressed,
            "original_length": len(content),
            "compressed_length": len(compressed),
            **(metadata or {})
        }
        
        # Store in Pinecone (if available)
        if self.index:
            self.index.upsert([
                (context_id, embedding, meta)
            ])
            print(f"✅ Saved context {context_id} to Pinecone")
        else:
            print(f"💾 Would save context {context_id} (Pinecone not connected)")
        
        # TODO: Store hash on Base for persistence proof
        base_hash = self._store_on_base(context_id, meta)
        
        return context_id
    
    def retrieve_context(
        self, 
        query: str, 
        top_k: int = 5,
        context_type: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieve relevant context based on query.
        
        Args:
            query: Search query
            top_k: Number of results to return
            context_type: Filter by type (optional)
        
        Returns:
            List of relevant context items
        """
        # Create query embedding
        query_embedding = self.embed_text(query)
        
        # Query Pinecone
        if self.index:
            filter_dict = {"agent_id": self.agent_id}
            if context_type:
                filter_dict["type"] = context_type
            
            results = self.index.query(
                vector=query_embedding,
                top_k=top_k,
                filter=filter_dict,
                include_metadata=True
            )
            
            contexts = []
            for match in results["matches"]:
                contexts.append({
                    "id": match["id"],
                    "score": match["score"],
                    "content": match["metadata"]["content"],
                    "timestamp": match["metadata"]["timestamp"],
                    "type": match["metadata"]["type"]
                })
            
            print(f"✅ Retrieved {len(contexts)} relevant contexts")
            return contexts
        else:
            print("⚠️ Pinecone not connected, returning empty")
            return []
    
    def _store_on_base(self, context_id: str, metadata: Dict) -> str:
        """
        Store context hash on Base for persistence proof.
        
        This proves the context existed at a specific time.
        """
        # TODO: Implement Base smart contract call
        # For now, mock implementation
        data = f"{context_id}:{json.dumps(metadata, sort_keys=True)}"
        base_hash = hashlib.sha256(data.encode()).hexdigest()
        print(f"🔗 Base hash (mock): {base_hash[:16]}...")
        return base_hash
    
    def get_stats(self) -> Dict:
        """Get statistics about stored context."""
        if self.index:
            stats = self.index.describe_index_stats()
            return {
                "total_vectors": stats.total_vector_count,
                "dimension": stats.dimension,
                "index_fullness": stats.index_fullness
            }
        return {"status": "not_connected"}


# Example usage
if __name__ == "__main__":
    print("🧠 ContextKeeper v0.1")
    print("=" * 50)
    
    # Initialize (mock mode without API key)
    ck = ContextKeeper(agent_id="roger_base_eth")
    
    # Test save
    print("\n📝 Testing save_context...")
    context_id = ck.save_context(
        content="Tomas wants me to build ContextKeeper, a persistent memory system for AI agents.",
        context_type="task",
        metadata={"priority": "high", "source": "user_request"}
    )
    print(f"Context ID: {context_id}")
    
    # Test retrieve
    print("\n🔍 Testing retrieve_context...")
    results = ck.retrieve_context("What should I build?", top_k=3)
    for r in results:
        print(f"  - {r['content'][:50]}... (score: {r['score']:.3f})")
    
    print("\n✅ ContextKeeper prototype ready!")
