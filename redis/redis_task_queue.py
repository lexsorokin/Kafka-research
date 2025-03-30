import redis

# Подключение к Redis
client = redis.StrictRedis(host="localhost", port=6379, db=0)


# Функция для постановки задачи в очередь
def add_task(task_data):
    client.rpush("task_queue", task_data)  # Добавляем задачу в конец очереди
    print(f"Задача добавлена: {task_data}")


# Функция для обработки задач
def process_task():
    task = client.lpop("task_queue")  # Забираем первую задачу
    if task:
        task = task.decode()
        print(f"Обрабатываем задачу: {task}")
    else:
        print("Очередь пуста")


# Добавляем задачи
add_task("Отправить email")
add_task("Сгенерировать отчет")
add_task("Обновить кэш")

# Обрабатываем задачи
process_task()
process_task()
process_task()


def worker():
    while True:
        task = client.brpop("task_queue", timeout=10)  # Ожидаем задачу 10 секунд
        if task:
            print(f"Обрабатываем задачу: {task[1].decode()}")
        else:
            print("Нет задач, ждем...")


worker()
