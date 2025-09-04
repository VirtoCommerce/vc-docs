# Version-Based Documentation Deployment

This system allows you to control documentation versions locally through configuration files.

## How It Works

1. **Version Control**: Version information is stored in `version-config.json`
2. **Always Deploy**: GitHub Actions deploys on every push (if enabled)
3. **Smart Version Management**: 
   - Same version → Updates existing version documentation
   - New version → Creates new version alongside existing ones
4. **No Manual Inputs**: No need to specify version/alias in GitHub Actions UI

## Configuration File: `version-config.json`

```json
{
  "version": "3.800",
  "alias": "latest",
  "setDefault": true,
  "deployOnPush": true,
  "description": "Main documentation version"
}
```

### Configuration Options:

- **`version`**: Documentation version (e.g., "3.800", "4.0-beta")
- **`alias`**: Version alias (e.g., "latest", "stable", "dev")
- **`setDefault`**: Whether to set this as the default version (true/false)
- **`deployOnPush`**: Whether to auto-deploy on push (true/false)
- **`description`**: Human-readable description of this version

## Workflow for Version Updates

### 1. Regular Development (Same Version)
```bash
# Make documentation changes
git add .
git commit -m "Update documentation content"
git push
```
**Result**: ✅ Deployment happens - **UPDATES** existing version 3.800

### 2. New Version Release
```bash
# 1. Update version configuration
vim version-config.json
# Change version to "3.810" and update description

# 2. Commit changes
git add version-config.json
git commit -m "Release documentation version 3.810"
git push
```
**Result**: ✅ **NEW** version 3.810 deployed alongside existing 3.800!

### 3. Disable Auto-Deployment
```json
{
  "version": "3.800",
  "alias": "latest",
  "setDefault": true,
  "deployOnPush": false,  // ← Disable auto-deployment
  "description": "Work in progress"
}
```
**Result**: ✅ No deployments until you set `deployOnPush: true`

## Local Testing

### Test Version Check
```bash
# Check if current version would be deployed
./check-version-update.sh
```

### Deploy Locally
```bash
# Deploy from config without pushing to remote
./deploy-from-config.sh

# Deploy and push to remote (like GitHub Actions does)
./deploy-from-config.sh --push
```

## GitHub Actions Behavior

### Auto-Deploy Triggers:
- Push to `main`, `master`, or `feature/structure_redesign` branches
- Manual workflow dispatch

### Smart Skipping:
- ✅ Deploys only when `version-config.json` changes
- ✅ Skips deployment if same version was already deployed
- ✅ Respects `deployOnPush: false` setting

### GitHub Actions Logs:
```
✅ New version 3.800 ready for deployment
🚀 Deploying from configuration file...
📦 Deploying version 3.800 with alias latest...
🎯 Setting 3.800 as default version...
✅ Successfully deployed version 3.800
```

OR

```
⏭️ Version 3.800 already deployed, skipping
🚫 Deployment disabled in version-config.json (deployOnPush: false)
```

## Example Scenarios

### Scenario 1: Major Version Release
```json
{
  "version": "4.000",
  "alias": "latest",
  "setDefault": true,
  "deployOnPush": true,
  "description": "Major release v4.0"
}
```

### Scenario 2: Beta Version
```json
{
  "version": "4.1-beta",
  "alias": "beta",
  "setDefault": false,
  "deployOnPush": true,
  "description": "Beta version for testing"
}
```

### Scenario 3: Hotfix
```json
{
  "version": "3.800.1",
  "alias": "stable",
  "setDefault": false,
  "deployOnPush": true,
  "description": "Critical hotfix for v3.800"
}
```

## Benefits

✅ **No Manual GitHub Actions**: No need to remember version numbers in UI
✅ **Version Control**: Version info is tracked in git alongside code  
✅ **Always Up-to-Date**: Deploys on every push to keep docs current
✅ **Smart Versioning**: Updates existing version OR creates new version automatically
✅ **Fail-Safe**: Can disable deployment with `deployOnPush: false`
✅ **Audit Trail**: Git history shows exactly when versions were released
✅ **Team Friendly**: Everyone can see version plans in pull requests

## Migration from Old System

1. **Create `version-config.json`** with your current version
2. **Set `deployOnPush: false`** initially to test
3. **Test locally** with `./check-version-update.sh`
4. **Enable with `deployOnPush: true`** when ready
5. **Remove old manual workflows** that use inputs
