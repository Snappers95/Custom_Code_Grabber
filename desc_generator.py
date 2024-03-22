# Author: Jacob Laviolette
# Date: 3/22/2024

from openai import OpenAI


OPENAI_API_KEY = '<API_KEY>'


def get_ai_description(prompt):
    """
    Use OpenAI API to get a description for each file, Passes entire SQL text to API.
    :param prompt: The SQL text we want to describe.
    :return: Ai-Generated Response wrapped in comment block.
    """
    client = OpenAI(api_key=OPENAI_API_KEY)
    message = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": "Provide extremely short response describing the base functions of the provided SQL."},
            {"role": "user", "content": prompt}
        ],
    )
    return str(f'/* AI SUMMARY: {message.choices[0].message.content} */\n')


def main():
    pass


if __name__ == "__main__":
    main()
