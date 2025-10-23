# Ozon FBS Enricher (MVP)

Цель проекта — по вводимому `posting_number` (Ozon FBS) получать **ровно те поля**, которые нужны для вашей таблицы юнит-экономики, без лишних данных.  
Архитектура максимально простая, чтобы шаг за шагом «натренироваться» работать с API Ozon и потом уже расширять функционал.

---

## Что умеет MVP сейчас

- Запускается локальный веб-сервис на FastAPI.
- Эндпоинт `/health` (проверка, что сервис жив).
- Заглушка `/enrich/order` — вернёмся к ней на следующем шаге (сначала тестируем окружение).

---

## Требования

- Python **3.11+**
- Доступ к кабинету Ozon Seller и **API-ключи** (Client ID и API Key). Создайте в личном кабинете Ozon (Настройки → API).  
  **Важно:** не загружайте реальные ключи в GitHub.

---

## Быстрый старт (локально)

### 1) Клонируйте или разархивируйте шаблон
Если вы скачали zip — распакуйте его в удобную папку и перейдите внутрь проекта.

```bash
cd ozon-fbs-enricher
```

### 2) Создайте виртуальное окружение Python и активируйте его

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3) Установите зависимости
```bash
pip install -r requirements.txt
```

### 4) Подготовьте файл `.env`
Создайте файл `.env` в корне (рядом с README). Проще — скопируйте шаблон:
```bash
cp .env.example .env   # macOS/Linux
# На Windows создайте .env вручную на основе .env.example
```
Затем откройте `.env` и заполните:
```env
OZON_CLIENT_ID=ВАШ_CLIENT_ID
OZON_API_KEY=ВАШ_API_KEY
APP_HOST=127.0.0.1
APP_PORT=8000
LOG_LEVEL=INFO
```

### 5) Запустите приложение
```bash
uvicorn app.main:app --reload
```
Откройте http://127.0.0.1:8000/health — должно вернуть:
```json
{"status":"ok"}
```

---

## Структура проекта

```
app/
  main.py                # FastAPI-приложение (/health, заглушка /enrich/order)
  adapters/
    ozon.py              # клиент Ozon (пока заглушка)
  services/
    enrich.py            # бизнес-логика (заглушка)
  models/
    schemas.py           # Pydantic-схемы
  config/
    fields.yml           # список полей для вытягивания
requirements.txt
.env.example
README.md
.gitignore
```

---

## Дальнейшие шаги
1. Проверяем, что локальный запуск работает.
2. Реализуем вызов Ozon API по `posting_number` и мэппинг **строго** в поля из `config/fields.yml`.
3. Добавим финансы/удержания при необходимости.
4. Экспорт в CSV/JSON одной строкой — чтобы вставить в вашу таблицу.
5. Позже — настроим расписание (cron) через GitHub Actions.

---

## Безопасность
- Никогда не коммитьте `.env` с реальными ключами.
- В логах не выводятся секреты.
