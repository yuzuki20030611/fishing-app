# Node.js 18を使用
FROM node:18-alpine

# 作業ディレクトリを設定
WORKDIR /app

# package.jsonをコピーして依存関係をインストール
COPY package*.json ./
RUN npm install

# アプリケーションコードをコピー
COPY . .

# Next.jsアプリをビルド
RUN npm run build

# ポート3000を公開
EXPOSE 3000

# アプリを起動
CMD ["npm", "start"]