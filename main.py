from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def welcome():
    return {"message": "Welcome to Jina Template API"}
# endpoint
@app.post("/tps")
def tps():
    return {"message": "TPS"}

@app.get("/tps")
def tps():
    return {"message": "TPS get"}
