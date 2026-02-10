import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Flask App for Render Health Check
app = Flask(__name__)

@app.route('/')
def hello():
    return "Bot is alive! verified"

def run_flask():
    # Render assigns the port to the PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

# Bot Logic
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am running on Render.")

if __name__ == '__main__':
    # Start Flask in a separate thread so Render detects a binded port
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Get Token
    token = os.environ.get("TELEGRAM_TOKEN")
    
    if not token:
        print("ERROR: TELEGRAM_TOKEN environment variable is not set.")
        print("The web server is running, but the bot will not start without a token.")
        # We keep the script running so the web server stays alive to report the error
        flask_thread.join()
    else:
        print("Starting Bot...")
        # Create the Application
        application = ApplicationBuilder().token(token).build()

        # Add handlers
        start_handler = CommandHandler('start', start)
        application.add_handler(start_handler)

        # Run the bot
        # This blocks, so it ensures the program keeps running
        application.run_polling()
