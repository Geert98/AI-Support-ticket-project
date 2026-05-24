from pydantic import BaseModel

class TicketRequest(BaseModel):
    subject: str
    description: str

class TicketAnalysis(BaseModel):
    category: str
    priority: str
    summary: str
    suggested_reply: str
    