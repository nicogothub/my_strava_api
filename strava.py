import requests

BASE_URL = "https://www.strava.com/api/v3"

def get_activities(access_token, per_page=30):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(
        f"{BASE_URL}/athlete/activities",
        headers=headers,
        params={"per_page": per_page}
    )
    return response.json()