from pydub import AudioSegment
import os

async def processVoice(bot, file_id):
    file = await bot.get_file(file_id)
    file_path = await file.download_to_drive('voice.ogg')
    audio = AudioSegment.from_ogg(file_path)
    loudness = audio.dBFS
    os.remove(file_path)
    return loudness

def convert_dbfs_to_score(dbfs: float) -> str:
    #coverts dbfs reading to a score from 0-9999
    MIN_DBFS = -60.0
    MAX_DBFS = 0.0

    #clamp dBFS to ensure it does not go beyond MIN_DBFS or MAX_DBFS
    clamped = max(MIN_DBFS, min(dbfs, MAX_DBFS))
    
    fraction = (clamped - MIN_DBFS) / (MAX_DBFS - MIN_DBFS)
    raw_score = int(round(fraction * 9999))

    #format with zero-padding to always have 4 digits
    return f"{raw_score:04d}"
