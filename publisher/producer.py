import os
import json
import asyncio
import logging
from aiokafka import AIOKafkaProducer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

KAFKA_BROKER_URL = os.getenv("KAFKA_BROKER_URL", "localhost:9092")

producer = None

async def start_producer():
    global producer
    producer = AIOKafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    await producer.start()
    logger.info("Kafka producer started")

async def stop_producer():
    if producer:
        await producer.stop()
        logger.info("Kafka producer stopped")

async def send_message(topic: str, message: dict):
    if producer is None:
        raise RuntimeError("Producer not initialized")
    await producer.send_and_wait(topic, message)
    logger.info(f"Sent message to {topic}: {str(message)[:30]}...")
