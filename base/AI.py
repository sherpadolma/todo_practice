from dotenv import load_dotenv
import os
from groq import Groq

# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise Exception("GROQ_API_KEY not found. Check your .env file!")

client = Groq(api_key=api_key)

def create_description_with_ai(todo_title):
    completion = client.chat.completions.create(
        model="llama3-8b-8192",  
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that generates todo descriptions in JSON format."
            },
            {
                "role": "user",
                "content": f"Write a brief JSON description for a todo titled: {todo_title}"
            }
        ],
        temperature=1,
        max_tokens=300,
        top_p=1,
        stream=False,
        response_format={"type": "json_object"}
    )
    return completion.choices[0].message.content
