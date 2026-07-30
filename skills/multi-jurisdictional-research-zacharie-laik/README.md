# Multi-jurisdictional Research

Multi-jurisdictional legal research and risk assessment using the Legal Data Hunter MCP (40+ countries, 13M+ documents). Use when the user asks about law across multiple countries, comparative law, cross-border regulatory analysis, or case law/legislation in any European or other covered jurisdiction. Triggers on jurisdictional comparison, cross-border risk, multi-country compliance, GDPR enforcement across member states, or Legal Data Hunter references. Also handles single non-French jurisdiction research.

## Install Legal Data Hunter

Install the Legal Data Hunter MCP server and verify the connection. Legal Data Hunter provides access to 18M+ legal documents across 110+ countries — case law, legislation, and doctrine — via hybrid semantic + keyword search.

### Step 1: Detect environment and install

Check if running inside Claude Code:

```bash  
which claude 2\>/dev/null  
```

**If Claude Code is available**, run:

```bash  
claude mcp add legal-data-hunter --transport http https://legaldatahunter.com/mcp  
```

**If not Claude Code** (Cursor, VS Code, Windsurf, JetBrains, Copilot, Lawvable), run:

```bash  
npx legal-data-hunter --yes  
```

This auto-detects the client and writes the MCP config to the correct location. It supports: Cursor, VS Code, Lawvable, Windsurf, Copilot CLI, and JetBrains (Junie).

### Step 2: Verify installation

After installing, confirm the MCP server is connected. In Claude Code, reconnect MCP servers and check that `Legal Data Hunter` appears with its tools. The server exposes 7 tools:

| Tool | Purpose |  
|------|---------|  
| `discover\_countries()` | List all 110+ indexed countries with document counts |  
| `discover\_sources(country)` | List available sources for a country (e.g. `"FR"`, `"DE"`, `"EU"`) |  
| `search(query, ...)` | Hybrid semantic + keyword search across jurisdictions |  
| `resolve\_reference(citation)` | Look up a specific citation — ECLI, CELEX, article number, case number |  
| `get\_document(id)` | Retrieve the full text of a document by ID |  
| `get\_filters()` | List available filter options (courts, document types, date ranges) |  
| `report\_source\_issue(...)` | Report a problem with a data source or request a new one |

### Step 3: Getting started

Once connected, here are useful first queries to try:

**Explore coverage:**  
- Call `discover_countries()` to see all indexed jurisdictions and their document counts  
- Call `discover_sources("FR")` to see French court databases, legislation sources, and doctrine

**Search across jurisdictions:**  
- `search("unfair dismissal", country="DE", doc_type="case_law")` — German case law on unfair dismissal  
- `search("artificial intelligence regulation", country="EU")` — EU legislation on AI  
- `search("data protection breach notification", country="UK")` — UK GDPR enforcement

**Resolve specific citations:**  
- `resolve_reference("ECLI:EU:C:2014:317")` — look up a CJEU decision by ECLI  
- `resolve_reference("32016R0679")` — look up the GDPR by CELEX number  
- `resolve_reference("Article 49 TFEU")` — find Treaty provisions

**Retrieve full documents:**  
- Use `get_document(id)` with an ID returned from search or resolve_reference to get the complete text

## Tips

- **Natural language works**: The search engine understands legal concepts, not just keywords. "Can an employer fire someone for social media posts?" works as well as "dismissal social media misconduct".  
- **Cross-reference**: Search one jurisdiction, then use the same query in another to compare legal approaches across borders.  
- **Citation chains**: Use `resolve_reference()` to find a law, then `search()` with that law's name to find all court decisions that cite it.  
- **Filters narrow results**: Call `get_filters()` first to see what filter options are available, then pass them to `search()`.  
- **Missing a source?** Use `report_source_issue()` to request a new legal source or report a problem. New sources can be indexed in under 48 hours.

## Links

- Dashboard: https://legaldatahunter.com  
- API Docs: https://legaldatahunter.com/docs  
- GitHub: https://github.com/worldwidelaw/legal-sources  
- MCP endpoint: https://legaldatahunter.com/mcp  