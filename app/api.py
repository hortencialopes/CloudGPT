from fastapi import FastAPI

app = FastAPI()

cloud_providers = [
    {"cloud_id": "AWS"},
    {"cloud_id": "GCP"},
    {"cloud_id": "AZURE"}
]

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/cloud/{cloud_name}")
async def read_item(skip: int = 0, limit: int = 10):
    return cloud_providers[skip : skip + limit]