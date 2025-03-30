import threading

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


def worker(name):
    while True:
        task = client.brpop("task_queue", timeout=10)
        if task:
            print(f"Воркер {name} обработал: {task[1].decode()}")


# Запускаем 2 рабочих процесса (воркера)
threading.Thread(target=worker, args=("A",), daemon=True).start()
threading.Thread(target=worker, args=("B",), daemon=True).start()

# Добавляем задачи в очередь
add_task("Задача 1")
add_task("Задача 2")
add_task("Задача 3")
