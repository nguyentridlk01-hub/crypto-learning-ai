def explain_crypto(topic):

    topic = topic.lower()

    if "blockchain" in topic:
        return "Blockchain is a decentralized ledger that records crypto transactions."

    elif "bitcoin" in topic:
        return "Bitcoin is the first cryptocurrency and runs on blockchain."

    elif "binance" in topic:
        return "Binance is one of the largest crypto exchanges where users trade cryptocurrencies."

    else:
        return "I can explain crypto topics like blockchain, bitcoin, and Binance."


def generate_quiz():

    print("\nQuiz Time!")
    print("What does BTC stand for?")
    print("A. Bitcoin")
    print("B. Binance Token")

    answer = input("Your answer: ")

    if answer.lower() == "a":
        print("Correct! ??")
    else:
        print("Not correct. BTC means Bitcoin.")


def agent_loop():

    print("Crypto Learning AI Agent")
    print("Ask about crypto or type 'quiz'")

    while True:

        user = input("\nYou: ")

        if user.lower() == "quiz":
            generate_quiz()

        elif user.lower() == "exit":
            print("Goodbye!")
            break

        else:
            response = explain_crypto(user)
            print("AI:", response)


agent_loop()