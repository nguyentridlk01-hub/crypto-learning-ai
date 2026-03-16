def run_agent():
    print("Crypto Learning AI Agent (OpenClaw Style)")
    print("Ask about crypto or type 'quiz'")
    print("Type 'exit' to quit\n")

    while True:
        user = input("You: ")

        if user.lower() == "quiz":
            print("\nWhat does BTC stand for?\n")
            print("A. Bitcoin")
            print("B. Binance Token")

            answer = input("\nYour answer: ")

            if answer.upper() == "A":
                print("\nCorrect! BTC stands for Bitcoin.\n")
            else:
                print("\nNot quite. BTC stands for Bitcoin.\n")

        elif user.lower() == "btc":
            print("\nBTC stands for Bitcoin, the first cryptocurrency.\n")

        elif user.lower() == "exit":
            print("\nGoodbye!\n")
            break

        else:
            print("\nTry typing 'quiz' or ask about BTC.\n")


if __name__ == "__main__":
    run_agent()
