from fastapi import FastAPI
from datetime import datetime

# create app instance
app = FastAPI()

# create the main endpoint
@app.get("/home")
def home():
    return {"message": "Welcome to my home"}

@app.get("/time")
def get_time():
    current_time = datetime.now()
    time_message = f'The current time is {current_time}'
    return {"message": "time is " + time_message}

