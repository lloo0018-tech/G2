# Builds a container that runs the app with gunicorn on port 8000.
# Works on AWS (EC2, App Runner, ECS), Render, Railway, Fly.io, Google Cloud Run, etc.
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DATABASE=/app/data/app.db \
    PORT=8000

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN useradd --create-home appuser && mkdir -p /app/data && chown -R appuser /app
USER appuser

EXPOSE 8000
CMD gunicorn app:app --bind 0.0.0.0:${PORT} --workers 2 --access-logfile -
