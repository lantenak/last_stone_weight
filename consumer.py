# Import modules
from kafka import KafkaConsumer
import json
import time
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS


# Kafka settings
consumer = KafkaConsumer(
    'last_stone_weight',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    consumer_timeout_ms=1000,
    value_deserializer=lambda m: json.loads(m.decode())
)


# InfluxDB settings
url = 'http://localhost:8086'
token = 'secure'
org = 'lantenak'


# InfluxDB connection
client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)
write_api = client.write_api(write_options=SYNCHRONOUS)


# Process data flow
start_time = time.time()
timeout = 300
for message in consumer:
    # 5 min threshold
    if time.time() - start_time > timeout:
        break
    
    # Get ready for insertion
    res = message.value
    print(res)
    point = influxdb_client.Point('last_stone_weight').field('last_stone_weight', res)

    # Insert data
    write_api.write(bucket='last_stone_weight', org=org, record=point)
consumer.close()
print('All data have been received & inserted')