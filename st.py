import streamlit as st
import requests
st.markdown(
    "<h1 style='text-align:center; color:navy; font-style:italic; font-weight:bold;'>📦 Displaying Data as DATAFRAME & JSON Format (via FastAPI)</h1>",
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .stApp {
        background-color: teal;
    }
    </style>
    """,
    unsafe_allow_html=True
)


#st.title("Displaying Data in CSV & JSON Formats (via FastAPI)")

# Call FastAPI endpoint
response = requests.get("http://127.0.0.1/csv-to-json/")
if response.status_code == 200:
    data = response.json()
    cc=["JSON", "DataFrame"]
    selected_view = st.sidebar.selectbox("Select View", cc)
    if selected_view == "JSON":
        st.json(data)  # nicely formatted JSON
    elif selected_view == "DataFrame":
        st.dataframe(data)  # table view
else:
    st.error("Failed to fetch data from FastAPI")

