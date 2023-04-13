import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Bionic Reading API Response")

url = "https://bionic-reading1.p.rapidapi.com/convert"

user_input = st.text_input("Please type anything here:")

if user_input:
    payload = "content={}&response_type=html&request_type=html&fixation=1&saccade=10".format(user_input)
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "c81a99a1a7mshfe0051848f9bdfap19d4a9jsnc8fc6674dadb",
        "X-RapidAPI-Host": "bionic-reading1.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    # Parse the response HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract only the contents within the <b> tags
    b_tags = soup.find_all('b', class_='bionic-b bionic')

    # Create a list to store the formatted words
    formatted_words = []

    # Iterate through the <b> tags
    for tag in b_tags:
        # Extract the bold text
        bold_text = tag.text

        # Find the next sibling (non-bold text)
        sibling = tag.next_sibling
        if sibling:
            normal_text = sibling.string
        else:
            normal_text = ""

        # Combine bold and normal text
        formatted_word = f"<b>{bold_text}</b>{normal_text}"
        formatted_words.append(formatted_word)

    # Join the extracted contents and display the result
    bionic_text = ' '.join(formatted_words)
    st.write(bionic_text, unsafe_allow_html=True)
