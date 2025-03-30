import redis  # Импортируем библиотеку для работы с Redis

# Создаем подключение к Redis
client = redis.StrictRedis(host="localhost", port=6379, db=0)

# Сохраняем значение по ключу 'mykey'
client.set("mykey", "Hello")

# Читаем значение по ключу 'mykey'
value = client.get("mykey")
print(value.decode())  # Выводим значение на экран (decode() переводит байты в строку)

# Устанавливаем время жизни ключа 'mykey' в 10 секунд
client.expire("mykey", 10)

# Добавляем элемент в список 'mylist'
client.lpush("mylist", "value1")
client.lpush("mylist", "value2")

# Читаем все элементы списка 'mylist'
list_values = client.lrange("mylist", 0, -1)
print([value.decode() for value in list_values])  # Выводим список на экран
