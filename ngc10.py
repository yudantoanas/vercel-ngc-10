from fastapi import FastAPI, HTTPException, Header

app = FastAPI()

# define api key
API_KEY = "secret123"

dict = {
    "New York City": {
        "temperature": 3,
        "weather":"Sunny"
    },
    "Los Angeles": {
        "temperature": 16,
        "weather":"Clear"
    },
    "Chicago": {
        "temperature": 1,
        "weather":"Light Fog"
    },
}

@app.get("/authenticate")
def handlerAuth(api_key: str = Header(None)):
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    return {"message":"authenticated"}

@app.get("/weather/{location}")
def handlerLocation(location, api_key: str = Header(None)):
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    if location not in dict:
        raise HTTPException(status_code=404, detail="Not found")

    return dict[location]