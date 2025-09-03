from dotenv import load_dotenv
import os
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
)

prompt = (
    "Crie a imagem de um Mustang Dark Horse em uma pista de corrida parado angulado de lado"
)

response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[prompt],
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.save("generated_image.png")