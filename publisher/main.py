from fastapi import FastAPI
from producer import start_producer, stop_producer
from publish import publish_one_message_per_category
from contextlib import asynccontextmanager
import asyncio
import logging


logger = logging.getLogger("uvicorn.error")

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager to handle startup and shutdown tasks.
    """
    await asyncio.sleep(30)
    await start_producer()
    logger.info("producer initialized")
    # Yield control to the application
    yield
    await stop_producer()
    logger.info("producer closed")

app = FastAPI(title="Kafka News Publisher",lifespan=lifespan)


@app.get("/publish")
async def publish():
    await publish_one_message_per_category()
    return {"status": "Messages sent: one per category"}



