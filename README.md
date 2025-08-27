# Kafka Newsgroup Classifier

This project demonstrates a complete event-driven microservices architecture. The system fetches data from the "20 Newsgroups" dataset, publishes it to different Kafka topics, processes it using separate consumer services, and stores the results in a MongoDB database. The entire system is managed and orchestrated using Docker and Docker Compose.

## Stack

- Python 3.11
- FastAPI
- aiokafka (for asynchronous Kafka communication)
- scikit-learn (for fetching the dataset)
- MongoDB (with the `motor` async driver)
- Docker & Docker Compose

## How to Use

### Using Docker Compose
You will need Docker and Docker Compose installed to follow the next steps. To build the images and run all the services, use the following command from the project's root directory:

```bash
docker-compose up --build
```
# python-kafka-docker
The main objective in this project was to learn how to create an application that sends and receives a message from Kafka, using Docker and docker-compose tools.


The configuration will create a cluster with 5 containers:

- publisher: A FastAPI application that fetches data and sends it to Kafka. It will be accessible at http://localhost:8015.
- sub_interesting: An instance of the generic Consumer service, listening to the interesting topic and saving data to MongoDB. Accessible at http://localhost:8016.
- sub_not_interesting: Another instance of the Consumer service, listening to the not_interesting topic. Accessible at http://localhost:8017.
- kafka: A Kafka broker running in KRaft mode (without Zookeeper).
- zookeeper: Manages the Kafka cluster state.
- mongo: A MongoDB NoSQL database instance.

### API

- Publish Messages (Publisher)
```
GET http://localhost:8015/publish
```

## Swagger
Automatic interactive API documentation for each service is available at the /docs endpoint:
- Publisher: http://localhost:8015/docs
- Consumer (Interesting): http://localhost:8016/docs
- Consumer (Not Interesting): http://localhost:8017/docs
## Project Structure
The project is structured into two main microservices, publisher and a generic consumer.

```
cmd
.
├── consumer/
│   ├── Dockerfile
│   ├── __init__.py
│   ├── config.py
│   ├── db.py
│   ├── main.py
│   └── requirements.txt
├── publisher/
│   ├── Dockerfile
│   ├── __init__.py
│   ├── data.py
│   ├── main.py
│   ├── producer.py
│   ├── publish.py
│   └── requirements.txt
├── .gitignore
└── docker-compose.yml
```

## Environment Variables
The services are configured via environment variables. These are set in the docker-compose.yml file. For local development outside of Docker, you can create an .env file in each service's root folder.
- Publisher:
```
#Kafka broker address (set automatically by docker-compose)
KAFKA_BROKER_URL=kafka:9092
  ```

-Consumer:
The Consumer service is generic. The docker-compose.yml file runs two instances of the same image, each with a different configuration.
```
# Required variables that must be set for each instance
KAFKA_TOPIC=
KAFKA_GROUP_ID=
COLLECTION_NAME=

# Variables with sensible defaults (set/overridden by docker-compose)
KAFKA_BROKER_URL=kafka:9092
MONGO_URI=mongodb://root:example@mongo:27017/
DB_NAME=newsgroups_db
```

## Help and Resources
You can read more about the tools used in this project in their official documentation:

- aiokafka
- Docker
- FastAPI
- Kafka
- MongoDB
- Motor (MongoDB Async Driver)
- scikit-learn