from ai_client import AIClient

def run_sentiment():
    ai = AIClient()

    prompt = """
Analyze sentiment line by line and give overall summary:

1. I love this product!
2. The battery life is terrible.
3. It’s okay, not great.
4. Customer service was amazing.
"""

    response = ai.chat(
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    print(response.choices[0].message.content)