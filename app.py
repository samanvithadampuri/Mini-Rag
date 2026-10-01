
import streamlit as st
import ollama

st.title("Snacks Stall")

st.write("Enjoy the tasty food!")

st.button("Click here to open")

st.sidebar.button("Drop")

text = st.text_input("Enter Your Favourite Dish")

prompt = st.text_area("Ask")

if st.button("Send"):

    if prompt:

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        st.write(response["message"]["content"])

    else:
        st.warning("Please enter a question!")