import requests
import json

def get_advice(weather):
    history = [{"role": "system", "content": f"Посоветуй что одеть по этой погоде\n{weather}"},
               {"role": "user", "content": "вопрос"}]

    result = requests.post(
        url='https://api.openai.com/v1/chat/completions',
        headers={
            "Authorization": "Bearer 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",
        },
        json={
            'model': 'gpt-3.5-turbo',
            'messages': history,
        },
        timeout=20
    )

    print(result)
    # response = result.json()
    # return response['choices'][0]['message']['content']