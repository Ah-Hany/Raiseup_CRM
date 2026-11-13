import json
from confluent_kafka import Producer

conf = {
    'bootstrap.servers': 'localhost:9092'
}

def send_user_event(username, email, event_type="user_added"):
    producer = Producer(conf)

    event = {
        "event": event_type,
        "username": username,
        "email": email
    }

    producer.produce(
        'crm-users',
        key=str(username),
        value=json.dumps(event)
    )

    remaining = producer.flush(10)

    if remaining:
        raise Exception(f"{remaining} messages were not delivered")

    print(f">>> KAFKA SUCCESS: {event}")