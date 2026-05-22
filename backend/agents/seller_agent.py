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

def seller_agent(user_request, buyer_offer=None):

    prompt = f"""
    You are a seller AI agent.

    Your goals:
    - maximize price
    - keep realistic deadlines
    - secure agreement

    User request:
    {user_request}

    Buyer offer:
    {buyer_offer}

    Respond ONLY in valid JSON.

    Example:
    {{
      "message": "I can deliver for this amount.",
      "price": 180,
      "deadline_hours": 48,
      "accepted": false
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

        print("\nSELLER RESPONSE:\n")
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

        print("SELLER ERROR:", e)

        return """
        {
          "message": "Negotiation failed",
          "price": 0,
          "deadline_hours": 0,
          "accepted": false
        }
        """
