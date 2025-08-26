from fastapi import FastAPI
from .producer import start_producer, stop_producer
from .publish import publish_one_message_per_category

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await start_producer()

@app.on_event("shutdown")
async def shutdown_event():
    await stop_producer()

@app.get("/publish")
async def publish():
    await publish_one_message_per_category()
    return {"status": "Messages sent: one per category"}

# import json
# from fastapi import FastAPI
# from kafka import KafkaProducer
# from sklearn.datasets import fetch_20newsgroups
#
# app = FastAPI()
#
# producer = KafkaProducer(
#     bootstrap_servers=['localhost:9092'],
#     value_serializer=lambda v: json.dumps(v).encode('utf-8')
# )
#
# interesting_categories = ['alt.atheism',
#                           'comp.graphics',
#                           'comp.os.ms-windows.misc',
#                           'comp.sys.ibm.pc.hardware',
#                           'comp.sys.mac.hardware',
#                           'comp.windows.x',
#                           'misc.forsale',
#                           'rec.autos',
#                           'rec.motorcycles',
#                           'rec.sport.baseball']
#
#
# not_interesting_categories = ['rec.sport.hockey',
#                               'sci.crypt',
#                               'sci.electronics',
#                               'sci.med', 'sci.space',
#                               'soc.religion.christian',
#                               'talk.politics.guns',
#                               'talk.politics.mideast',
#                               'talk.politics.misc',
#                               'talk.religion.misc']
#
# newsgroups_interesting = fetch_20newsgroups(subset='all', categories=interesting_categories, remove=('headers', 'footers', 'quotes'))
# newsgroups_not_interesting = fetch_20newsgroups(subset='all', categories=not_interesting_categories, remove=('headers', 'footers', 'quotes'))
#
#
# app.state.interesting_idx = 0
# app.state.not_interesting_idx = 0
#
# @app.get("/publish")
# def publish_messages():
#     i_idx = app.state.interesting_idx
#     ni_idx = app.state.not_interesting_idx
#
#     for i in range(10):
#         idx = (i_idx + i) % len(newsgroups_interesting.data)
#         message = {'content': newsgroups_interesting.data[idx]}
#         producer.send('interesting', value=message)
#         print(f"Sent to 'interesting': {message['content'][:30]}...")
#
#     app.state.interesting_idx = (i_idx + 10) % len(newsgroups_interesting.data)
#
#
#     for i in range(10):
#         idx = (ni_idx + i) % len(newsgroups_not_interesting.data)
#         message = {'content': newsgroups_not_interesting.data[idx]}
#         producer.send('not_interesting', value=message)
#         print(f"Sent to 'not_interesting': {message['content'][:30]}...")
#
#     app.state.not_interesting_idx = (ni_idx + 10) % len(newsgroups_not_interesting.data)
#
#     producer.flush()
#     return {"status": "20 messages sent successfully"}
#
# if __name__ == "__main__":
#     print("bye")
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

