import httpx

# Инициализируем клиент с base_url
client = httpx.Client(base_url="http://localhost:8000")

# Выполняем GET-запрос, используя относительный путь
response = client.get("/api/v1/users/me")

# Выводим ответ в консоль
print(response.text)
