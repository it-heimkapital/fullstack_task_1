#!/usr/bin/env bash

# This is not recommended for production. Running it here to insert intial department data
python3 -m utils.create_department
uvicorn app.api:app --host '0.0.0.0' --port 8005
