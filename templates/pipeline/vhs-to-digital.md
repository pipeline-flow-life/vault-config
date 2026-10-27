---
template: vhs-to-digital
type: workflow
version: 0.1
status: draft
reference_run: HOT-0004 (ticket in Google Drive, Pipeline/)
data_location: google-drive   # tickets and media live in Drive, never in this repo
---

# Template: VHS to Digital

Convert analog tape to durable digital files, classify by audience, and keep masters out of the working ecosystem.

## Inputs
- tape_id, tape_label, physical_location
- capture_device (make/model), capture_host (machine/OS), capture_software
- source_format (VHS, VHS-C, Hi8, MiniDV)

## Classification tiers
- public: safe to share or post
- private: family / named individuals only
- restricted: default on capture until reviewed

## Stages
1. Inventory: list tapes, labels, condition, location
2. Capture: raw master per tape segment, named `<Event> (<Source>).<ext>`
3. Land: upload master to Drive `Media/<Collection>/restricted/`, set online-only
4. Review: watch, reclassify to public/private/restricted, note people and dates
5. Derive: transcode delivery copy (default H.264 MP4); keep master
6. Publish (optional): public tier only, per social/release plan
7. Close: update ticket with counts, sizes, open items

## Ticket fields
status, opened, owner, collection, files[] (name, format, size, captured, tier), toolkit, open_questions[], next_actions[]

## Guardrails
- Media never enters the vault or this repo (see Pipeline User Guide: large files are not a source directory)
- Restricted is the default tier until a human reviews the file
