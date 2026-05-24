from fastapi import FastAPI

from app.schema import TicketRequest, TicketAnalysis
from app.llm import analyze_ticket

app = FastAPI()


@app.post("/analyze-ticket", response_model=TicketAnalysis)
def analyze_ticket_endpoint(ticket: TicketRequest):
    return analyze_ticket(ticket)