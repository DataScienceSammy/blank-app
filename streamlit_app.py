import streamlit as st
import requests
from datetime import datetime

st.title("Notion Embed API Diagnostics")

api_url = st.text_input(
    "API URL",
    "https://api.github.com/zen"
)

if st.button("Test API call"):
    try:
        started = datetime.utcnow()

        response = requests.get(api_url, timeout=10)

        finished = datetime.utcnow()

        st.success("Request completed")
        st.write("Status code:", response.status_code)
        st.write("Response time:", (finished - started).total_seconds(), "seconds")
        st.write("Called at:", finished.isoformat() + "Z")

        st.subheader("Response headers")
        st.json(dict(response.headers))

        st.subheader("Response body")
        st.code(response.text[:2000])

    except requests.exceptions.Timeout:
        st.error("Request timed out")

    except requests.exceptions.RequestException as e:
        st.error("Request failed")
        st.code(str(e))
