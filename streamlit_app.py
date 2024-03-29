import streamlit as st
from streamlit.delta_generator import DeltaGenerator as _DeltaGenerator
from altair import Chart
from rembg import remove
from PIL import Image

def removebg(img):
    input = Image.open(img)
    return remove(input)



def main():
    st.title("GURU PRASAATH NEW APP")
    st.header("Choose an image")
    uploaded_file =st.file_uploader("",type=["jpg","png"])

    if uploaded_file is not None:
        st.image(uploaded_file)
        st.write("Processing.....")
        result = removebg(uploaded_file)
        st.image(result)
        st.write("You can download the Image..")


if __name__ == "__main__":
    main()
