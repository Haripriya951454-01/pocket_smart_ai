import markdown
from fastapi import APIRouter, Form

router = APIRouter()


@router.post("/generate-home")
def generate_home(
    budget: float = Form(...),
    room: str = Form(...),
    style: str = Form("")
):
    return {
        "success": True,
        "message": "Home recommendation request received.",
        "budget": budget,
        "room": room,
        "style": style
    }


@router.post("/generate-party")
def generate_party(
    budget: float = Form(...),
    guests: int = Form(...),
    event_type: str = Form(...)
):
    return {
        "success": True,
        "message": "Party recommendation request received.",
        "budget": budget,
        "guests": guests,
        "event_type": event_type
    }


@router.post("/generate-jewelry")
def generate_jewelry(
    budget: float = Form(...),
    occasion: str = Form(...)
):
    return {
        "success": True,
        "message": "Jewelry recommendation request received.",
        "budget": budget,
        "occasion": occasion
    }