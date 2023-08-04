import streamlit as st
import pandas
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

with st.container():
    st.write("Below you can find some of the apps I built in Python. Feel free to contact me!")

# to get information from the data.csv file, we can use a built-in module called pandas that is best suited
# with dealing with csv files

df = pandas.read_csv("data.csv", sep=";")  # to get the information in form of a table, use the sep=";" as the text is
# separated by a semicolon.

col3, col4 = st.columns(2)
with col3:
    # this will iterate through the first
    for index, item in df[:10].iterrows():
        st.header(item["title"])

with col4:
    for index, item in df[10:].iterrows():
        st.header(item["title"])