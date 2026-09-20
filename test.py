from utils.audio_processor import process_input
from core.transcriber import transcribe_all

source= "https://youtu.be/vKPGZHoHX8k?si=j6TpgGhVtd3puA2c"

chunks= process_input(source)
print(transcribe_all(chunks))