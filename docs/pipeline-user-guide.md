# Pipeline - User Guide

How to set up and run your Pipeline workspace. Companion to [[Pipeline - Service Delivery SOP]] and [[Pipeline - Governance & Data Covenant]].

## Advice

### Large files are not a source directory
Keep large files (video, disk images, raw photo libraries, archives, datasets) out of the ecosystem's source directories. Your vault, your synced workspace folder, and your config repo should hold working material only.

- Process large files in a controlled, one-at-a-time manner: stage, use, then archive.
- Park them in a separate cloud location (for example an "Archive" or "Media" area in Drive) set to online-only, not mirrored to every device.
- Link to them from notes instead of storing them in the vault.
- Never commit them to git. The config repo's `.gitignore` should exclude media and archive types by default.

Why: large files slow every sync, bloat backups and agent indexing, and turn a fast, local source of record into a slow one. They also make forks harder to detect and reconcile.
