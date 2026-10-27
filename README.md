# vault-config (private)

Configuration and templates for Jon's personal operating system and the Pipeline framework.

- **System of record for data:** Google Drive (tickets, media, records) and the Obsidian vault at `~/Vault`.
- **This repo:** structure only. Obsidian settings, Pipeline templates, scripts, and docs.
- **Never here:** resumes, trackers, financial or health records, media, credentials. `.gitignore` is deny-by-default.

## Layout
- `obsidian/` vault settings and plugin manifests (plugin code reinstalls from community plugins)
- `templates/pipeline/` Pipeline template metadata (VHS to Digital, Water Source Assessment)
- `scripts/` helper scripts
- `docs/` Pipeline User Guide

## Restore Obsidian settings into a vault
```
cp -R obsidian/* ~/Vault/.obsidian/
```
Then reinstall the community plugins listed in `obsidian/community-plugins.json`.

Private until release alongside a public social and technical launch.
