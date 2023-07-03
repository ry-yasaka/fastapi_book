#!/bin/bash

# DB migration を実行
poetry run python -m api.migrate_cloud_db

# uvicorn のサーバーを立ち上げる
poetry run uvicorn api.main:app --host 0.0.0.0