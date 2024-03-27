from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.routes import router as NoteRouter

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

@app.get("/", tags=["Root"])
async def read_root():
  return { 
    "message": "Welcome to my notes application, use the /docs route to proceed"
   }

app.include_router(NoteRouter, prefix="/news-article")