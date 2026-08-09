import streamlit as st

st.title("🔍 Search Files")

if "files" not in st.session_state:
    st.warning("Please select a folder from Home first.")
    st.stop()

files = st.session_state["files"]

search = st.text_input(
    "Search file",
    placeholder="Type file name..."
)

if search:

    results = [
        file for file in files
        if search.lower() in file.name.lower()
    ]

    st.subheader(f"🔎 {len(results)} result(s)")

    for file in results:
        st.write("📄", file.name)

else:
    st.info("Enter a file name to search.")