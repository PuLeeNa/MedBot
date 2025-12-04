# Split Architecture Deployment

## Overview

- **Frontend**: Netlify (static files, instant loading)
- **Backend**: Render (API processing, AI inference)

## Setup Steps

### 1. Backend (Render)

Already configured with `render.yaml`:

```yaml
rootDir: backend
```

Push changes to GitHub → Render auto-deploys.

### 2. Frontend (Netlify)

**Manual Setup:**

1. Go to [Netlify](https://app.netlify.com/)
2. Click "Add new site" → "Import an existing project"
3. Connect GitHub repo
4. Configure:
   - Base directory: `frontend`
   - Build command: (leave empty)
   - Publish directory: `frontend`
5. Deploy site

**Get Site ID:**

```bash
# After first deployment
netlify status
# Copy NETLIFY_SITE_ID
```

**Get Auth Token:**

1. Go to Netlify → User settings → Applications
2. Create new personal access token
3. Copy token

### 3. GitHub Secrets

Add to repository secrets:

- `RENDER_SERVICE_ID` (from Render dashboard)
- `RENDER_API_KEY` (from Render account settings)
- `NETLIFY_AUTH_TOKEN` (from step 2)
- `NETLIFY_SITE_ID` (from step 2)

### 4. Update Frontend API URL

In `frontend/app.js`:

```javascript
const API_URL = "https://your-backend-url.onrender.com";
```

## CI/CD Workflow

- Changes to `backend/**` → Triggers backend deployment to Render
- Changes to `frontend/**` → Triggers frontend deployment to Netlify

## Benefits

✅ No cold start UI visible to users (frontend on CDN)  
✅ Fast static asset delivery (Netlify CDN)  
✅ Backend processes AI workload (Render)  
✅ Automated deployments with CI/CD
