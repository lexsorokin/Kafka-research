import redis

client = redis.StrictRedis(host="localhost", port=6379, db=0)

# Добавляем элементы в множество
client.sadd("myset", "apple", "banana", "orange")

# Проверяем наличие элемента
print(client.sismember("myset", "banana"))  # True

# Удаляем элемент из множества
client.srem("myset", "orange")

# Получаем все элементы множества
print([item.decode() for item in client.smembers("myset")])  # ['banana', 'apple']
