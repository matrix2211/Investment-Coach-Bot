from fastapi import FastAPI, Request
from app.telegram import handle_telegram_update

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/telegram")
async def telegram_webhook(request: Request):
    update = await request.json()
    handle_telegram_update(update)
    return {"ok": True}
