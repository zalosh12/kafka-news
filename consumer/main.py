from fastapi import FastAPI
from aiokafka import AIOKafkaConsumer
from datetime import datetime
import asyncio
import logging
import json
from db import insert_message,get_messages
from config import KAFKA_BROKER_URL,KAFKA_TOPIC,KAFKA_GROUP_ID



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()


async def consume():
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER_URL,
        group_id=KAFKA_GROUP_ID,
        value_deserializer=lambda v : json.loads(v.decode('utf-8'))
    )
    await consumer.start()
    try:
        async for msg in consumer:
            data = msg.value
            data['timestamp'] = datetime.now().isoformat()
            await insert_message(data)
            logger.info(f"Saved to 'interesting' collection: {data['content'][:30]}...")
    except Exception as e :
        logger.error(f"Consumer error: {e}")
    finally:
        await consumer.stop()


@app.on_event("startup")
async def startup_event():
    await asyncio.sleep(30)
    asyncio.create_task(consume())


@app.get("/messages")
async def read_messages():
    return await get_messages()
