# Built in imports
import base64

# Installed imports
import requests
from fastapi import FastAPI

# Local imports
import config

app = FastAPI()

@app.get("/")
async def root():
    """ Root with no purpose """
    return {"message": "I'm a teapot"}

@app.get("/access_token")
async def get_access_token():
    """ Returns access token from Spotify using Client Credentials """
    url = "https://accounts.spotify.com/api/token"
    body = {"grant_type": "client_credentials"}
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{config.SPOTIFY_CLIENT_ID}:{config.SPOTIFY_CLIENT_SECRET}".encode('utf-8')).decode('utf-8')
    }
    response = requests.post(url, data=body, headers=headers)
    return response.json(), response.status_code