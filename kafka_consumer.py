import json
from confluent_kafka import Consumer
import time

conf = {
    'bootstrap.servers': '127.0.0.1:9092',
    'group.id': f'test-group-{time.time()}',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
consumer.subscribe(['crm-users'])

print("Listening for messages...")

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(f"Error: {msg.error()}")
        continue

    try:
        data = json.loads(msg.value().decode('utf-8'))
        event_type = data.get('event', 'unknown')
        username = data.get('username', 'N/A')
        email = data.get('email', 'N/A')

        print(f"🔥 [LOGIN EVENT] User: {username} | Email: {email} (Type: {event_type})", flush=True)
    except:
        print(f"-> RAW MESSAGE: {msg.value().decode('utf-8')}", flush=True)