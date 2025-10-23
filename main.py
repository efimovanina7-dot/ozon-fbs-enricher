from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from schemas import EnrichRequest, EnrichResponse  # у тебя файлы лежат в корне

app = FastAPI(title="Ozon FBS Enricher", version="0.1.0")

HTML_PAGE = """
<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Ozon FBS Enricher</title>
  <style>
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; margin: 24px; }
    .card { max-width: 720px; padding: 16px; border: 1px solid #eee; border-radius: 12px; }
    label { display:block; margin: 12px 0 4px; font-weight:600; }
    input, select { width:100%; padding:10px; border:1px solid #ccc; border-radius:8px; }
    button { margin-top:16px; padding:10px 16px; border:0; border-radius:8px; cursor:pointer; }
    .primary { background:#111827; color:#fff; }
    pre { background:#fafafa; padding:12px; border-radius:8px; overflow:auto; }
  </style>
</head>
<body>
  <div class="card">
    <h2>Ozon FBS Enricher</h2>
    <p>Введи номер отправления (posting_number) — вернём ровно нужные поля.</p>
    <label>Маркетплейс</label>
    <select id="marketplace">
      <option value="ozon" selected>ozon</option>
    </select>
    <label>ID type</label>
    <input id="id_type" value="posting_number" />
    <label>Значение ID</label>
    <input id="id_value" placeholder="12345-001" />
    <button class="primary" onclick="enrich()">Получить данные</button>
    <div id="out"></div>
  </div>

  <script>
    async function enrich(){
      const body = {
        marketplace: document.getElementById('marketplace').value,
        id_type: document.getElementById('id_type').value,
        id_value: document.getElementById('id_value').value
      };
      const res = await fetch('/enrich/order', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify(body)
      });
      const data = await res.json();
      document.getElementById('out').innerHTML =
        '<h3>Ответ</h3><pre>'+JSON.stringify(data, null, 2)+'</pre>';
    }
  </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def index():
    return HTML_PAGE

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/enrich/order", response_model=EnrichResponse)
def enrich_order(req: EnrichRequest):
    # Заглушка: на следующем шаге подключим реальный вызов Ozon API.
    if req.marketplace.lower() != "ozon" or req.id_type != "posting_number":
        raise HTTPException(status_code=400, detail="MVP: только Ozon + posting_number")
    return EnrichResponse(
        data={"marketplace": req.marketplace, "posting_number": req.id_value},
        meta={"hint": "Дальше подключим реальный Ozon API и вернём нужные поля"}
    )
