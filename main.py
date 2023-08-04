import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/IMG-0089.jpg", width=300)
with col2:
    st.title("Maxwell Nyimbili")
    content = """I have a passion for technology, specifically, innovating how business processes are conducted, 
    with an emphasis on improving the Small and Medium Enterprises (SMEs) environment, for business owners not 
    technologically capable. I possess leadership, public speaking, as well as problem solving skills. 
    Furthermore, I continue to improve my competency with the Python programming language, as well as my 
    Web Development skills.
    """
    st.info(content)