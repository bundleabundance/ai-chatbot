from openai import OpenAI
from config import Config


client = OpenAI(api_key=Config.OPENAI_API_KEY)
from config import Config


def get_openai_response(prompt):
    response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
    max_tokens=150
    )
    return response.choices[0].message.content.strip()
