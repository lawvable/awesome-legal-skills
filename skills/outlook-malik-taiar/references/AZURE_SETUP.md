# Azure App Registration - Step by Step

This guide is for advanced users who want to use their own Azure App instead of the shared Lawvable app.

## 1. Create the App

1. Go to https://portal.azure.com
2. Search for "App registrations" in the top search bar
3. Click "New registration"

### Registration Form

| Field | Value |
|-------|-------|
| Name | `Lawvable-Outlook` (or any name you prefer) |
| Supported account types | "Accounts in any organizational directory (Any Azure AD directory - Multitenant) and personal Microsoft accounts" |
| Redirect URI | Platform: `Web`, URI: `http://localhost:3000/callback` |

4. Click "Register"

## 2. Note Your Credentials

After registration, you'll see the "Overview" page. Copy this value:

```
Application (client) ID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

You'll need this for the skill configuration.

## 3. Configure API Permissions

1. In the left sidebar, click "API permissions"
2. Click "Add a permission"
3. Select "Microsoft Graph"
4. Select "Delegated permissions"
5. Search and add each permission:

### Required Permissions

| Permission | Why |
|------------|-----|
| `Mail.Read` | Read email messages |
| `Mail.ReadWrite` | Create drafts, manage folders |
| `Mail.Send` | Send emails |
| `User.Read` | Get user profile info |

### Optional Permissions (for extended features)

| Permission | Why |
|------------|-----|
| `Calendars.Read` | Read calendar events |
| `Calendars.ReadWrite` | Create/modify events |
| `Files.Read.All` | Access OneDrive/SharePoint files |
| `Sites.Read.All` | Read SharePoint sites |

6. Click "Add permissions"

## 4. Grant Admin Consent (If Required)

If you see a warning "Not granted for [your org]":

- **Personal account**: You can grant consent yourself on first login
- **Work/School account**: Ask your IT admin to click "Grant admin consent for [org]"

## 5. Configure Authentication

1. In the left sidebar, click "Authentication"
2. Under "Advanced settings":
   - Allow public client flows: **Yes** (required for CLI-based auth)
3. Click "Save"

## 6. Environment Variable

Set this environment variable to use your own app:

```bash
export AZURE_CLIENT_ID="your-application-client-id"
```

## Verification Checklist

- [ ] App registered in Azure Portal
- [ ] Client ID copied
- [ ] API permissions added: `Mail.Read` and `User.Read`
- [ ] Admin consent granted (if using work account)
- [ ] "Allow public client flows" set to Yes
- [ ] Environment variable set

## Common Issues

### "AADSTS65001: The user or administrator has not consented"

→ Permissions need admin consent. Ask your IT admin or use a personal Microsoft account.

### "AADSTS7000218: The request body must contain: client_secret"

→ The app is configured as confidential. Go to Authentication > Advanced settings > Allow public client flows: Yes

### "AADSTS50011: The reply URL does not match"

→ Add `http://localhost:3000/callback` to your app's redirect URIs in Authentication settings.
