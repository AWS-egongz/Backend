from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from controllers.chatbotSetup import rag
from dotenv import load_dotenv
import os
class Chat(BaseModel):
    message: str 

open_ai_key = os.getenv("OPEN_AI_KEY")

app = FastAPI()
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 출처에서 요청을 허용하려면 * 사용 (실제 운영 환경에서는 가능한 출처를 명시하는 것이 좋음)
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # 허용되는 HTTP 메서드
    allow_headers=["*"],  # 모든 헤더를 허용하려면 * 사용 (실제 운영 환경에서는 필요한 헤더만 허용하는 것이 좋음)
)


@app.post('/chatbot')
async def query(chat:Chat):
    # POST 요청의 JSON 데이터 추출
    print(chat.message)
    response = rag(chat.message)
    # response = "This is from backend"
    # 메시지 처리 로직 구현
    # 여기서는 간단히 받은 메시지를 그대로 반환
    
    return response

