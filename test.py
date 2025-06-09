from crewai_tools import tool
from datetime import datetime

@tool
def fetch_calendar_events(date: str) -> str:
    """
    Simulates fetching calendar events for the given date.
    Returns a summary of scheduled events.
    """
    if date == datetime.today().strftime('%Y-%m-%d'):
        return "10:00 AM: Team Sync\n1:00 PM: Client Call\n3:30 PM: Internal Review"
    else:
        return "No events scheduled for this date."
