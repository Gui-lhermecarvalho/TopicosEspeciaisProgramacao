import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv(override=True)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What's in this image?"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://www.cbf.com.br/_next/image?url=https%3A%2F%2Fobjectstorage.sa-saopaulo-1.oraclecloud.com%2Fn%2Fgrsa9ybqykir%2Fb%2Fportalcbf%2Fo%2Fagenciacorinthians-foto-203885-scaled-aspect-ratio-512-320.webp&w=1920&q=75"
                    }
                }
            ]
        }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

print(completion.choices[0].message)
