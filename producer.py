# Import modules
import random
import heapq
from kafka import KafkaProducer
import json
import time


# Kafka settings
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda m: json.dumps(m).encode()
)


# Start data flow
start_time = time.time()
timeout = 300
while True:
    # 5 min threshold
    if time.time() - start_time > timeout:
        break
    
    # Generate an array
    stones = [random.randint(1, 1000) for _ in range(random.randint(1, 30))]
    
    # Preproccessing for Max Heap
    stones = [-s for s in stones]
    heapq.heapify(stones)

    # Algoritm
    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        if second > first:
            heapq.heappush(stones, first - second)
    
    # In case of empty array
    stones.append(0)
    # Save the result
    res = abs(stones[0])

    # Send data to Kafka
    producer.send(topic='last_stone_weight', value=res)
print('All data have been sent')