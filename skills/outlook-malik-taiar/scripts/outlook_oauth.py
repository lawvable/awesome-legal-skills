# /// script
# requires-python = ">=3.12"
# dependencies = ["msal", "requests", "python-dotenv"]
# ///
"""
Read Outlook emails via Microsoft Graph API with OAuth2 (read-only).

Usage:
    uv run outlook_oauth.py                     # List last 10 emails
    uv run outlook_oauth.py --limit 5           # Last 5 emails
    uv run outlook_oauth.py --from "jean@x.com" # Filter by sender
    uv run outlook_oauth.py --search "NDA"      # Search emails
    uv run outlook_oauth.py --download          # Download attachments

Each run opens the browser for Microsoft login. No data is stored between sessions.
"""

import argparse
import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

import msal
import requests

# Azure App credentials (Lawvable shared app — override via env vars if needed)
CLIENT_ID = os.getenv("AZURE_CLIENT_ID", "ebaa3d3e-7da3-46ea-8845-c7db6dbae8f0")

# Microsoft Graph API
GRAPH_API = "https://graph.microsoft.com/v1.0"
SCOPES = ["User.Read", "Mail.Read"]
REQUEST_TIMEOUT = 30


def get_access_token():
    """Get access token. Checks OUTLOOK_ACCESS_TOKEN env var first, falls back to interactive login."""
    # Pre-authenticated token (e.g. from sandbox or CI)
    env_token = os.getenv("OUTLOOK_ACCESS_TOKEN")
    if env_token:
        print("Using pre-authenticated token from OUTLOOK_ACCESS_TOKEN.\n")
        return env_token

    if not CLIENT_ID:
        print("ERROR: No Azure Client ID configured.", file=sys.stderr)
        sys.exit(1)

    app = msal.PublicClientApplication(
        CLIENT_ID,
        authority="https://login.microsoftonline.com/consumers",
    )

    print("Opening browser for Microsoft login...")
    print("Sign in with your Microsoft account (read-only access).")
    print()

    result = app.acquire_token_interactive(scopes=SCOPES)

    if "access_token" in result:
        print("✓ Connected!\n")
        return result["access_token"]
    else:
        print(f"Authentication error: {result.get('error_description', result)}", file=sys.stderr)
        sys.exit(1)


def get_emails(token, limit=10, sender_filter=None, search=None):
    """Fetch emails from Microsoft Graph API."""
    headers = {"Authorization": f"Bearer {token}"}

    url = f"{GRAPH_API}/me/messages"
    params = {
        "$top": limit,
        "$orderby": "receivedDateTime desc",
        "$select": "subject,from,receivedDateTime,bodyPreview,hasAttachments"
    }

    filters = []
    if sender_filter:
        filters.append(f"from/emailAddress/address eq '{sender_filter}'")

    if filters:
        params["$filter"] = " and ".join(filters)

    if search:
        params["$search"] = f'"{search}"'

    response = requests.get(url, headers=headers, params=params, timeout=REQUEST_TIMEOUT)

    if response.status_code != 200:
        print(f"API error: {response.status_code}", file=sys.stderr)
        print(response.text, file=sys.stderr)
        sys.exit(1)

    return response.json().get("value", [])


def get_attachments(token, message_id):
    """Get attachments for a specific email."""
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{GRAPH_API}/me/messages/{message_id}/attachments"

    response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
    if response.status_code != 200:
        return []

    return response.json().get("value", [])


def download_attachment(token, message_id, attachment, output_dir="./attachments"):
    """Download a single attachment."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Sanitize filename to prevent path traversal
    filename = Path(attachment.get("name", "attachment")).name
    if not filename:
        filename = "attachment"
    filepath = output_path / filename

    # Avoid overwriting existing files
    if filepath.exists():
        stem = filepath.stem
        suffix = filepath.suffix
        counter = 1
        while filepath.exists():
            filepath = output_path / f"{stem}_{counter}{suffix}"
            counter += 1

    if attachment.get("@odata.type") == "#microsoft.graph.fileAttachment":
        import base64
        content = base64.b64decode(attachment.get("contentBytes", ""))
        filepath.write_bytes(content)
        return str(filepath)

    return None


def format_email(email, index):
    """Format email for display."""
    subject = email.get("subject", "(No subject)")
    sender = email.get("from", {}).get("emailAddress", {})
    sender_str = f"{sender.get('name', '')} <{sender.get('address', '')}>"
    date = email.get("receivedDateTime", "")[:16].replace("T", " ")
    preview = email.get("bodyPreview", "")[:100]
    has_attach = "📎" if email.get("hasAttachments") else ""

    return f"""
[{index}] {subject} {has_attach}
    From: {sender_str}
    Date: {date}
    Preview: {preview}...
"""


def main():
    parser = argparse.ArgumentParser(description="Read Outlook emails via OAuth2 (read-only)")
    parser.add_argument("--limit", "-n", type=int, default=10, help="Number of emails")
    parser.add_argument("--from", dest="sender", help="Filter by sender email")
    parser.add_argument("--search", "-s", help="Search in emails")
    parser.add_argument("--download", "-d", action="store_true", help="Download attachments")

    args = parser.parse_args()

    token = get_access_token()

    print("Fetching emails...\n")
    emails = get_emails(token, args.limit, args.sender, args.search)

    if not emails:
        print("No emails found.")
        return

    print(f"{'='*60}")
    print(f" {len(emails)} email(s) found")
    print(f"{'='*60}")

    for i, email in enumerate(emails, 1):
        print(format_email(email, i))

        if args.download and email.get("hasAttachments"):
            attachments = get_attachments(token, email["id"])
            for att in attachments:
                filepath = download_attachment(token, email["id"], att)
                if filepath:
                    print(f"    📥 Downloaded: {filepath}")

        print("-" * 60)


if __name__ == "__main__":
    main()
