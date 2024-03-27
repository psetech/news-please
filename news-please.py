import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
  "*"
]

methods = ["GET", "POST", "PUT", "DELETE"]

headers = ["Content-Type", "Authorization"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Allow credentials (e.g., Authorization headers, Cookies)
    allow_methods=methods,    # Specify allowed HTTP methods (defaults to ['GET'])
    allow_headers=headers,    # Specify allowed headers (defaults to all headers)
)

@app.get("/news-article/")
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
