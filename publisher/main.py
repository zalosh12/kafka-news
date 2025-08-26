from fastapi import FastAPI
from producer import start_producer, stop_producer
from publish import publish_one_message_per_category
import asyncio


#create a fastapi application
app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await asyncio.sleep(30)
    await start_producer()

@app.on_event("shutdown")
async def shutdown_event():
    await stop_producer()

@app.get("/publish")
async def publish():
    await publish_one_message_per_category()
    return {"status": "Messages sent: one per category"}



