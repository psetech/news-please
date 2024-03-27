import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.get("/")
async def create_news_article(url: str):
  from newsplease import NewsPlease

  headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Content-type': 'application/json',
  }

  result = requests.get(url, headers)

  status = "SUCCESS" if result.status_code == 200 else "FAILED"

  data = {
    "status": status,
    "newsArticle": NewsPlease.from_html(result.content.decode(), url=url)
  }

  return data
