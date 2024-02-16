import os
import openai

openai.api_key = os.getenv("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")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        """
def foo(n, k):
    accum = 0
    for i in range(n):
        for l in range(k):
            accum += i
    return accum
"""
    ],
    temperature=0,
    max_tokens=256,
)

print(response)
