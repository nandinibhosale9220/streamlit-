import streamlit as st

st.set_page_config(
    page_title="My First Website",
    page_icon="🌐"
)

# Center the logo and text
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(
        "https://streamlit.io/images/brand/streamlit-mark-color.png",
        width=250
    )

    st.markdown(
        "<h1 style='text-align: center;'>Streamlit</h1>",
        unsafe_allow_html=True
    )

st.title("My First Streamlit Website")

st.write("Welcome to my first web page! 🎉")

name = st.text_input("What is your name?")

if name:
    st.success(f"Hello, {name}! 👋")
