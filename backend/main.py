from fastapi import FastAPI
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


@app.get("/")
async def root():
    return {"message": "釣り場情報共有API が正常に動作しています！"}


# 釣り場一覧取得のエンドポイント（仮データ）
@app.get("/fishing-spots")
async def get_fishing_spots():
    # 仮のデータ（後でデータベースから取得）
    return [
        {
            "id": 1,
            "name": "東京湾",
            "location": "東京都",
            "fish_types": ["アジ", "サバ", "イワシ"],
            "difficulty": "初心者",
            "description": "初心者でも楽しめる人気の釣り場",
        },
        {
            "id": 2,
            "name": "江ノ島",
            "location": "神奈川県",
            "fish_types": ["メジナ", "ウミタナゴ", "カサゴ"],
            "difficulty": "中級者",
            "description": "景色も楽しめる定番スポット",
        },
    ]


# 特定の釣り場の詳細情報取得
@app.get("/fishing-spots/{spot_id}")
async def get_fishing_spot(spot_id: int):
    # 実際はデータベースから取得するが、今は仮データ
    return {
        "id": spot_id,
        "name": "東京湾",
        "location": "東京都",
        "fish_types": ["アジ", "サバ", "イワシ"],
        "difficulty": "初心者",
        "description": "初心者でも楽しめる人気の釣り場",
        "access": "電車：JR品川駅から徒歩15分",
        "facilities": ["トイレ", "駐車場", "コンビニ"],
        "best_season": "春〜秋",
    }
