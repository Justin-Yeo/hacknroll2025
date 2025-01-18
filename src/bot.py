from telegram.ext import Application, CommandHandler
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TELEGRAM_API_KEY")

# Define the function to handle the /start command using async
async def start(update, context):
    await update.message.reply_text('Bot is running')  # Use await here

def main():
    # Initialize the bot application with the token from the .env file
    application = Application.builder().token(TOKEN).build()

    # Register the command handler for the /start command
    application.add_handler(CommandHandler('start', start))

    # Start the bot (polling for updates)
    print("Bot is now running. Press Ctrl+C to stop.")
    application.run_polling()

if __name__ == "__main__":
    main()
