import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


MODEL = "gemini-3.6-flash"


def ask_gemini(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        print(f"Gemini error: {e}")

        return (
            "Gemini is temporarily unavailable. "
            "Please try again in a moment."
        )

def home_recommendation(
    budget: float,
    room: str,
    style: str
):
    prompt = f"""
You are PocketSmart AI, a budget-aware home recommendation assistant.

User budget: {budget}
Room: {room}
Preferred style: {style or "practical and comfortable"}

Give a practical home recommendation that stays within the user's budget.

Include:
1. Recommended setup
2. Suggested items
3. Approximate budget allocation
4. One money-saving tip

Keep the answer concise and easy to understand.
"""

    recommendation = ask_gemini(prompt)

    return {
        "category": "home",
        "budget": budget,
        "room": room,
        "style": style,
        "recommendation": recommendation
    }


def party_recommendation(
    budget: float,
    guests: int,
    event_type: str
):
    per_guest = budget / guests

    prompt = f"""
You are PocketSmart AI, a budget-aware party planning assistant.

Total budget: {budget}
Number of guests: {guests}
Event type: {event_type}
Approximate budget per guest: {round(per_guest, 2)}

Create a practical party plan within this budget.

Include:
1. Food
2. Decorations
3. Activities
4. Approximate spending allocation
5. One money-saving tip

Keep the answer concise.
"""

    recommendation = ask_gemini(prompt)

    return {
        "category": "party",
        "budget": budget,
        "guests": guests,
        "event_type": event_type,
        "budget_per_guest": round(per_guest, 2),
        "recommendation": recommendation
    }


def jewelry_recommendation(
    budget: float,
    occasion: str
):
    prompt = f"""
You are PocketSmart AI, a budget-aware jewelry recommendation assistant.

Budget: {budget}
Occasion: {occasion}

Suggest suitable jewelry options that stay within the budget.

Include:
1. Suitable jewelry types
2. Style suggestion
3. Budget guidance
4. One money-saving tip

Keep the answer concise.
"""

    recommendation = ask_gemini(prompt)

    return {
        "category": "jewelry",
        "budget": budget,
        "occasion": occasion,
        "recommendation": recommendation
    }