from fastapi import FastAPI
import uvicorn

from src.endoints import router

app = FastAPI()
app.include_router(router=router)

@app.get('/')
def home():
    return {'status': 'OK'}



if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)