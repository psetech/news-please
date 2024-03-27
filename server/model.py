from typing import Optional
from pydantic import BaseModel

class NoteSchema(BaseModel):
  title: Optional[str]
  content: Optional[str]

  class Config:
    schema_extra = {
    	"status": "SUCCESS",
        "newsArticle": {
            "authors": ["Test"],
            "date_download": "",
            "date_modify": "",
            "date_publish": "",
            "description": "",
            "filename": "",
            "image_url": "",
            "language": "",
            "localpath": "",
            "source_domain": "",
            "maintext": "",
            "title": "",
            "title_page": "",
            "title_rss": "",
            "url": "",
        }
    }
