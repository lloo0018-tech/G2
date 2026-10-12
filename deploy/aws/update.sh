#!/usr/bin/env bash
# Run this on the server after you push new code to GitHub:
#   bash ~/app/deploy/aws/update.sh
set -euo pipefail
cd /home/ubuntu/app
git pull --ff-only
.venv/bin/pip install -r requirements.txt
sudo systemctl restart studentapp
echo "Updated and restarted."
