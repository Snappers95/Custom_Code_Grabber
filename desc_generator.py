# Author: Jacob Laviolette
# Date: 3/22/2024

from openai import OpenAI


OPENAI_API_KEY = '<API_KEY>'


def get_ai_description(prompt):
    client = OpenAI(api_key=OPENAI_API_KEY)
    message = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": "Povide extremely short response describing the base functions of the provided SQL."},
            {"role": "user", "content": prompt}
        ],
    )
    return str(f'/* AI SUMMARY: {message.choices[0].message.content} */\n')


def main():
    pass


if __name__ == "__main__":
    main()
