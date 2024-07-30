from pydantic import BaseModel


class ScrapeDocumentResult(BaseModel):
    text: str
    time_taken: float = 0
