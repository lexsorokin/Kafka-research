import redis

client = redis.StrictRedis(host="localhost", port=6379, db=0)

# Добавляем элементы в начало списка
client.lpush("mylist", "value1")
client.lpush("mylist", "value2")

# Добавляем элемент в конец списка
client.rpush("mylist", "value3")

# Извлекаем элементы из списка
print(client.lpop("mylist").decode())  # value2
print(client.rpop("mylist").decode())  # value3

# Получаем все элементы списка
elements = client.lrange("mylist", 0, -1)
print([e.decode() for e in elements])  # ['value1']
