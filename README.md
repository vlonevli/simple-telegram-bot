# Simple Telegram Bot on Render

This is a minimal Telegram bot setup to run on Render as a Web Service.

## Prerequisites

1.  **Telegram Bot Token**: Get one from [@BotFather](https://t.me/BotFather).
2.  **Render Account**: Sign up at [render.com](https://render.com).

## How it works

- **Flask Server**: Listens on the port Render provides (`PORT` env var). This keeps the service "healthy" in Render's eyes.
- **Telegram Bot**: Runs in polling mode alongside the Flask server.

## Deployment

1.  Create a **New Web Service** on Render.
2.  Connect this repository.
3.  Add an **Environment Variable**:
    - Key: `TELEGRAM_TOKEN`
    - Value: `YOUR_BOT_TOKEN_HERE`
4.  Deploy!

## Local Testing

1.  Install dependencies: `pip install -r requirements.txt`
2.  Set token: `export TELEGRAM_TOKEN=your_token` (Linux/Mac) or `$env:TELEGRAM_TOKEN='your_token'` (Windows PowerShell)
3.  Run: `python main.py`
