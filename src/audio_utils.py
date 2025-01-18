from pydub import AudioSegment
import os

async def processVoice(bot, file_id):
    file = await bot.get_file(file_id)
    file_path = await file.download_to_drive('voice.ogg')
    audio = AudioSegment.from_ogg(file_path)
    loudness = audio.dBFS
    os.remove(file_path)
    return loudness