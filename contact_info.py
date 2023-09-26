import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

def create_streamlit_content():
    load_css()

    st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://github.com/tapal123)")

    col1, col2, col3 = st.columns(3)
    col2.image(Image.open('dp.png'))

    st.header('Junaid Tapal, B.Tech')

    st.info('I am a software engineer graduate from SRM in specialization of AIML.')

    icon_size = 20

    st_button('linkedin', 'https://www.linkedin.com/in/tapal-junaid-573577223', 'linkedin', icon_size)

if __name__ == "__main__":
    create_streamlit_content()
