from fastapi import FastAPI, Query
from typing import List, Dict, Any
from pydantic import BaseModel

app = FastAPI()

class WeatherResult(BaseModel):
    source: str
    weather: str
    temperature: str

class WeatherResponse(BaseModel):
    city: str
    date: str
    results: List[WeatherResult]


def get_weather(
    city: str = Query(..., description="城市名称"),
    date: str = Query(..., description="日期，格式如2024-06-01")
):
    # 这里先返回mock数据，后续集成真实API
    mock_results = [
        WeatherResult(source="和风天气", weather="晴", temperature="28°C"),
        WeatherResult(source="百度天气", weather="多云", temperature="27°C"),
        WeatherResult(source="腾讯天气", weather="小雨", temperature="26°C"),
        WeatherResult(source="中国天气", weather="阴", temperature="25°C"),
    ]
    return WeatherResponse(city=city, date=date, results=mock_results)
