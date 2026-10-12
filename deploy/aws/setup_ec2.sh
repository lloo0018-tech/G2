#!/usr/bin/env bash
# =============================================================================
# One-command setup for an AWS EC2 server (Ubuntu 22.04 or 24.04).
#
# Usage (on the server, after you connect with SSH):
#   curl -fsSL https://raw.githubusercontent.com/YOUR-USER/YOUR-REPO/main/deploy/aws/setup_ec2.sh -o setup.sh
#   bash setup.sh https://github.com/YOUR-USER/YOUR-REPO.git
#
# What it does:
#   1. Installs Python, git and nginx
#   2. Downloads your code into /home/ubuntu/app
#   3. Creates a .env file with a random SECRET_KEY
#   4. Runs the app with gunicorn as a service (starts again after reboot)
#   5. Puts nginx in front so the app is on http://YOUR-SERVER-IP
#
# Safe to run again: it updates the code and restarts the app.
# =============================================================================
set -euo pipefail

REPO_URL="${1:-}"
APP_DIR="/home/ubuntu/app"
SERVICE="studentapp"

if [ -z "$REPO_URL" ] && [ ! -d "$APP_DIR/.git" ]; then
  echo "Usage: bash setup.sh https://github.com/YOUR-USER/YOUR-REPO.git"
  exit 1
fi

echo "==> 1/5 Installing system packages"
sudo apt-get update -y
sudo apt-get install -y python3 python3-venv python3-pip git nginx

echo "==> 2/5 Getting the code"
if [ -d "$APP_DIR/.git" ]; then
  git -C "$APP_DIR" pull --ff-only
else
  git clone "$REPO_URL" "$APP_DIR"
fi
cd "$APP_DIR"

echo "==> 3/5 Installing Python packages"
python3 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt
mkdir -p data

if [ ! -f .env ]; then
  echo "    Creating .env with a new random SECRET_KEY"
  {
    echo "SECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_hex(32))')"
    echo "APP_NAME=Student App"
    echo "DATABASE=$APP_DIR/data/app.db"
  } > .env
  chmod 600 .env
fi

echo "==> 4/5 Creating the app service"
sudo tee /etc/systemd/system/$SERVICE.service > /dev/null <<UNIT
[Unit]
Description=Student App (gunicorn)
After=network.target

[Service]
User=ubuntu
WorkingDirectory=$APP_DIR
EnvironmentFile=$APP_DIR/.env
ExecStart=$APP_DIR/.venv/bin/gunicorn app:app --bind 127.0.0.1:8000 --workers 2
Restart=always

[Install]
WantedBy=multi-user.target
UNIT
sudo systemctl daemon-reload
sudo systemctl enable $SERVICE
sudo systemctl restart $SERVICE

echo "==> 5/5 Setting up nginx"
sudo tee /etc/nginx/sites-available/$SERVICE > /dev/null <<'NGINX'
server {
    listen 80 default_server;
    server_name _;
    client_max_body_size 5M;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
NGINX
sudo ln -sf /etc/nginx/sites-available/$SERVICE /etc/nginx/sites-enabled/$SERVICE
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx

sleep 2
if curl -fs http://127.0.0.1/health > /dev/null; then
  IP=$(curl -fs --max-time 3 https://checkip.amazonaws.com || echo "YOUR-SERVER-IP")
  echo ""
  echo "SUCCESS! Your app is live at:  http://$IP"
else
  echo ""
  echo "Something went wrong. See the logs with:"
  echo "  sudo journalctl -u $SERVICE -n 50 --no-pager"
  exit 1
fi
