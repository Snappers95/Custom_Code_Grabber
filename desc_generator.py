# Author: Jacob Laviolette
# Date:

# import requests
from openai import OpenAI
import sys

OPENAI_API_KEY = sys.argv[1]


def get_ai_description(prompt):
    client = OpenAI(api_key=sys.argv[1])
    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": prompt
        }],
        model="gpt-3.5-turbo-0125"
    )
    return chat_completion


def main():
    print(get_ai_description('what day is it?'))


if __name__ == "__main__":
    main()
