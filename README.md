# weather_recommendation_backend
Application for recommending songs based on weather. This backend only sends access token to the client.

(For Linux, slightly different on Windows)

1. Create venv with: `python3 -m venv venv`
2. Activate venv with: `source venv/bin/activate`
3. Install packages with `pip install -r requirements.txt`
4. Copy `config.example.py` to `config.py`
5. Add app info to `config.py`
6. Run program with `uvicorn main:app`
