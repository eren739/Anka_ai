from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# 1. ANKA AI Uygulamasını Başlatıyoruz
app = FastAPI(title="ANKA AI Core")

# 2. CORS GÜVENLİK DUVARINI YIKAN KISIM (Kritik!)
# Bu blok olmazsa Spck Editor "Failed to fetch" hatası verir.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Tüm dünyadan gelen isteklere kapıyı aç
    allow_credentials=True,
    allow_methods=["*"], # GET, POST her şeye izin ver
    allow_headers=["*"],
)

# 3. Veri Modeli (Analiz için kullanılacak)
class UserSpeech(BaseModel):
    text: str

# --- ROTALAR (ENDPOINTS) ---

@app.get("/")
async def status():
    return {"status": "online", "message": "ANKA AI küllerinden doğdu, sistem ayakta!"}

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
    # Senin efsane 'gonna/wanna' kuralın
    if "gonna" in text or "wanna" in text:
        return {
            "status": "success", 
            "message": "Harika! 'gonna/wanna' kullandın. +60 cent kazandın!"
        }
    else:
        return {
            "status": "error", 
            "message": "Mızrağın köreldi! 'going to' yerine 'gonna' veya 'wanna' kullanmalısın."
        }

# İleride daha karmaşık analizler yapacağın kısım
@app.post("/analyze")
async def analyze(data: UserSpeech):
    text = data.text.lower()
    if "gonna" in text or "wanna" in text:
        return {"reply": "Mızrağın keskin, tam isabet!", "status": "success"}
    return {"reply": "Mızrağın ucu körelmiş, 'gonna' kullan!", "status": "fail"}
