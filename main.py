import streamlit as st
st.write("Hello, World!")

st.title("Title")
st.header("Header")
st.subheader("Sub-header")

st.title("Simple Web Form with Streamlit")

st.ehader("User Information Users")

name = st.text_input("Enter your name: ")

options = ["Option 1", "Option 2", "Option 3"]
seletced_option = st.selectbox("Choose an Option: "), options

slider_value = st.slider("Select a value", 1, 100, 50)

if st.button("Submit"):
    st.write(f"Name: {name}")
    st.write(f"Selecetd Option: {seletced_option}")
    st.write(f"Slider Value: {slider_value}")

    st.subheader("Summary")
    st.write("Fill out the form above and click the Submit button to see detail")
    