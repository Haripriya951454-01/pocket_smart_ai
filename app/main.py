from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware

from .database import init_db

from .routes.pages import (
    router as pages_router
)

from .routes.auth_routes import (
    router as auth_router
)

from .routes.planner_routes import (
    router as planner_router
)


app = FastAPI(

    title="PocketSmart AI",

    version="1.0.0",

    description=(
        "Budget-aware AI recommendation assistant"
    )

)


app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://127.0.0.1:8000",
        "http://localhost:8000"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


app.mount(

    "/static",

    StaticFiles(
        directory="static"
    ),

    name="static"

)


app.include_router(
    pages_router
)

app.include_router(
    auth_router
)

app.include_router(
    planner_router
)


@app.on_event("startup")
def startup():

    init_db()


@app.get("/startup")
def startup_status():

    return {

        "status":
            "ready",

        "service":
            "PocketSmart AI"

    }


@app.get("/session-info")
def session_info():

    return {

        "message":
            "Use the authenticated dashboard for session details."

    }


@app.get("/session-data")
def session_data():

    return {

        "message":
            "Session data is stored through authenticated recommendation history."

    }


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(

        "app.main:app",

        host="127.0.0.1",

        port=8000,

        reload=True

    )