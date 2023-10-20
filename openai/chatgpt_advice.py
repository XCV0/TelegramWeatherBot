import httpx
import asyncio

client = httpx.AsyncClient()
model = 'gpt-3.5-turbo'

user = 123


async def get_advice(weather):
    history = [{"role": "system", "content": f"Посоветуй что одеть по этой погоде\n"
                                             f"{weather}"},
               {"role": "user", "content": "вопрос"}]

    result = await client.post(
        url='https://api.openai.com/v1/chat/completions',
        headers={
            "Authorization": "Bearer" + "",
        },
        json={
            'model': model,
            'messages': history,
            'user': user 
        },
        timeout=20
    )

    return result['choice'][0]['message']
