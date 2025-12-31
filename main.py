from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Sapiens AI Core")

# GÖRÜNMEZ DUVARI YIKAN KISIM (CORS Ayarı)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# JavaScript'ten gelecek veri kalıbı
class UserSpeech(BaseModel):
    text: str
    user_id: str = "lion_1"

@app.get("/")
async def status():
    return {"message": "Mızrak keskin, sistem ayakta!", "version": "0.1"}

@app.get("/daily-task")
async def get_task():
    return {
        "task": "Bugün bir işe başlayacağını söyle.",
        "target": "I'm gonna start working.",
        "tip": "Unutma, 'going to' dersen mızrağın körelir!",
        "reward": 0.6,
        "currency": "cent"
    }

@app.get("/check-grammar")
async def check_grammar(text: str):
    text = text.lower()
    # Senin meşhur 'gonna/wanna' kuralın
    if "gonna" in text or "wanna" in text:
        return {"status": "success", "message": "Harika! 'gonna/wanna' kullandın. +60 cent kazandın!"}
    else:
        return {"status": "error", "message": "Mızrağın köreldi! 'going to' yerine 'gonna' kullanmalısın."}

@app.post("/analyze")
async def analyze(data: UserSpeech):
    # Şimdilik basit mantık, ileride engine.py'a bağlarız
    text = data.text.lower()
    if "gonna" in text or "wanna" in text:
        return {"reply": "Mızrağın keskin aslanım, tam isabet!", "status": "success"}
    return {"reply": "Mızrağın ucu körelmiş, 'gonna' kullan!", "status": "fail"}
