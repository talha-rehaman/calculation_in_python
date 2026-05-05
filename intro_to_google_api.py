import os
import requests
import base64
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

# Image download karo
image_url = "https://i.pinimg.com/236x/c1/da/a8/c1daa8536b364a4b4d62af369ce606cc.jpg"
response_img = requests.get(image_url)
image_data = base64.b64encode(response_img.content).decode("utf-8")

# Image Analyze karo
response = client.models.generate_content(
    model="gemini-2.0-flash",  # ✅ Aapke paas available hai
    contents=[
        {
            "role": "user",
            "parts": [
                {
                    "inline_data": {
                        "mime_type": "image/jpeg",
                        "data": image_data
                    }
                },
                {
                    "text": "Describe this image in detail."
                }
            ]
        }
    ]
)

print(response.text)
