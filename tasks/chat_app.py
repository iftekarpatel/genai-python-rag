from ai_client import AIClient

def run_chat():
    ai = AIClient()

    chat_history = [
        {
            "role": "system",
            "content": """You are a friendly hiking enthusiast.
Ask user location and hiking intensity before suggesting hikes.
Include interesting facts."""
        }
    ]

    print("AI Hiking Assistant (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        chat_history.append({"role": "user", "content": user_input})

        stream = ai.chat(chat_history, stream=True)

        full_response = ""
        print("AI: ", end="")

        for chunk in stream:
            if not chunk.choices:
                continue

            delta = chunk.choices[0].delta

            if hasattr(delta, "content") and delta.content:
                content = delta.content
                print(content, end="", flush=True)
                full_response += content

        print("\n")

        chat_history.append({"role": "assistant", "content": full_response})