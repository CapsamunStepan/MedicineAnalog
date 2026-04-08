# MedicineAnalog (MVP)

Веб‑приложение на Django для поиска лекарств, сравнения цен по аптекам и поиска **аналогов по действующему веществу**.

## Быстрый старт

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Открыть `http://127.0.0.1:8000/`.

## Загрузка данных (из JSON)

Примеры (как раньше), но теперь можно заполнить `active_ingredient`:

```bash
python manage.py load2db --path meds_scraper\\farmacie_md.json --pharmacy FarmacieMD --extract-active
python manage.py load2db --path meds_scraper\\farmacia_familiei.json --pharmacy FarmaciaFamiliei --manufacturer True --extract-active
python manage.py load2db --path meds_scraper\\hippocrates.json --pharmacy Hippocrates --manufacturer True --extract-active
```

## Обновление данных одной командой

Запустить Scrapy + перезалить БД:

```bash
python manage.py refresh_data --extract-active
```

Если Scrapy не нужен (уже есть JSON), можно:

```bash
python manage.py refresh_data --skip-scrapy --extract-active
```

## Active ingredient: OpenAI (опционально)

По умолчанию используется офлайн‑fallback. Чтобы использовать OpenAI, задайте переменную окружения:

- `OPENAI_API_KEY`
- (опционально) `OPENAI_MODEL` (по умолчанию `gpt-4o-mini`)

PowerShell пример:

```powershell
$env:OPENAI_API_KEY="..."
python manage.py fill_active_ingredients --overwrite --limit 50
```

