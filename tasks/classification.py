from ai_client import AIClient

def run_classification():
    ai = AIClient()

    prompt = """
Classify each statement into one of these categories:
Complaint, Suggestion, Praise, Other.

1. The app crashes frequently.
2. Add dark mode please.
3. Excellent performance!
4. What are your office hours?
"""

    response = ai.chat(
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    print(response.choices[0].message.content)