import logging
from fastapi import FastAPI, Request
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from src.handlers import start, handle_voice, end, help, show_all_scores, clear
import os
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TELEGRAM_API_KEY")

app = FastAPI()
application = Application.builder().token(TOKEN).build()

# Register handlers
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('show', show_all_scores))
application.add_handler(CommandHandler('clear', clear))
application.add_handler(MessageHandler(filters.VOICE, handle_voice))
application.add_handler(CommandHandler('help', help))
application.add_handler(CommandHandler('end', end))

@app.post("/webhook")
async def telegram_webhook(request: Request):
    try:
        update = await request.json()
        logger.info(f"Received update: {update}")
        
        # Ensure the update contains the expected keys
        if "message" not in update:
            logger.error("No 'message' field found in update")
            return {"status": "error", "message": "Invalid update format"}, 400
        
        await application.update_queue.put(update)
        logger.info("Update successfully processed")
        return {"status": "ok"}

    except Exception as e:
        logger.error(f"Error processing update: {str(e)}", exc_info=True)
        return {"status": "error", "message": str(e)}, 500

@app.get("/")
async def root():
    return {"message": "Telegram Bot is running!"}
