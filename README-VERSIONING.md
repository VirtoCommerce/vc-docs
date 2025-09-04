# 📚 Documentation Versioning

This repository now supports automatic versioning using `mike` with configuration-based deployment.

## 🚀 Quick Start

1. **Main Guide**: [`VERSION-MANAGEMENT.md`](./VERSION-MANAGEMENT.md) - Complete guide to the new system
2. **Migration**: [`MIGRATION-GUIDE.md`](./MIGRATION-GUIDE.md) - How to migrate from old workflows

## ⚡ TL;DR

### Set Version:
```json
// version-config.json
{
  "version": "3.800",
  "alias": "latest", 
  "setDefault": true,
  "deployOnPush": true,
  "description": "Current version"
}
```

### Deploy:
```bash
git push  # That's it! Automatic deployment based on config
```

### Result:
- Same version → Updates existing docs
- New version → Creates new version alongside old ones
- All versions available simultaneously

## 📖 Documentation Files

- **[VERSION-MANAGEMENT.md](./VERSION-MANAGEMENT.md)** - Main documentation for new system
- **[MIGRATION-GUIDE.md](./MIGRATION-GUIDE.md)** - Migration guide from old workflows
- **[docker-files-structure.md](./docker-files-structure.md)** - Docker integration details

## 🛠️ Scripts

- `./check-version-update.sh` - Check if version should be deployed
- `./deploy-from-config.sh` - Deploy based on version-config.json
- `./manage-versions.sh` - Manage versions (list, delete, alias)

---

**Start with [`VERSION-MANAGEMENT.md`](./VERSION-MANAGEMENT.md) for complete instructions.**