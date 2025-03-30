import time

import redis

# Создаем подключение к Redis
client = redis.StrictRedis(host="localhost", port=6379, db=0)


def expensive_computation(n):
    """Функция для дорогих вычислений, например, сумма чисел от 1 до N."""
    time.sleep(2)  # Симуляция длительных вычислений
    return sum(range(1, n + 1))


def get_from_cache_or_compute(n):
    """Пытаемся получить данные из кэша, если их нет — выполняем вычисления и кэшируем результат."""

    # Проверяем, есть ли результат в кэше
    cached_result = client.get(f"computation:{n}")

    if cached_result:
        # Если результат есть в кэше, возвращаем его
        print("Получено из кэша!")
        return int(cached_result)

    # Если результата нет в кэше, вычисляем и сохраняем в кэш
    print("Вычисление...")
    result = expensive_computation(n)

    # Сохраняем результат в кэш с временем жизни 60 секунд
    client.setex(f"computation:{n}", 60, result)

    return result


# Тестируем функцию
print(get_from_cache_or_compute(10))  # Первая попытка: вычисляем и кэшируем
print(get_from_cache_or_compute(10))  # Вторая попытка: получаем из кэша
