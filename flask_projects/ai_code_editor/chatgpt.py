import os
from openai import OpenAI
from pathlib import Path
import json

def answer_me(input_text):
    # Load the API key from a JSON file
    with open('config.json', 'r') as file:
        config = json.load(file)
        api_key = config['openai_api_key']

    client = OpenAI(
        # This is the default and can be omitted
        api_key=api_key,
    )

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"{input_text}"
            }
        ]
    )

    return completion.choices[0].message.content