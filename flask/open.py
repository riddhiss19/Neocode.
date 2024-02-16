import openai

openai.api_key = "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"


def getComment(data):
    prompt = f"Give me python docstring for below python code :\n\n{data}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    documentation = response.choices[0].text

    return '"""\n' + documentation + '\n"""\n' + data
