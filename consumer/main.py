from fastapi import FastAPI
from aiokafka import AIOKafkaConsumer
from datetime import datetime
import asyncio
import logging
import json
from consumer.db import insert_message,get_messages
from consumer.config import KAFKA_BROKER_URL,KAFKA_TOPIC,KAFKA_GROUP_ID



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
    asyncio.create_task(consume())


@app.get("/messages")
async def read_messages():
    return await get_messages()
    # return await collection.find({}, {"_id": 0}).to_list(length=100)





# import json
# import threading
# from datetime import datetime
# from fastapi import FastAPI
# from kafka import KafkaConsumer
# from pymongo import MongoClient
#
# app = FastAPI()
#
#
# client = MongoClient('mongodb://localhost:27017/')
# db = client['newsgroups_db']
# collection = db['interesting']
#
#
# def consume_messages() :
#     consumer = KafkaConsumer(
#         'interesting',
#         bootstrap_servers=['localhost:9092'],
#         auto_offset_reset='earliest',  # להתחיל מההודעה הכי ישנה אם הצרכן חדש
#         group_id='interesting-group',  # מזהה קבוצת צרכנים
#         value_deserializer=lambda v : json.loads(v.decode('utf-8'))  # להפוך חזרה מ-bytes ל-JSON
#     )
#
#     for message in consumer :
#         data = message.value
#         data['timestamp'] = datetime.now().isoformat()
#
#         collection.insert_one(data)
#         print(f"Saved to 'interesting' collection: {data['content'][:30]}...")
#
#
#
# @app.on_event("startup")
# async def startup_event() :
#     threading.Thread(target=consume_messages, daemon=True).start()
#
#
#
# @app.get("/messages")
# def get_messages() :
#     messages = list(collection.find({}, {'_id' : 0}))  # להחזיר הכל, בלי שדה ה-id של מונגו
#     return messages


# from fastapi import FastAPI
# from pymongo.errors import PyMongoError
# from aiokafka import AIOKafkaConsumer
# from pymongo.errors import PyMongoError
# from pymongo import MongoClient
# from datetime import datetime
# from motor.motor_asyncio import AsyncIOMotorClient
# import asyncio
# import logging
# import random
# import json
#
#
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
#
# app = FastAPI()
#
# client = AsyncIOMotorClient('mongodb://localhost:27017/')
# db = client['newsgroups_db']
# collection = db['interesting']
#
# KAFKA_BROKER_URL = "localhost:9092"
# TOPIC_NAME = "interesting"
#
# async def consume():
#     consumer = AIOKafkaConsumer(
#         TOPIC_NAME,
#         bootstrap_servers=KAFKA_BROKER_URL,
#         group_id='interesting-group',
#         value_deserializer=lambda v : json.loads(v.decode('utf-8'))
#     )
#     await consumer.start()
#     try:
#         async for msg in consumer:
#             data = msg.value
#             data['timestamp'] = datetime.now().isoformat()
#             await collection.insert_one(data)
#             logger.info(f"Saved to 'interesting' collection: {data['content'][:30]}...")
#     except Exception as e :
#         logger.error(f"Consumer error: {e}")
#     finally:
#         await consumer.stop()
#
#
# @app.on_event("startup")
# async def startup_event():
#     asyncio.create_task(consume())
#
#
# @app.get("/messages")
# async def get_messages():
#     return await collection.find({}, {"_id": 0}).to_list(length=100) הסבר לי כל שורה בקוד