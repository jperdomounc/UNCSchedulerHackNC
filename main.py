from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import random

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock course and rating data
MOCK_DATA = {
    "CS101": {"times": ["MWF 9AM", "TTh 11AM"], "rating": 4.5},
    "MATH201": {"times": ["MWF 10AM", "TTh 2PM"], "rating": 3.9},
    "PHYS105": {"times": ["MWF 1PM", "TTh 9AM"], "rating": 4.8}
}

class ScheduleRequest(BaseModel):
    courses: List[str]
    start_time: str
    end_time: str

@app.post("/generate")
def generate_schedule(req: ScheduleRequest):
    schedules = []

    for _ in range(3):  
        schedule = []
        for course in req.courses:
            section = random.choice(MOCK_DATA[course]["times"])
            schedule.append({
                "course": course,
                "time": section,
                "rating": MOCK_DATA[course]["rating"]
            })
        # Sort by average rating for fun
        avg_rating = sum(c["rating"] for c in schedule) / len(schedule)
        schedules.append({"schedule": schedule, "average_rating": avg_rating})

    schedules.sort(key=lambda x: -x["average_rating"])
    return {"schedules": schedules}
