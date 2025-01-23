from telegram.ext import Application, CommandHandler, MessageHandler, filters
from fastapi import FastAPI, Request
import os
from dotenv import load_dotenv
from handlers import start, handle_voice, end, help, show_all_scores, clear

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TELEGRAM_API_KEY")

# Initialize FastAPI app
app = FastAPI()

# Initialize the bot application with the token from the .env file
application = Application.builder().token(TOKEN).build()

# Register the command handlers
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('show', show_all_scores))
application.add_handler(CommandHandler('clear', clear))
application.add_handler(MessageHandler(filters.VOICE, handle_voice))
application.add_handler(CommandHandler('help', help))
application.add_handler(CommandHandler('end', end))

# Set bot commands
async def set_commands():
    await application.bot.set_my_commands([
        ('start', 'Start the game and get an introduction'),
        ('show', 'Show the current scores'),
        ('clear', 'Clear all existing scores'),
        ('end', 'End the game and see the final rankings'),
        ('help', 'Show help message')
    ])

@app.post("/webhook")
async def telegram_webhook(request: Request):
    update = await request.json()
    await application.update_queue.put(update)
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"message": "Telegram Bot is running!"}

@app.on_event("startup")
async def startup_event():
    await set_commands()
    print("Bot commands have been set successfully.")
