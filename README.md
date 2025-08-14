# STOCK PICKER

## Run locally

- Install dependencies (poetry or pip):

```bash
poetry install
poetry run dev
# or
poetry run uvicorn stock_picker.app.main:app --reload
```

or with pip

```bash
pip install -e .
uvicorn stock_picker.app.main:app --reload
```

Open http://127.0.0.1:8000 and http://127.0.0.1:8000/docs

## Structure

```
src/stock_picker/app
├── api
│   ├── __init__.py
│   ├── router.py             # Compose API routers
│   └── routes
│       └── health.py         # Healthcheck endpoint
├── core
│   ├── config.py             # Pydantic settings
│   └── logging.py            # Logging configuration
├── dependencies              # Shared dependencies (DI)
├── middleware                # Custom middlewares
├── schemas                   # Pydantic models
├── services                  # Business logic / services
├── main.py                   # FastAPI app entry
└── worker.py                 # Background worker entry
```

## Next steps
- Add your domain services under `services/`
- Add Pydantic models under `schemas/`
- Add routes under `api/routes/` and include them in `api/router.py`
- Configure environment via `.env` (see `app/core/config.py`)

