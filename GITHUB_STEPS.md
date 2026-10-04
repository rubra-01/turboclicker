# Exact Steps to Deploy 10 Instances on Railway

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `turboclicker` (or any name you want)
3. Make it **Private** (recommended)
4. Click "Create repository"
5. Copy the repository URL (e.g., `https://github.com/YOUR_USERNAME/turboclicker.git`)

## Step 2: Push to GitHub

Replace `YOUR_USERNAME` with your actual GitHub username:

```bash
# Rename branch to main
git branch -M main

# Add your actual GitHub repo (replace YOUR_USERNAME)
git remote set-url origin https://github.com/YOUR_USERNAME/turboclicker.git

# Push
git push -u origin main
```

## Step 3: Deploy 10 Instances on Railway

### Option A: 10 Separate Railway Projects (Recommended)

1. Go to https://railway.app and login
2. Click "New Project" → "Deploy from GitHub repo"
3. Select `turboclicker` repository
4. Wait for deployment (first one)
5. Repeat steps 2-4 nine more times to create 10 total projects

**Cost:** 10 projects × $5/month = $50/month

### Option B: One Project with Scaling (Not Recommended)

Railway doesn't support horizontal scaling for Docker services well. You'd need to modify the code to run multiple browser instances, which is complex and resource-intensive.

**Recommended:** Use Option A with 10 separate projects.

## Step 4: Monitor All 10 Instances

1. In Railway dashboard, you'll see all 10 projects
2. Each project has its own logs and metrics
3. All 10 will run independently, clicking in parallel

## Alternative: Use Railway CLI for Faster Setup

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Create first project
railway init
railway up

# For additional 9 projects, repeat:
railway init --project-name turboclicker-2
railway up
railway init --project-name turboclicker-3
railway up
# ... continue for turboclicker-4 through turboclicker-10
```

## Important Reminders

- **Cost:** 10 instances = $50/month minimum on Railway
- **Resource limits:** Each instance has CPU/memory limits
- **Performance:** May be slower than local due to cloud constraints
- **GitHub repo must be public or you must connect Railway to your GitHub account**

## Cheaper Alternative

If cost is a concern, consider:
- Running 10 instances locally on your machine (free)
- Using a cheaper VPS ($5-10/month for all instances)
- Using Render ($7/month per instance, similar to Railway)
