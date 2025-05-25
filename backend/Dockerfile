# Python 3.11の軽量版を使用
FROM python:3.11-alpine

# コンテナ内の作業ディレクトリを設定
WORKDIR /app

# Pythonの依存関係ファイルをコピー
COPY requirements.txt .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . .

# ポート8000を公開（FastAPIのデフォルト）
EXPOSE 8000

# FastAPIアプリケーションを起動
# uvicorn = FastAPIを動かすためのWebサーバー
# main:app = main.pyファイルのappオブジェクト
# --host 0.0.0.0 = 全てのIPアドレスからアクセス可能
# --port 8000 = 8000番ポートで起動
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]