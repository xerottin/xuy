import os
from fastapi import FastAPI

app = FastAPI()

# Получаем порт из переменной окружения (Railways требует этого)
port = os.getenv("PORT", 8000) 