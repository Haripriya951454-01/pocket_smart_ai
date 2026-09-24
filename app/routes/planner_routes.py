from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import markdown

from ..services.recommendation_engine import (
    home_recommendation,
    party_recommendation,
    jewelry_recommendation
)

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.post("/generate-home", response_class=HTMLResponse)
def generate_home(
    request: Request,
    budget: float = Form(...),
    room: str = Form(...),
    style: str = Form("")
):
    result = home_recommendation(
        budget,
        room,
        style
    )

    result["recommendation"] = markdown.markdown(
        result["recommendation"],
        extensions=["tables"]
    )

    return templates.TemplateResponse(
        request,
        "result.html",
        {
            "result": result,
            "title": "Home Recommendation"
        }
    )


@router.post("/generate-party", response_class=HTMLResponse)
def generate_party(
    request: Request,
    budget: float = Form(...),
    guests: int = Form(...),
    event_type: str = Form(...)
):
    result = party_recommendation(
        budget,
        guests,
        event_type
    )

    result["recommendation"] = markdown.markdown(
        result["recommendation"],
        extensions=["tables"]
    )

    return templates.TemplateResponse(
        request,
        "result.html",
        {
            "result": result,
            "title": "Party Recommendation"
        }
    )


@router.post("/generate-jewelry", response_class=HTMLResponse)
def generate_jewelry(
    request: Request,
    budget: float = Form(...),
    occasion: str = Form(...)
):
    result = jewelry_recommendation(
        budget,
        occasion
    )

    result["recommendation"] = markdown.markdown(
        result["recommendation"],
        extensions=["tables"]
    )

    return templates.TemplateResponse(
        request,
        "result.html",
        {
            "result": result,
            "title": "Jewelry Recommendation"
        }
    )