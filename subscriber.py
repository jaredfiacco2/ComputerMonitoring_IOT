import os
from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError

credentials_path = 'gcp-service-account-auth-key.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

timeout = 5.0

subscriber = pubsub_v1.SubscriberClient()
subscriber_path = 'projects/project-name/subscriptions/subscription-name'

def callback(message):
    print(f'Received message: {message}')
    print(f'data: {message.data}')
    message.ack()

streaming_pull_future = subscriber.subscribe(subscriber_path, callback=callback)
print(f'Listening for message on {subscriber_path}')

with subscriber:
    try:
        # streaming_pull_future.result(timeout=timeout)
        streaming_pull_future.result()
    except TimeoutError:
        streaming_pull_future.cancel()
        streaming_pull_future.result()