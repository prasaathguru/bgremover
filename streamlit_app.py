import streamlit as st
from streamlit.delta_generator import DeltaGenerator as _DeltaGenerator
from altair import Chart
from rembg import remove
from PIL import Image
from textblob import TextBlob
import nltk


def removebg(img):
    input = Image.open(img)
    return remove(input)

def sentiment(input):
    blob = TextBlob(input)
    sentiment = blob.sentiment.polarity #-1 to 1
    print(sentiment)
    print(input)
    return sentiment

def main():
    # # Example of a slider widget
    # st.write("You can select your age")
    # age = st.slider("Select your age", 0, 100, 25)

    # chart_data = [1, 2, 3, 4]
    # st.line_chart(chart_data)

    # # Example of a button
    # if st.button("Click me"):
    #      st.write("Button clicked!")
    st.sidebar.header("Enter the text")
    user_input = st.sidebar.text_input("")
    # user_input = st.text_input("Enter the text")
    # st.write(user_input)
    output = sentiment(user_input)
    st.write("Your Sentiment analysis is....")
    st.write(output)

    st.title("GURU PRASAATH NEW APP")
    st.sidebar.header("Choose an image")
    uploaded_file =st.sidebar.file_uploader("",type=["jpg","png"])

    if uploaded_file is not None:
        st.image(uploaded_file)
        st.write("Processing.....")
        result = removebg(uploaded_file)
        st.image(result)

    

if __name__ == "__main__":
    main()
