<<<<<<< Updated upstream
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
=======
import openai

openai.api_key = ""

# Define the system message
system_msg = 'You are a helpful assistant who understands data science.'

# Define the user message
user_msg = 'Create a small dataset about total sales over the last year. The format of the dataset should be a data frame with 12 rows and 2 columns. The columns should be called "month" and "total_sales_usd". The "month" column should contain the shortened forms of month names from "Jan" to "Dec". The "total_sales_usd" column should contain random numeric values taken from a normal distribution with mean 100000 and standard deviation 5000. Provide Python code to generate the dataset, then provide the output in the format of a markdown table.'

# Create a dataset using GPT
response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                        messages=[{"role": "system", "content": system_msg},
                                         {"role": "user", "content": user_msg}])
>>>>>>> Stashed changes
