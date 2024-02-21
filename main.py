from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from chatbot import routers as chatbot_router
import uvicorn



app = FastAPI()

origins = [
    "http://localhost:3000",  # Assuming your React app runs on localhost:3000
]
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of origins that are allowed to make requests
    allow_credentials=True,  # Whether to support cookies in the requests
    # Which methods to allow, ["GET", "POST"] or ["*"] for all
    allow_methods=["*"],
    # Which headers to allow, can be specific or ["*"] for all
    allow_headers=["*"],
)



app.include_router(chatbot_router.router)
    

@app.get("/test")
def test():
    return "hello"

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
