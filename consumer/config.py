import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("DB_NAME", "newsgroups_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "interesting")


KAFKA_BROKER_URL = os.getenv("KAFKA_BROKER_URL", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "interesting")
KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID", "interesting-group")






# MONGO_URI = "mongodb://localhost:27017/"
# DB_NAME = "newsgroups_db"
# COLLECTION_NAME = "interesting"
#
# KAFKA_BROKER_URL = "localhost:9092"
# KAFKA_TOPIC = "interesting"
# KAFKA_GROUP_ID = "interesting-group"
