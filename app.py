import streamlit as st

st.title("Crypto Learning AI Agent")
st.write("Ask about crypto or try the quiz!")

user = st.text_input("You:")

if user.lower() == "quiz":
    st.write("What does BTC stand for?")
    answer = st.radio("Choose:", ["Bitcoin", "Binance Token"])

    if st.button("Submit"):
        if answer == "Bitcoin":
            st.success("Correct! BTC stands for Bitcoin.")
        else:
            st.error("Not quite. BTC stands for Bitcoin.")

elif user.lower() == "btc":
    st.info("BTC stands for Bitcoin, the first cryptocurrency.")

elif user != "":
    st.write("Try typing 'quiz' or 'btc'.")
