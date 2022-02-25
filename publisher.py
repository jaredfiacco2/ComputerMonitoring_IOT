import os
from google.cloud import pubsub_v1
from util import getSystemInfo
import time

credentials_path = 'gcp-service-account-auth-key.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

publisher = pubsub_v1.PublisherClient()
topic_path = 'projects/project-name/topics/topic-name'

data = "Computer-Stats-Data"
data = data.encode('utf-8')
while True:
    attributes = getSystemInfo()
    future = publisher.publish(topic_path, data, **attributes)
    print(f'published message id {future.result()}')
    time.sleep(5*60)