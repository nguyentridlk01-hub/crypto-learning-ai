import streamlit as st

st.title("Crypto Learning AI")

user = st.text_input("Ask about crypto or type 'quiz'")

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
