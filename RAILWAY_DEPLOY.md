# Railway Deployment Guide

## Prerequisites
- Railway account (sign up at railway.app)
- GitHub account
- This project pushed to GitHub

## Steps to Deploy

### 1. Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

### 2. Create Railway Project

1. Go to [railway.app](https://railway.app)
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository
5. Railway will detect the Dockerfile automatically

### 3. Configure Service

Railway will build and deploy using the Dockerfile. The service will:
- Install Python 3.11
- Install Playwright and Chromium
- Run the autoclicker in headless mode

### 4. Important Notes

**Cost Warning:**
- Railway charges $5/month minimum for the Eco plan
- Browser automation is resource-intensive
- May need to upgrade to higher tier for stability

**Limitations:**
- Railway has CPU/memory limits that may affect browser performance
- The autoclicker may be slower than local execution
- Railway services restart on failures (configured in railway.json)

**Monitoring:**
- View logs in Railway dashboard
- Check metrics tab for resource usage
- May need to adjust based on performance

### 5. Alternative: Use Railway CLI

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Deploy
railway up
```

## Troubleshooting

**Build fails:**
- Check Dockerfile syntax
- Verify requirements.txt has correct dependencies

**Runtime errors:**
- Check Railway logs
- May need to increase memory/CPU allocation
- Browser may timeout due to resource limits

**Service keeps restarting:**
- Normal behavior for long-running browser tasks
- Adjust restartPolicy in railway.json if needed

## Local Testing Before Deploy

Test locally with Docker first:

```bash
docker build -t autoclicker .
docker run -it autoclicker
```
