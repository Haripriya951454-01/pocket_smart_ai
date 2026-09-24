from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>PocketSmart AI</title>
    </head>
    <body>
        <h1>Welcome to PocketSmart AI</h1>
        <p>Your smart budget and recommendation assistant.</p>

        <h2>Home Interior Planner</h2>

        <form action="/generate-home" method="post">

            <label>Budget:</label>
            <input type="number" name="budget" required>

            <br><br>

            <label>Room:</label>
            <select name="room">
                <option value="Living Room">Living Room</option>
                <option value="Bedroom">Bedroom</option>
                <option value="Kitchen">Kitchen</option>
            </select>

            <br><br>

            <label>Style:</label>
            <input
                type="text"
                name="style"
                placeholder="Modern"
            >

            <br><br>

            <button type="submit">
                Generate Recommendations
            </button>

        </form>
    </body>
    </html>
    """


@router.get("/health")
def health():
    return {
        "status": "ok"