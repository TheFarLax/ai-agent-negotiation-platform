import re
import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
    timeout=60.0
)

def buyer_agent(user_request, seller_offer=None):

    prompt = f"""
    You are a buyer AI agent.

    Your goals:
    - minimize price
    - minimize deadline
    - maximize quality

    User request:
    {user_request}

    Seller offer:
    {seller_offer}

    Respond ONLY in valid JSON.

    Example:
    {{
      "message": "I can accept this deal.",
      "price": 150,
      "deadline_hours": 48,
      "accepted": true
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

        print("\nBUYER RESPONSE:\n")
        print(content)

        match = re.search(r"\{.*\}", content, re.DOTALL)

        if match:
            return match.group(0)

        return """
        {
          "message": "Invalid response",
          "price": 0,
          "deadline_hours": 0,
          "accepted": false
        }
        """

    except Exception as e:

        print("BUYER ERROR:", e)

        return """
        {
          "message": "Negotiation failed",
          "price": 0,
          "deadline_hours": 0,
          "accepted": false
        }
        """
