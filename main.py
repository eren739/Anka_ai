from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Senin oluşturduğun mızrak parçalarını içeri alıyoruz
import engine
import learn
import economy

app = FastAPI(title="Sapiens AI Core")

# Sitemizin (Frontend) bu koda erişebilmesi için güvenlik kapısını açıyoruz
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Global olacağımız için her yere açık
    allow_methods=["*"],
    allow_headers=["*"],
)

# JavaScript'ten gelecek veri kalıbı
class UserSpeech(BaseModel):
    text: str
    user_id: str = "lion_1" # Şimdilik sabit, ileride dinamik olacak

@app.get("/")
async def status():
    return {"message": "Mızrak keskin, sistem ayakta!", "version": "0.1"}

@app.get("/daily-task")
async def get_task():
    # learn.py içindeki günlük görevi çekip siteye yolluyoruz
    return learn.gunluk_gorev_getir()

@app.post("/analyze")
async def analyze(data: UserSpeech):
    # 1. Önce economy.py'dan kullanıcının hakkı var mı bakalım
    acc = economy.bakiye_kontrol(data.user_id)
    if acc["days_left"] <= 0:
        return {"reply": "Mızrağının süresi dolmuş aslanım, 60 cente tazelemeye ne dersin?"}

    # 2. engine.py ile sesi analiz edip 'saf dil' geri bildirimi veriyoruz
    feedback = engine.saf_dil_kontrol(data.text)
    
    return {"reply": feedback, "days_left": acc["days_left"]}

if __name__ == "__main__":
    import uvicorn
    # Terminale yazmak yerine direkt dosyayı çalıştırarak başlatabilirsin
    uvicorn.run(app, host="127.0.0.1", port=8000)
