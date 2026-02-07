# Deploy to Netlify (Static + Serverless Functions)

**✅ Your app is now Netlify-friendly!**

---

## Why This Approach?

- ✅ Static HTML pages (fast & reliable)
- ✅ Serverless functions for feedback/submissions (no backend needed)
- ✅ Free tier: Unlimited sites & builds
- ✅ Auto-deploy from GitHub
- ✅ Custom domain support

---

## Step 1: Test Locally

Build static pages:
```bash
cd "c:\Users\DeLL\Desktop\files"
C:/Users/DeLL/Desktop/files/.venv/Scripts/python.exe build_static.py
```

This creates a `dist/` folder with all static HTML pages ready for Netlify.

---

## Step 2: Push to GitHub

```bash
cd "c:\Users\DeLL\Desktop\files"
git add .
git commit -m "Convert to Netlify: static site + serverless functions"
git push origin main
```

---

## Step 3: Deploy on Netlify

### Option A: Netlify Dashboard (Easiest)

1. Go to **https://app.netlify.com**
2. Click **"Add new site"** → **"Import an existing project"**
3. Choose **GitHub**
4. Select your repository: `baloch-culture-platform`
5. Settings:
   - Build command: `pip install -r requirements.txt && python build_static.py`
   - Publish directory: `dist`
6. Click **"Deploy site"**

### Option B: Netlify CLI

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Login
netlify login

# Deploy
cd "c:\Users\DeLL\Desktop\files"
netlify deploy --prod
```

---

## Step 4: Your Live Site

Your site will be at:
```
https://your-site-name.netlify.app
```

**OR with custom domain:**
```
https://baloch-culture.com (if you own domain)
```

---

## What Gets Deployed?

### Static Pages (Auto-generated)
- ✅ `index.html` - Home page
- ✅ `/region/eastern/` - Eastern region page
- ✅ `/region/western/` - Western region page
- ✅ `/region/southern/` - Southern region page
- ✅ `/privacy/` - Privacy policy
- ✅ `/feedback/` - Feedback page
- ✅ `/collaborate/` - Collaboration page
- ✅ `/submissions/` - View submissions

### Static Assets
- ✅ `/static/style.css` - All styling
- ✅ `/static/main.js` - JavaScript
- ✅ `/static/audio/` - All audio files
- ✅ `/static/images/` - Logo and images
- ✅ `/static/ads.js` - Ad system

### Serverless Functions
- ✅ `/.netlify/functions/feedback` - Save feedback
- ✅ `/.netlify/functions/collaborate` - Save collaborations

---

## Important Files

### netlify.toml
- ✅ Build command configured
- ✅ Functions directory: `netlify/functions/`
- ✅ Publish directory: `dist/`
- ✅ URL rewrites for SPA routing

### build_static.py
- ✅ Generates all static pages from templates
- ✅ Runs during Netlify build
- ✅ Creates proper directory structure

### netlify/functions/*.py
- ✅ Serverless functions for form submissions
- ✅ Save data to JSON files
- ✅ Handle feedback and collaborations

---

## Auto-Deploy from GitHub

Every time you push to GitHub:
1. Netlify detects changes
2. Runs `build_static.py`
3. Deploys new version automatically
4. Site updates in 2-3 minutes

---

## Update Content

To update your site:

1. **Edit Balochi content:**
   - Modify `data_enhanced.py`
   - Push to GitHub
   - Netlify auto-rebuilds

2. **Edit pages:**
   - Modify templates in `templates/`
   - Push to GitHub
   - Netlify auto-rebuilds

3. **Add new audio/images:**
   - Add to `static/audio/` or `static/images/`
   - Update `data_enhanced.py` with references
   - Push to GitHub
   - Netlify auto-rebuilds

---

## Troubleshooting

### Build fails?
- Check build logs: Netlify Dashboard → Deploys → Click deploy → View logs
- Ensure `requirements.txt` has all dependencies
- Verify `build_static.py` runs locally first

### Functions not working?
- Check function logs: Functions → Click function → View logs
- Ensure `netlify/functions/` directory exists
- Verify functions have `.py` extension

### Styles not loading?
- Ensure `dist/` is published directory
- Check CSS paths are relative
- Clear browser cache (Ctrl+Shift+Del)

### Audio files not playing?
- Verify audio files are in `static/audio/`
- Check file paths in `data_enhanced.py`
- Ensure netlify.toml has correct publish directory

---

## Monitoring

**Track your site's performance:**

1. Netlify Dashboard → Analytics
2. See:
   - Unique visitors
   - Page views
   - Traffic sources
   - Performance metrics

---

## Custom Domain

To use your own domain (optional):

1. Buy domain from: GoDaddy, Namecheap, Google Domains
2. In Netlify: Domain management → Add domain
3. Update DNS records per Netlify instructions
4. Your site: `https://baloch-culture.com`

---

## Next Steps

1. ✅ Commit all changes to GitHub
2. ✅ Go to Netlify and connect repository
3. ✅ Click "Deploy"
4. ✅ Wait 2-3 minutes
5. ✅ Your site is live! 🎉

---

## Key Differences from Flask

| Feature | Flask (Heroku) | Static (Netlify) |
|---------|---|---|
| Server | Always running | Serverless |
| Cost | Free tier limited | Free & unlimited |
| Performance | Slower (cold starts) | Very fast |
| Deployment | Automatic | Automatic |
| Database | Supported | Use serverless DB or JSON |
| Scaling | Need more dynos | Automatic |
| Cold starts | 30 sec delay | None (static files) |

---

**Your Baloch Culture Platform is now Netlify-ready!** 🚀

Deploy in **5 minutes** with automatic updates from GitHub! ✨
