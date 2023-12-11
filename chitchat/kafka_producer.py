from confluent_kafka import Producer
import socket
import json
import os
from dotenv import load_dotenv

load_dotenv()


p = Producer({'bootstrap.servers': os.getenv("KAFKA_BOOTSTAP_SERVER_EXTERNAL"),
        'client.id': socket.gethostname()})

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

with open(os.getenv("CHITCHAT_DUMMY_DATAFILE")) as f:
    data = json.load(f)
    for i, item in enumerate(data):
        print(f"processing doc: {i}: {item}")
        # Trigger any available delivery report callbacks from previous produce() calls
        p.poll(0)

        # Asynchronously produce a message. The delivery report callback will
        # be triggered from the call to poll() above, or flush() below, when the
        # message has been successfully delivered or failed permanently.
        p.produce(os.getenv("KAFKA_TOPIC_CHITCHAT"), json.dumps(item), callback=delivery_report)

p.flush()
