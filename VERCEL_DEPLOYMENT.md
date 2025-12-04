# Vercel Deployment Guide for MedBot

## 🚀 Quick Deploy to Vercel

### Prerequisites
- GitHub account with MedBot repository
- Vercel account (free tier available)
- Pinecone API key
- Groq API key

---

## Step-by-Step Deployment

### 1. **Prepare Your Repository**

Ensure these files are in your repository:
```
✅ api/index.py (Vercel serverless function)
✅ vercel.json (Vercel configuration)
✅ requirements-vercel.txt (Python dependencies for Vercel)
✅ templates/ (HTML templates)
✅ static/ (CSS, images)
✅ src/ (helper functions, prompts)
```

### 2. **Commit and Push Changes**

```bash
git add .
git commit -m "Add Vercel deployment configuration"
git push origin main
```

### 3. **Deploy to Vercel**

#### Option A: Using Vercel Dashboard (Recommended)

1. Go to [https://vercel.com](https://vercel.com)
2. Click **"Add New"** → **"Project"**
3. **Import** your GitHub repository: `PuLeeNa/MedBot`
4. Vercel will auto-detect the configuration from `vercel.json`
5. Click **"Deploy"**

#### Option B: Using Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy from project directory
cd "c:\25\AI\GenAI\Medical Bot\MedBot\MedBot"
vercel --prod
```

### 4. **Configure Environment Variables**

In Vercel Dashboard → Your Project → Settings → Environment Variables:

Add the following:

| Name | Value | Environment |
|------|-------|-------------|
| `PINECONE_API_KEY` | `your_pinecone_api_key` | Production, Preview, Development |
| `GROQ_API_KEY` | `your_groq_api_key` | Production, Preview, Development |

**Important:** Click "Save" after adding each variable.

### 5. **Redeploy** (if needed)

After adding environment variables, trigger a new deployment:
- Go to **Deployments** tab
- Click **"Redeploy"** on the latest deployment

---

## ⚙️ Configuration Details

### vercel.json Structure

```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "/(.*)",
      "dest": "/api/index.py"
    }
  ]
}
```

### Key Differences from Render

| Feature | Render | Vercel |
|---------|--------|--------|
| **Runtime** | Docker container | Serverless functions |
| **Cold Start** | ~30-60s | ~3-5s |
| **Max Execution** | Continuous | 10s (Hobby), 60s (Pro) |
| **Memory** | 512MB (free) | 1024MB (Hobby) |
| **Pricing** | Free tier available | Free tier available |
| **Best For** | Long-running processes | Fast API responses |

---

## 🔍 Verifying Deployment

### Check Deployment Status

1. Go to Vercel Dashboard → Your Project → **Deployments**
2. Wait for status: **"Ready"** ✅
3. Click on the deployment URL to test

### Test Your Application

1. Visit your Vercel URL: `https://medbot-your-project.vercel.app`
2. Test the chat interface
3. Ask a medical question
4. Verify responses are working

### View Logs

- Go to Vercel Dashboard → Your Project → **Logs**
- Monitor real-time function execution
- Debug any errors

---

## 🐛 Troubleshooting

### Issue: "Module not found" Error

**Solution:** Ensure `requirements-vercel.txt` exists in root directory

```bash
# Rename if needed
mv requirements-vercel.txt requirements.txt
```

### Issue: Environment Variables Not Working

**Solution:** 
1. Verify variables are added in Vercel Dashboard
2. Redeploy after adding variables
3. Check variable names match exactly (case-sensitive)

### Issue: Cold Start Timeout

**Symptom:** First request takes too long (>10s)

**Solutions:**
- Upgrade to Vercel Pro (60s timeout)
- Optimize model loading (cache embeddings)
- Use smaller embedding models

### Issue: Static Files Not Loading

**Solution:** Verify `vercel.json` routes configuration:

```json
{
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    }
  ]
}
```

---

## 📊 Monitoring Performance

### Vercel Analytics (Optional)

Enable in Vercel Dashboard → Your Project → **Analytics**

Monitors:
- ✅ Response times
- ✅ Request volume
- ✅ Error rates
- ✅ Geographic distribution

### Function Logs

View in real-time:
```bash
vercel logs
```

---

## 🔄 CI/CD Integration

### Automatic Deployments

Vercel automatically deploys when you push to GitHub:

- **Push to `main`** → Production deployment
- **Push to other branches** → Preview deployment
- **Pull Requests** → Automatic preview URLs

### Manual Deployment Trigger

```bash
# Deploy specific branch
vercel --prod

# Deploy preview
vercel
```

---

## 💰 Cost Comparison

### Vercel Free Tier (Hobby)

- ✅ 100 GB bandwidth/month
- ✅ 100 GB-hours function execution
- ✅ 10s max function duration
- ✅ Unlimited deployments
- ✅ Automatic HTTPS

### When to Upgrade

Upgrade to Pro ($20/month) if:
- Need >10s execution time
- High traffic (>100GB bandwidth)
- Team collaboration features
- Priority support

---

## 🆚 Render vs Vercel - Which to Use?

| Scenario | Recommended Platform |
|----------|---------------------|
| **Portfolio/Demo** | ✅ Vercel (faster cold starts) |
| **Production App** | ✅ Render (Docker, more control) |
| **High Traffic** | ✅ Render (continuous running) |
| **Low Traffic** | ✅ Vercel (better free tier) |
| **Complex Deployment** | ✅ Render (Docker flexibility) |
| **Simple API** | ✅ Vercel (serverless simplicity) |

---

## ✅ Post-Deployment Checklist

- [ ] Application loads successfully
- [ ] Chat interface is responsive
- [ ] Medical queries return accurate responses
- [ ] Static files (CSS, logo) load correctly
- [ ] Environment variables are configured
- [ ] Logs show no errors
- [ ] Update README with Vercel deployment link

---

## 📝 Update README

After successful deployment, update your README.md:

```markdown
## 🌐 Live Demo

- **Render:** [https://medbot-jvsz.onrender.com](https://medbot-jvsz.onrender.com)
- **Vercel:** [https://medbot-your-project.vercel.app](https://medbot-your-project.vercel.app)
```

---

## 🎉 Success!

Your MedBot is now deployed on Vercel! 

**Next Steps:**
1. Test all functionalities
2. Monitor performance and logs
3. Share your live demo link
4. Update your CV with deployment details

---

## 📞 Support

- **Vercel Docs:** [https://vercel.com/docs](https://vercel.com/docs)
- **Vercel Community:** [https://github.com/vercel/vercel/discussions](https://github.com/vercel/vercel/discussions)

---

## 🔗 Useful Links

- [Vercel Python Runtime](https://vercel.com/docs/runtimes#official-runtimes/python)
- [Serverless Functions](https://vercel.com/docs/functions/serverless-functions)
- [Environment Variables](https://vercel.com/docs/projects/environment-variables)
