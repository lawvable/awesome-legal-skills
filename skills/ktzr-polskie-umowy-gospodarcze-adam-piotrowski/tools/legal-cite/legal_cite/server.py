"""legal-cite — samodzielny serwer MCP (weryfikacja przepisu PL/UE).

Transport:
  - Cloud Run (env K_SERVICE lub PORT): streamable-http na 0.0.0.0:$PORT,
    endpoint MCP = `/mcp` → podłączasz w Claude jako custom connector (URL).
  - lokalnie (brak PORT): stdio (Claude Desktop / Claude Code).

Publiczny, bez auth — serwuje wyłącznie publiczne teksty aktów prawnych.
"""
from __future__ import annotations

import logging
import os
import sys

from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

from legal_cite import core

logging.basicConfig(level=logging.INFO, stream=sys.stderr,
                    format="[legal-cite] %(message)s")
logger = logging.getLogger(__name__)

mcp = FastMCP("legal-cite")


@mcp.tool()
async def verify_article(citation: str) -> str:
    """Dokładne brzmienie cytowanego przepisu z OFICJALNEGO źródła
    (api.sejm.gov.pl dla PL, EUR-Lex dla UE) — zwraca tylko ten artykuł,
    nie cały akt. Zwraca AKTUALNE brzmienie (tekst jednolity).
    Anti-halucynacja: weryfikacja cytatu wprost ze źródła.
    Format: 'art. N [ust. M] KOD'. Przykłady: 'art. 45 u.k.k.',
    'art. 385 KC', 'art. 28 ust. 3 RODO', 'art. 10 CCD'. Kody: list_acts()."""
    try:
        return await core.verify_article(citation)
    except Exception as e:
        logger.warning("verify_article blad=%s", type(e).__name__)
        return f"❌ Błąd weryfikacji: {type(e).__name__}: {e}"


@mcp.tool()
def list_acts() -> str:
    """Lista obsługiwanych kodów aktów (PL + UE) dla verify_article."""
    return core.list_acts()


def main() -> None:
    port = os.getenv("PORT")
    if os.getenv("K_SERVICE") or port:
        mcp.settings.host = "0.0.0.0"
        mcp.settings.port = int(port or "8080")
        # Za proxy Cloud Run Host = domena *.run.app (nie localhost). Ochrona
        # DNS-rebinding jest dla serwerów LOKALNYCH (atak z przeglądarki na
        # localhost) — publiczny serwis z publicznymi przepisami jej nie potrzebuje.
        mcp.settings.transport_security = TransportSecuritySettings(
            enable_dns_rebinding_protection=False)
        logger.info("legal-cite start: streamable-http na %s:%s (/mcp)",
                    mcp.settings.host, mcp.settings.port)
        mcp.run(transport="streamable-http")
    else:
        logger.info("legal-cite start: stdio (lokalnie)")
        mcp.run()


if __name__ == "__main__":
    main()
