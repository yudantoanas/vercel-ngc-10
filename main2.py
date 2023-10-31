from fastapi import FastAPI, HTTPException, Header

app = FastAPI()

# key yang perlu dimasukkan ke dalam header
key = "hacktiv8mania2023"

# public
@app.get("/") # menentukan alamat/url
def helloFunction(): # function yang memproses alamat/url tertentu
    return {
        "message": "hello world"
    }

# secret -> harus memasukkan authentication
@app.get("/secret") 
def helloFunction(api_key: str = Header(None)):
    # check api_key dari header
    if api_key is None or api_key != key:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    return {
        "message": "secret message"
    }