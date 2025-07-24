from groq import Groq
from groq.types.chat import ChatCompletionUserMessageParam
import os
from dotenv import load_dotenv

load_dotenv()

# Directly fetch the key
api_key = os.getenv("GROQ_API_KEY")
if api_key is None:
    raise ValueError("GROQ_API_KEY not found in environment variables")

client = Groq(api_key=api_key)

def get_completion(prompt: str):
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            ChatCompletionUserMessageParam(
                role="user",
                content=prompt
            )
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    prompt = "What are the basic requirements for making a pasta?"
    response = get_completion(prompt)
    print(response)