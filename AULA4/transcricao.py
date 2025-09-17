import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv(override=True)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

AUDIO = "historia.mp3"            # o áudio está na mesma pasta do script
OUT   = "transcricao.txt"

# opcional: validar existência do arquivo
if not os.path.exists(AUDIO):
    raise FileNotFoundError(f"Não encontrei: {os.path.abspath(AUDIO)}")

with open(AUDIO, "rb") as f:
    resp = client.audio.transcriptions.create(
        file=f,
        model="whisper-large-v3-turbo",
        language="pt",
        response_format="text"  # retorna texto puro
    )

texto = resp if isinstance(resp, str) else getattr(resp, "text", "")
with open(OUT, "w", encoding="utf-8") as g:
    g.write(texto)

print(f"Transcrição salva em: {os.path.abspath(OUT)}")