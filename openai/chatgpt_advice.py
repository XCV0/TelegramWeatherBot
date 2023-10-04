import httpx
import asyncio

client = httpx.AsyncClient()
model = 'gpt-3.5-turbo'
history = [{"role": "system", "content": "You are a helpful assistant."},
           {"role": "user", "content": "вопрос"}]
user = 123

result = await client.post(
    url = 'https://api.openai.com/v1/chat/completions',
    headers={
        "Authorization": "Bearer" + "",
    },
    json = {
        'model': model,
        'messages': history,
        'user': user
    },
    timeout=20
)
