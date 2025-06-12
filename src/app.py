import os
from fastapi import FastAPI
from redis import Redis
from logsystem import logevent

app = FastAPI()
redis_db = Redis(host=os.getenv("REDIS_HOST"),
                 port=int(os.getenv("REDIS_PORT", "6379")))
@app.get("/")
def hello():
    redis_db.incr("visitorCount")
    visitor_count = redis_db.get("visitorCount").decode("utf-8")
    logevent(f"Visitor count: {visitor_count}")
    return {"message": f"Hello, World From Current Environment: {os.getenv("ENV", "dev")}, visitors: {visitor_count}"}