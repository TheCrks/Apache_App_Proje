import json

from confluent_kafka import Consumer, KafkaError

# Kafka broker configuration
bootstrap_servers = ""
while bootstrap_servers == "":
    bootstrap_servers = input("Enter bootstrap servers (eg. localhost:9092)")

topic = ""
while topic == "":
    topic = input("Enter Topic (eg. my_topic)")

group_id = ""
while group_id == "":
    group_id = input("Enter group id:")


# Create a Kafka consumer
consumer = Consumer({
    'bootstrap.servers': bootstrap_servers,
    'group.id': group_id,
    'auto.offset.reset': 'earliest'  # Start consuming from the beginning of the topic
})

# Subscribe to the Kafka topic
consumer.subscribe([topic])

# Consume messages
while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            # End of partition, continue to the next message
            continue
        else:
            # Handle error
            print('Error:', msg.error())
            break

    # Process the consumed message
    json_message = msg.value().decode('utf-8')
    parsed_message = json.loads(json_message)

    # Print the parsed message
    print(parsed_message)

# Close the consumer
consumer.close()
