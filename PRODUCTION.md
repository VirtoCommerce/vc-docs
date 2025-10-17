# Production Setup Guide

This guide explains how to set up the documentation versioning system for production use.

## GitHub Pages Setup

### 1. Enable GitHub Pages

1. Go to your repository settings
2. Navigate to "Pages" section
3. Set source to "Deploy from a branch"
4. Select `gh-pages` branch and `/` (root) folder
5. Click "Save"

### 2. Configure Repository Secrets (if using private repo)

If your repository is private, add these secrets in Settings > Secrets and variables > Actions:

- `GITHUB_TOKEN` (usually available by default)

## Domain Configuration

### Option 1: GitHub Pages Default Domain

Your documentation will be available at:
`https://[username].github.io/[repository-name]/`

### Option 2: Custom Domain

1. Add a `CNAME` file to the gh-pages branch with your domain:
   ```
   docs.yourdomain.com
   ```

2. Configure DNS records:
   ```
   Type: CNAME
   Name: docs
   Value: [username].github.io
   ```

3. Enable HTTPS in repository settings

## Workflow Setup

### 1. Copy GitHub Action

The workflow file `.github/workflows/deploy-docs.yml` handles automatic deployment.

### 2. Branch Protection (Recommended)

1. Go to Settings > Branches
2. Add rule for `main` branch
3. Require status checks to pass
4. Require branches to be up to date

### 3. Version Management Strategy

Choose your versioning strategy:

#### Strategy A: Semantic Versioning
```json
{
  "version": "v3.800",
  "alias": "latest",
  "title": "v3.800 (Latest)",
  "update_mode": "replace"
}
```

#### Strategy B: Date-based Versioning
```json
{
  "version": "2025-01",
  "alias": "latest", 
  "title": "January 2025",
  "update_mode": "replace"
}
```

#### Strategy C: Branch-based
- `main` branch → `latest` version
- `release/v3.x` → specific version
- `dev` branch → `development` version

## CI/CD Integration

### From Another Repository

If you want to trigger documentation deployment from another repository:

#### 1. Create Repository Dispatch Trigger

In your docs repository, add this workflow (`.github/workflows/external-deploy.yml`):

```yaml
name: External Documentation Deploy

on:
  repository_dispatch:
    types: [deploy-docs]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout documentation
      uses: actions/checkout@v4
      with:
        repository: YourOrg/vc-docs
        token: ${{ secrets.DOCS_TOKEN }}
        
    - name: Update version
      run: |
        echo '{
          "version": "${{ github.event.client_payload.version }}",
          "alias": "${{ github.event.client_payload.alias }}",
          "title": "${{ github.event.client_payload.title }}",
          "update_mode": "replace"
        }' > version.json
        
    - name: Deploy
      run: ./deploy-auto-version.sh
```

#### 2. Trigger from External Repository

In your main application repository:

```yaml
- name: Trigger Documentation Deploy
  uses: peter-evans/repository-dispatch@v2
  with:
    token: ${{ secrets.DOCS_TOKEN }}
    repository: YourOrg/vc-docs
    event-type: deploy-docs
    client-payload: |
      {
        "version": "${{ steps.version.outputs.version }}",
        "alias": "latest",
        "title": "${{ steps.version.outputs.version }} (Latest)"
      }
```

## Monitoring and Maintenance

### 1. Monitor Deployments

- Check Actions tab for deployment status
- Monitor GitHub Pages deployments in Settings > Pages
- Set up notifications for failed deployments

### 2. Version Cleanup

Periodically clean up old versions:

```bash
# List all versions
./list-versions.sh

# Manual cleanup (run locally)
git checkout gh-pages
rm -rf old-version-folder
git add .
git commit -m "Remove old version"
git push origin gh-pages
```

### 3. Analytics (Optional)

Add Google Analytics to track documentation usage:

1. Add your GA tracking ID to `mkdocs.yml`:
   ```yaml
   google_analytics:
     - 'UA-XXXXXXXX-X'
     - 'auto'
   ```

2. Track version usage with custom events

## Security Considerations

### 1. Branch Protection

Protect your main branches to prevent unauthorized changes:
- Require pull request reviews
- Require status checks
- Restrict pushes to specific people/teams

### 2. Secrets Management

- Never commit sensitive information
- Use GitHub secrets for tokens
- Rotate secrets regularly

### 3. Content Review

- Set up branch protection rules
- Require reviews for documentation changes
- Use automated content scanning if needed

## Troubleshooting

### Common Issues

1. **"gh-pages branch not found"**
   - Ensure gh-pages branch exists
   - Check if initial deployment completed

2. **"Version selector not working"**
   - Verify versions.json exists and is valid
   - Check browser console for JavaScript errors
   - Ensure assets are loading correctly

3. **"Links broken between sections"**
   - Check relative path configuration
   - Verify all sections are built correctly
   - Test locally first

4. **"GitHub Pages not updating"**
   - Check Actions tab for deployment status
   - Verify gh-pages branch has latest content
   - Clear browser cache

### Support Checklist

- [ ] GitHub Pages enabled
- [ ] Workflow permissions configured
- [ ] Domain (if custom) configured
- [ ] SSL certificate active
- [ ] Version selector working
- [ ] All sections accessible
- [ ] Links between sections working
- [ ] Search functionality working

## Maintenance Schedule

**Weekly:**
- Review deployment logs
- Test version selector
- Check for broken links

**Monthly:**
- Update dependencies
- Review and clean old versions
- Update documentation

**Quarterly:**
- Security audit
- Performance review
- Backup validation