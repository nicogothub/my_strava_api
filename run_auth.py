from dotenv import load_dotenv
import webbrowser
import os

load_dotenv()

CLIENT_ID = os.getenv("STRAVA_CLIENT_ID")

url = (
    "https://www.strava.com/oauth/authorize"
    f"?client_id={CLIENT_ID}"
    "&response_type=code"
    "&redirect_uri=http://localhost"
    "&approval_prompt=force"
    "&scope=read,activity:read_all"
)

webbrowser.open(url)