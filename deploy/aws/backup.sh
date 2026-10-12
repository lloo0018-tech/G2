#!/usr/bin/env bash
# Makes a dated copy of the database in ~/backups:
#   bash ~/app/deploy/aws/backup.sh
set -euo pipefail
mkdir -p ~/backups
cp /home/ubuntu/app/data/app.db ~/backups/app-$(date +%Y%m%d-%H%M%S).db
ls -1t ~/backups | head -5
