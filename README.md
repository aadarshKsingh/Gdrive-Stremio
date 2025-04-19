# stremio-gdrive

Stream your **Google Drive (My Drive + Shared Drives)** content directly in **Stremio**.

Based on: [ssnjr2002/stremio-gdrive](https://github.com/ssnjr2002/stremio-gdrive)

---

## 🔧 Google Cloud Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/projectcreate), create a project.
2. Go to **APIs & Services > OAuth Consent Screen**:
   - User Type: **External**
   - Add your email as test user
3. Enable **Google Drive API**:
   - Go to **API Library**, search for "Drive API", and enable it.
4. Go to **Credentials > Create Credentials > OAuth Client ID**:
   - App Type: **Desktop**
   - Download the `client_secret.json`
5. **Publish the App** from the OAuth Consent Screen.

---

## 🔑 Generate Token

1. Clone this repo and make sure `client_secret.json` is in the root folder.
2. Open `getToken.py`, add your **Client ID** and **Client Secret** at the top.
3. Run:

```bash
python getToken.py
```

4. Authorize via the URL shown, paste the auth code when prompted.
5. You will get a token like:

```json
{
  "token": "ya29...",
  "refresh_token": "1//...",
  "token_uri": "https://oauth2.googleapis.com/token",
  "client_id": "...apps.googleusercontent.com",
  "client_secret": "...",
  "scopes": ["https://www.googleapis.com/auth/drive"]
}
```

**Save this token**, you'll need it for Vercel deployment.

---

## 🚀 Deploy on Vercel

1. Go to [vercel.com](https://vercel.com), sign in.
2. Import this repo:  
   `https://github.com/aadarshKsingh/Gdrive-Stremio-Update`
3. In project settings:
   - Set Node version to `18.xx` in `vercel.json`:
   - Add environment variable:
     - **Key**: `TOKEN`
     - **Value**: *(Paste your token JSON)*

4. Redeploy (disable build cache), then click **Visit**.

---

## 📺 Add to Stremio

1. Get your deployed URL and add `/manifest.json` to the end.  
   Example:  
   ```
   https://your-project.vercel.app/manifest.json
   ```
2. Open Stremio (desktop/mobile) → **Add-ons** → Paste the manifest URL in search.
3. Click **Install**.

---

## 🔍 How It Works

- The addon searches your Google Drive for matching videos when you open a title in Stremio.
- It supports:
  - 🎬 **Movies**: `Movie Name (Year).mkv`
  - 📺 **TV Episodes**: S01E01, 1x01, Season 1 Episode 1, etc.

**Example**:

Searching for **Pirates of the Goolag** will find:
- `Pirates of the Goolag 2016.mkv`
- `Pirates.of.the.Goolag.2016.1080p.x265.mkv`

If matched, Stremio displays it as a stream instantly.

---