# LoudestWins Telegram Bot

## 📖 Project Overview

**LoudestWins** is a fun group game for measuring and comparing the loudness of participants’ voice messages in a Telegram chat. Each user sends a voice message, the bot measures its decibel level, then tracks and ranks everyone’s submissions. At the end of the round, the bot declares the winner with the highest decibel reading, bringing a bit of friendly competition (along with some chaotic screaming) to your group!

---

## 🚀 Features

- **Start a Game**: Initiate the loudness challenge with a single command (e.g., `/start`). This resets any previous scores.
- **Voice Message Analysis**: Users simply send a Telegram voice message in the group, and the bot automatically measures its loudness.
- **Live Scoreboard**: After each submission, the bot updates the group with the current standings.
- **End the Game**: Conclude a round with `/end` and see final results, including who placed first.
- **Replay Anytime**: Start new rounds on demand—perfect for party games or quick team-building activities.

---

## ⚙️ Tech Stack

- **Language**: [Python](https://www.python.org/)  
- **Framework**: [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)  
- **Audio Processing**: [pydub](https://github.com/jiaaro/pydub) & `ffmpeg` for reading voice files and measuring loudness  
- **Data Storage**: In-memory dictionary or JSON file for tracking user scores (depending on your needs)

---

## 🔑 Disabling Privacy Mode for Group Chats
To ensure LoudestWins works seamlessly in your group, the bot needs to process voice messages sent by users. 
This requires disabling Privacy Mode, which is enabled by default for Telegram bots.

> Disabling Privacy Mode means the bot can see all messages in the group. Make sure this aligns with your group’s privacy preferences.

Here’s how you can disable Privacy Mode:
1. Open a chat with BotFather (Telegram’s bot management tool).
2. Send the command /setprivacy.
3. Select your bot from the list.
4. Choose `Disable` to turn off Privacy Mode.

**Enjoy playing LoudestWins with your friends!**
