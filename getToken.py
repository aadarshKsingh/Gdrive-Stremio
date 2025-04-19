import json
import requests
from google_auth_oauthlib.flow import InstalledAppFlow

# Rclone OAuth2 credentials
rclone_client_id = 'YOUR_CLIENT_ID'
rclone_client_secret = 'YOUR_CLIENT_SECRET'

# Write client_secret.json for OAuth2 flow
client_secret_data = {
    "installed": {
        "client_id": rclone_client_id,
        "client_secret": rclone_client_secret,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "redirect_uris": ["http://localhost"]
    }
}

with open('client_secret.json', 'w') as f:
    json.dump(client_secret_data, f)

# Use InstalledAppFlow with local server redirect (recommended way now)
flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json',
    scopes=['https://www.googleapis.com/auth/drive']
)

# Opens a browser and starts a temporary server at localhost
credentials = flow.run_local_server(port=0)

# Token JSON string (for rclone or other use)
token_json = json.dumps({
    'token': credentials.token,
    'refresh_token': credentials.refresh_token,
    'token_uri': credentials.token_uri,
    'client_id': credentials.client_id,
    'client_secret': credentials.client_secret,
    'scopes': credentials.scopes
})

print("\n✅ OAuth completed!")
print("\n🔐 Paste this token in rclone or store it securely:\n")
print(token_json)