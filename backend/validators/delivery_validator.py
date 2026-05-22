import re
import os
import json

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
    timeout=60.0
)

def evaluate_delivery(task, agreement, delivery):

    prompt = f"""
    You are an AI validator.

    Your job:
    - evaluate delivery quality
    - check if task requirements are satisfied
    - determine if seller deserves payment

    TASK:
    {task}

    AGREEMENT:
    {agreement}

    DELIVERY:
    {delivery}

    Respond ONLY in JSON.

    Example:
    {{
      "approved": true,
      "reason": "Requirements satisfied."
    }}
    """

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = response.choices[0].message.content

        print("\nVALIDATOR RESPONSE:\n")
        print(content)

        match = re.search(r"\{.*\}", content, re.DOTALL)

        if match:
            import json

            return json.loads(match.group(0))

        return {
            "approved": False,
            "reason": "Invalid validator response"
        }

    except Exception as e:

        print("VALIDATOR ERROR:", e)

        return {
            "approved": False,
            "reason": str(e)
        }
