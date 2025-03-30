from confluent_kafka import Consumer, KafkaException

# настройка подключения к Kafka
conf = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "group1",  # Группа потребителя
    "auto.offset.reset": "earliest",  # Читаем сообщения с самого начала
}

consumer = Consumer(conf)


def consume(topic="orders"):
    consumer.subscribe([topic])
    print(f"Consumer 2 ждет сообщения...")

    try:
        while True:
            msg = consumer.poll(timeout=1.0)  # ожидание сообщения
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())

            print(f'Consumer 2 получил: {msg.value().decode("utf-8")}')
    except KeyboardInterrupt:
        print("Остановка Consumer 2...")

    finally:
        consumer.close()


if __name__ == "__main__":
    consume()
