# engine.py

def saf_dil_kontrol(metin):
    metin = metin.lower()
    
    # 60 centlik samimi uyarılar
    if "going to" in metin:
        return "Hey! You used 'going to'. Too formal! You're gonna sound better if you say 'gonna'."
    
    if "want to" in metin:
        return "Brother, 'want to' is for textbooks. You wanna speak like a local? Say 'wanna'!"
    
    if "have to" in metin:
        return "Listen, 'have to' is okay but you gotta use 'gotta' for that sharp accent."

    # Başarı durumu
    success_keywords = ["gonna", "wanna", "gotta"]
    if any(word in metin for word in success_keywords):
        return "Excellent! You sound like a real lion. Keep that energy!"

    return f"I heard you: '{metin}'. It's okay, but let's make it more natural."
