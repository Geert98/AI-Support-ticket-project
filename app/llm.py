from app.schema import TicketRequest, TicketAnalysis

def analyze_ticket(ticket: TicketRequest) -> TicketAnalysis:
    return TicketAnalysis(
        category="Authentication",
        priority="Medium",
        summary="User cannot log in",
        suggested_reply="Thanks for reaching out. We will investigate your login issue",  
        )