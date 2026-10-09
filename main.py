from fastapi import FastAPI
 
app = FastAPI(title="Hello API")
 
@app.get("/")
def home():
    return {
        "message": "Hello from Azure!",
        "status": "running"
    }
 
@app.get("/health")
def health():
    return {"status": "healthy"}
