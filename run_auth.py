#Now, manually visit this URL in your browser (replace CLIENT_ID):

'''
https://www.strava.com/oauth/authorize
?client_id=200723
&response_type=code
&redirect_uri=http://localhost
&approval_prompt=force
&scope=read,activity:read_all
'''

from auth import get_token
import webbrowser
import os
from dotenv import load_dotenv

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

#token_data = get_token("2c33c95ed3be4c738d872ca36ba205fa62439294")
#print(token_data)