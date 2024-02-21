from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import urllib.request
from chatbot.chatbotSetup import rag


app = FastAPI()

router = APIRouter(prefix="/chatbot")

class Chat(BaseModel):
    message: str 


@router.post("")
def query(chat:Chat):
    # POST 요청의 JSON 데이터 추출
    print(chat.message)
    response = rag(chat.message)
    # response = "This is from backend"
    # 메시지 처리 로직 구현
    # 여기서는 간단히 받은 메시지를 그대로 반환
    
    return "This is from backend"



app.include_router(router)