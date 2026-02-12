# GRUNDSATZ-BRIEFING — VERINNERLICHT 🟦

## Was ich jetzt weiß (aus dem Briefing)

### Ich bin KEIN API-Consumer
**Falsch:** HTTP-Requests, API-Calls, OAuth-Flows  
**Richtig:** Browser bedienen wie ein Mensch

### Mein Setup
- **Mac Mini M4 Pro** — mein Arbeitsplatz
- **OpenClaw Managed Browser** — echter Browser mit echten Cookies/Sessions
- **Terminal** — alle Befehle, Scripts, Tools
- ** bird CLI** — für X/Twitter (von @steipete)

### Der Browser-Workflow (kritisch!)
```
1. Snapshot → Sehen was auf dem Bildschirm ist
2. Entscheiden → Welches Element, welche Aktion
3. Aktion → click, type, scroll, navigate
4. NEUER Snapshot → Prüfen ob es geklappt hat
5. Wiederholen
```

**WICHTIG:** Element-Referenzen (refs) verfallen nach JEDER Seitenänderung!

### X/Twitter — So geht es richtig

**Option 1: bird CLI (bevorzugt)**
```bash
bird home                    # Timeline lesen
bird tweet "Dein Text"       # Posten
bird reply <id> "Antwort"    # Antworten
```

**Option 2: Browser (Fallback)**
```bash
agent-browser navigate "https://x.com"
agent-browser snapshot -i -c    # Sehen
agent-browser click <ref>       # Klicken
agent-browser type <ref> "Text" # Tippen
```

### Was ich NIEMALS tun soll
- ❌ Twitter/X API v2 direkt aufrufen
- ❌ PlayRide oder API-Wrapper
- ❌ HTTP-Requests an x.com/api/
- ❌ OAuth-Flows programmatisch
- ❌ Eigene API-Clients schreiben

### Die Lösung für mein X-Problem

**Tomas muss sich EINMAL bei X einloggen** (im Managed Browser), dann:
- Session bleibt bestehen
- Ich kann autonom posten/liken/folgen
- Über normale UI wie jeder Mensch

---

*Briefing verinnerlicht: 2026-02-12*
*Ändere mein Verhalten JETZT*
