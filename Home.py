import streamlit as st

st.set_page_config(layout="wide")

col = st.columns(1)
with col:
    st.title("Ardit Sulce")
    content = """
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.
        It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.
        The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters,
    """
    st.info(content)

