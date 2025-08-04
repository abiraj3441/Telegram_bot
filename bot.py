# bot.py

import asyncio
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Load the token from the .env file
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not set in the .env file.")

# Message handler function
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"You said: {user_message}")

# Main entry to run the bot
async def main():
    # Build the application (this is the equivalent of creating an Updater in v20+)
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add the handler for text messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start polling for updates (new in v20+)
    print("Bot is running...")
    await app.run_polling()  # This replaces 'updater.start_polling()' from older versions

# Entry point for the script
def run():
    loop = asyncio.get_event_loop()

    # If the event loop is already running, create a task instead of using asyncio.run
    if loop.is_running():
        asyncio.create_task(main())  # Start the main function as a task
    else:
        loop.run_until_complete(main())  # If not running, start the event loop normally

# Start the bot
if __name__ == '__main__':
    run()
