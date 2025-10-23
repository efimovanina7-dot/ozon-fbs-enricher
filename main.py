from fastapi import FastAPI, HTTPException
from app.models.schemas import EnrichRequest, EnrichResponse

app = FastAPI(title="Ozon FBS Enricher", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/enrich/order", response_model=EnrichResponse)
def enrich_order(req: EnrichRequest):
    # Заглушка: на следующем шаге подключим реальный вызов Ozon API.
    if req.marketplace.lower() != "ozon" or req.id_type != "posting_number":
        raise HTTPException(status_code=400, detail="Для MVP поддерживаем только Ozon и posting_number")
    return EnrichResponse(
        data={"posting_number": req.id_value},
        meta={"hint": "В следующем шаге здесь появятся реальные поля из Ozon API"}
    )
