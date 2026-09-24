from fastapi import APIRouter

router = APIRouter()

@router.get("/auth/status")
def auth_status():
    return {
        "success": True,
        "message": "Authentication routes are working."
    }