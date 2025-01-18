from telegram import Update
from telegram.ext import ContextTypes
from audio_utils import processVoice, convert_dbfs_to_score
from game_logic import update_score, get_current_rankings, get_all_scores, clear_scores, is_first_time
import json

# Game state tracking
game_active = False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global game_active
    game_active = True
    intro_message = (
        "Welcome to the Voice Loudness Game Bot! 🎉\n\n"
        "Send a voice message to participate in the game. "
        "Type /end to finish the game. Have fun!"
    )
    await update.message.reply_text(intro_message)

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global game_active
    if not game_active:
        await update.message.reply_text("The game is not active. Type /start to begin!")
        return
    
    try:
        user = update.message.from_user
        print(user)
        file_id = update.message.voice.file_id
        loudness = await processVoice(context.bot, file_id)
        loudness_score = convert_dbfs_to_score(loudness)
        player_first_time = is_first_time(user.id)
        new_best = update_score(user.id, user.username, loudness_score)
        rankings = get_current_rankings()
        
        if player_first_time: 
            await update.message.reply_text(f"Well done, {user.first_name}! Amazing first attempt with {loudness_score} pts!\n\nCurrent Rankings:\n{rankings}")
        elif new_best:
            await update.message.reply_text(f"Congrats, {user.first_name}! You just beat your previous record with {loudness_score} pts!\n\nCurrent Rankings:\n{rankings}")
        else:
            await update.message.reply_text(f"Your new attempt: {loudness_score} pts, {user.first_name}!\nYou didn’t beat your previous best — keep trying!\n\nCurrent Rankings:\n{rankings}")
        
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {e}")
        print(f"Error: {e}")

async def show_all_scores(update, context):
    """Command to show scores for all users."""
    scores_message = get_all_scores()
    await update.message.reply_text(f"📊 All Scores:\n{scores_message}")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_message = (
        "Voice Loudness Game Bot Help:\n\n"
        "/start - Start the game and get an introduction.\n"
        "/show - See the current rankings.\n"
        "/end - End the game and see the final rankings.\n"
        "/help - Show this help message.\n\n"
        "Send a voice message to participate in the game. The bot will measure the loudness of your voice and rank "
        "you against other participants."
    )
    await update.message.reply_text(help_message)

async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Command to clear all scores from the JSON file."""
    try:
        clear_scores()  # Call the function to clear the scores
        await update.message.reply_text("All scores have been cleared!")
    except Exception as e:
        await update.message.reply_text(f"An error occurred while clearing the scores: {e}")
        print(f"Error: {e}")

        
async def end(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global game_active
    if not game_active:
        await update.message.reply_text("The game is already inactive. Type /start to begin!")
        return

    game_active = False
    try:
        rankings = get_current_rankings()
        if rankings:
            final_message = f"Game Over! Here are the final rankings:\n{rankings}"
        else:
            final_message = "No participants recorded any voice messages."
        await update.message.reply_text(final_message)
        end_message = (
            "The game has ended! Voice message detection is now disabled. "
            "Type /start to begin a new game."
        )
        await update.message.reply_text(end_message)
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {e}")
        print(f"Error: {e}")
