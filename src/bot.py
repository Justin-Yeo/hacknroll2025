from telegram.ext import Application, CommandHandler, MessageHandler, filters
import os
from dotenv import load_dotenv
from handlers import start, handle_voice, end, help, show_all_scores, clear

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TELEGRAM_API_KEY")

def main():
    # Initialize the bot application with the token from the .env file
    application = Application.builder().token(TOKEN).build()

    # Register the command handler for the /start command
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('show', show_all_scores))
    application.add_handler(CommandHandler('clear', clear))
    application.add_handler(MessageHandler(filters.VOICE, handle_voice))
    application.add_handler(CommandHandler('help', help))
    application.add_handler(CommandHandler('end', end))

    application.bot.set_my_commands([
        ('start', 'Start the game and get an introduction'),
        ('show', 'show the current scores'),
        ('clear', 'clear all existing scores'),
        ('end', 'End the game and see the final rankings'),
        ('help', 'Show help message')
    ])

    # Start the bot (polling for updates)
    print("Bot is now running. Press Ctrl+C to stop.")
    application.run_polling()

if __name__ == "__main__":
    main()