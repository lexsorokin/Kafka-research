from confluent_kafka import Producer

# настройка подключения к Kafka
conf = {'bootstrap.servers': 'localhost:9092'} # адрес брокера Kafka

# создаем продюсера 
producer = Producer(conf)

# Функция обратного вызова для обработки доставки сообщений
def delivery_report(err, msg): 
    if err: 
        print(f'Ошибка при отправке сообщения: err')
    else: 
        print(f'Сообщение доставлено в {msg.topic()} [{msg.partition()}]')

def send_message(topic='test-topic'):
    for i in range(5): 
        message = f'Сообщение {i}'
        producer.produce(topic, message.encode('utf-8'), callback=delivery_report)
        producer.flush()
    print('Все сообщения отправлены')

if __name__ == "__main__":
    send_message()