#!/bin/bash

alembic upgrade head

uvicorn app.main:app --host 10.0.0.51 --port 8000