from telegram import Update
from telegram.ext import ContextTypes
from audio_utils import processVoice
from game_logic import update_score, get_current_rankings, clear_scores

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    intro_message = (
        "Welcome to the Voice Loudness Game Bot! 🎉\n\n"
        "Send a voice message to participate in the game. "
        "The bot will measure the loudness of your voice and rank you against other participants. "
        "Type /end to finish the game and see the final rankings. Have fun!"
    )
    await update.message.reply_text(intro_message)

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.message.from_user
        file_id = update.message.voice.file_id
        loudness = await processVoice(context.bot, file_id)
        update_score(user.id, user.username, loudness)
        rankings = get_current_rankings()
        await update.message.reply_text(f"Loudness: {loudness} dB\nCurrent Rankings:\n{rankings}")
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {e}")
        print(f"Error: {e}")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_message = (
        "Voice Loudness Game Bot Help:\n\n"
        "/start - Start the game and get an introduction.\n"
        "/end - End the game and see the final rankings.\n"
        "/help - Show this help message.\n\n"
        "Send a voice message to participate in the game. The bot will measure the loudness of your voice and rank "
        "you against other participants."
    )
    await update.message.reply_text(help_message)
async def end(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        rankings = get_current_rankings()
        if rankings:
            final_message = f"Game Over! Here are the final rankings:\n{rankings}"
        else:
            final_message = "No participants recorded any voice messages."
        await update.message.reply_text(final_message)
        clear_scores()
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {e}")
        print(f"Error: {e}")