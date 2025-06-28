from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime, timedelta
from backend.calendar_utils import book_event
import re

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat(message: Message):
    text = message.text.lower()

    # Very basic parsing logic (replace with LangGraph chain later)
    if "tomorrow" in text:
        start_time = datetime.now() + timedelta(days=1, hours=15)  # 3 PM tomorrow
        end_time = start_time + timedelta(minutes=30)
        link = book_event("Meeting", start_time, end_time)
        return {"reply": f"Your meeting has been booked: {link}"}

    elif "friday" in text:
        return {"reply": "What time on Friday would you prefer?"}

    elif "between" in text:
        match = re.search(r'between (\d+)[ -]?(\d+)', text)
        if match:
            start_hour = int(match.group(1))
            end_hour = int(match.group(2))
            start_time = datetime.now() + timedelta(days=7)
            start_time = start_time.replace(hour=start_hour, minute=0)
            end_time = start_time.replace(hour=end_hour)
            link = book_event("Meeting", start_time, end_time)
            return {"reply": f"Meeting booked: {link}"}

    return {"reply": "Can you please specify a date and time?"}
