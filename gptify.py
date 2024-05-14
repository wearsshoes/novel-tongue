"""
Calls the OpenAI API to interact with GPT-4o.
"""

from openai import OpenAI
import anthropic
client = OpenAI()

def gpt(system_prompt, prev, tgt):
    """
    Ask GPT to merge the source and target sentences.
    """
    messages = [
        {
        "role": "system",
        "content": [
            {
            "type": "text",
            "text": f"{system_prompt}"
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": f"{prev}\n{tgt}"
            }
        ]
        },
    ]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content

client2 = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    # api_key="my_api_key",
)


def clod(system_prompt, prev1, tgt1):
    """
    Ask clod to merge the source and target sentences.
    """

    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"{prev1}\n{tgt1}"
                }
            ]
        }
    ]

    message = client2.messages.create(
        messages=messages,
        model="claude-3-sonnet-20240229",
        max_tokens=1000,
        temperature=0,
        system=f"{system_prompt}",
        )

    return message.content[0].text

