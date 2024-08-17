#!/bin/bash

start_fastapi() {
  cd backend
  uvicorn app:app --host 0.0.0.0 --port 8000 --reload
}

start_react() {
  cd webshield-website
  npm start
}


start_fastapi &
start_react &
