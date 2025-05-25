from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware

# FastAPIアプリケーションを作成
app = FastAPI(
    title="釣り場情報共有API",
    description="全国の釣り場情報を共有するためのAPI",
    version="1.0.0",
)

# CORS設定（Cross-Origin Resource Sharing）
# フロントエンド（localhost:3000）からバックエンド（localhost:8000）への
# アクセスを許可するために必要
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # フロントエンドのURL
    allow_credentials=True,
    allow_methods=["*"],  # 全てのHTTPメソッドを許可
    allow_headers=["*"],  # 全てのヘッダーを許可
)

API_KEY = "YOUR_API_KEY"  # 環境変数で管理推奨


@app.get("/weather")
async def get_weather(city: str = "Tokyo"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ja"
    response = requests.get(url)
    data = response.json()
    return data
