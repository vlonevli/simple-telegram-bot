import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am running on Render with Webhooks!")

if __name__ == '__main__':
    token = os.environ.get("TELEGRAM_TOKEN")
    if not token:
        logging.error("TELEGRAM_TOKEN environment variable is not set.")
        exit(1)

    application = ApplicationBuilder().token(token).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Render specific configuration
    port = int(os.environ.get("PORT", "8443"))
    render_external_url = os.environ.get("RENDER_EXTERNAL_URL")

    if render_external_url:
        logging.info(f"Starting webhook on port {port}, url: {render_external_url}")
        application.run_webhook(
            listen="0.0.0.0",
            port=port,
            url_path=token,
            webhook_url=f"{render_external_url}/{token}"
        )
    else:
        logging.warning("RENDER_EXTERNAL_URL not found. Falling back to polling for local testing.")
        application.run_polling()
