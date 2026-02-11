from tasks.text_completion import run_text_completion
from tasks.classification import run_classification
from tasks.summarization import run_summarization
from tasks.sentiment import run_sentiment
from tasks.chat_app import run_chat

def main():
    print("""
1 - Text Completion
2 - Classification
3 - Summarization
4 - Sentiment Analysis
5 - Chat Application
""")

    choice = input("Select option: ")

    if choice == "1":
        run_text_completion()
    elif choice == "2":
        run_classification()
    elif choice == "3":
        run_summarization()
    elif choice == "4":
        run_sentiment()
    elif choice == "5":
        run_chat()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()