import redis

client = redis.StrictRedis(host="localhost", port=6379, db=0)

# Устанавливаем поля в хеше
client.hset("user:1000", "name", "Alice")
client.hset("user:1000", "age", 30)

# Получаем значение по ключу из хеша
name = client.hget("user:1000", "name").decode()
print(name)  # Alice

# Увеличиваем значение по ключу
client.hincrby("user:1000", "age", 1)

# Получаем все поля и значения хеша
user_data = client.hgetall("user:1000")
print(
    {k.decode(): v.decode() for k, v in user_data.items()}
)  # {'name': 'Alice', 'age': '31'}
