"use client";

import { useEffect, useState } from "react";

export default function Wether() {
  const [weather, setWether] = useState<any>(null);

  useEffect(() => {
    const fetchWether = async () => {
      const res = await fetch("http://localhost:8000/weather?city=Tokyo");
      const data = res.json();
      setWether(data);
    };
    fetchWether();
  }, []);
  return (
    <div className="p-6">
      <h1 className="text-xl font-bold">🌤️ 天気情報（東京</h1>
      {weather ? (
        <div className="mt-4">
          <p>天気: {weather.weather[0].description}</p>
          <p>気温: {weather.main.temp}°C</p>
          <p>湿度: {weather.main.humidity}%</p>
        </div>
      ) : (
        <p>読み込み中...</p>
      )}
    </div>
  );
}
