from ai_client import AIClient

def run_summarization():
    ai = AIClient()

    text = """
Microservices architecture allows systems to scale independently,
improves resilience and enables continuous deployment.
"""

    prompt = f"Summarize the following text in one concise sentence:\n{text}"

    response = ai.chat(
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    print(response.choices[0].message.content)