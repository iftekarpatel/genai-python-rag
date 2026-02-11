from ai_client import AIClient

def run_text_completion():
    ai = AIClient()

    user_prompt = input("Enter your prompt: ")

    response = ai.chat(
        messages=[
            {"role": "user", "content": user_prompt}
        ]
    )

    print("\nAI Response:\n")
    print(response.choices[0].message.content)

    print("\nToken Usage:")
    print(response.usage)