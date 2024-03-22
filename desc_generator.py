# Author: Jacob Laviolette
# Date:

import requests
from openai import OpenAI
import sys

OPENAI_API_KEY = sys.argv[1]


def get_ai_description():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    response_json = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json={
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "ping"}],
        "temperature": 0
    }).json()

    print(response_json[message])


def main():
    get_ai_description()


if __name__ == "__main__":
    main()
