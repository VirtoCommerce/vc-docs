# Versioning System Usage Examples

## 📌 Scenario 1: Update Documentation Without Version Change

**Situation**: Need to fix typos or update content in current version.

**Steps**:
1. Current version in `VERSION`: `1.0.0`
2. Version `1.0.0` already deployed
3. Make changes to documents
4. Run: `./build-versioned-local.sh`

**Result**:
```
Reading version from local configuration...
Current version in file: 1.0.0
Last deployed version: 1.0.0
Version 1.0.0 already deployed. Will update content.
Will update existing version: 1.0.0
```
✅ Content of version 1.0.0 updated, URL remains the same.

---

## 📌 Scenario 2: Release New Version

**Situation**: Ready to release a new version of documentation.

**Steps**:
1. Change version:
   ```bash
   echo "1.1.0" > VERSION
   ```

2. Update `version.json`:
   ```json
   {
     "version": "1.1.0",
     "alias": "latest",
     "title": "VirtoCommerce Documentation v1.1.0",
     "changelog": ["New features", "Fixes"]
   }
   ```

3. Run: `./build-versioned-local.sh`

**Result**:
```
Reading version from local configuration...
Current version in file: 1.1.0
Last deployed version: 1.0.0
New version 1.1.0. Will create new deployment.
Will create new version: 1.1.0
```
✅ Created new version 1.1.0 with alias latest.

---

## 📌 Scenario 3: GitHub Actions Automatic Deployment

**Situation**: Set up CI/CD for automatic deployment.

**Workflow setup**:
- version: `auto`
- alias: `auto`
- deploy_mode: `versioned`

**Behavior**:
- System reads `VERSION` file
- Checks if this version is deployed
- **If yes** → updates content
- **If no** → creates new version

---

## 📌 Scenario 4: Working with Development Version

**Situation**: Need separate version for development.

**Steps**:
1. Create dev version:
   ```bash
   echo "dev" > VERSION
   ```

2. Deploy:
   ```bash
   ./build-versioned-local.sh
   ```

**Result**:
- Creates `dev` version
- Available at URL: `/dev/`
- Can be updated without version change

---

## 📌 Scenario 5: Emergency Rollback

**Situation**: Need to quickly rollback to previous version.

**Option 1 - Switch alias**:
```bash
mike alias 1.0.0 latest --push
```

**Option 2 - Delete problematic version**:
```bash
mike delete 1.1.0 --push
mike alias 1.0.0 latest --push
```

**Option 3 - Via VERSION file**:
```bash
echo "1.0.0" > VERSION
./build-versioned-local.sh
```

---

## 📌 Scenario 6: Multiple Active Versions

**Situation**: Maintain multiple versions simultaneously.

**Structure**:
```
1.0.0 [stable] - stable version for production
1.1.0 [latest] - latest version
dev            - development version
```

**Update old version**:
```bash
echo "1.0.0" > VERSION
# Make critical fixes
./build-versioned-local.sh
# Content 1.0.0 updated
```

**Update latest**:
```bash
echo "1.1.0" > VERSION
# Make changes
./build-versioned-local.sh
# Content 1.1.0 updated
```

---

## 💡 Useful Commands

### Pre-deployment check:
```bash
# What will the system do?
python3 version-utils.py check-should-update
```

### View versions:
```bash
# All deployed versions
mike list

# Local preview
mike serve
```

### Alias management:
```bash
# Add alias
mike alias 1.0.0 stable

# Change default version
mike set-default latest
```

---

## 📋 Release Checklist

- [ ] Update `VERSION` file
- [ ] Update `version.json` with changelog
- [ ] Check: `python3 version-utils.py check-should-update`
- [ ] Run locally: `./build-versioned-local.sh`
- [ ] Verify: `mike serve`
- [ ] Commit changes
- [ ] Run GitHub Actions

---

## ⚠️ Common Errors

### Error: "Version not updating"
**Cause**: Forgot to change `VERSION` file
**Solution**: Check `VERSION` content

### Error: "Alias not working"
**Cause**: Not specified in `version.json`
**Solution**: Add `"alias": "latest"` to `version.json`

### Error: "Mike cannot find versions"
**Cause**: No `gh-pages` branch
**Solution**: Script will create it automatically on first run