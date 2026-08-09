import streamlit as st
import tkinter as tk
from tkinter import filedialog


st.markdown("""
<style>

[data-testid="stSidebarNav"] {
    display: none;
}

</style>
""", unsafe_allow_html=True)


st.set_page_config(
    page_title="File Sort Explorer",
    page_icon="📁",
    layout="wide"
)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("📁 File Sort Explorer")

    st.divider()

    st.page_link(
        "main.py",
        label="🏠 Home"
    )

    st.page_link(
        "pages/file_categorize.py",
        label="📂 Categories"
    )

    st.page_link(
        "pages/file_search.py",
        label="🔍 Search Files"
    )

    st.page_link(
        "pages/file_duplicate.py",
        label="♻️ Duplicate Files"
    )

    st.divider()

    st.caption("Hackathon Project")


# ---------------- HOME ----------------

st.title("📁 File Sort Explorer")

st.write(
    "Organize, search and manage your files easily."
)

st.divider()

st.subheader("📂 Select Your Folder")


# Folder selection
if st.button("📂 Select Folder"):

    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    folder = filedialog.askdirectory()

    root.destroy()

    if folder:

        st.session_state["folder_path"] = folder

        st.success("✅ Folder selected successfully!")


# Show selected folder
if "folder_path" in st.session_state:

    st.info(
        f"📂 Selected Folder: "
        f"{st.session_state['folder_path']}"
    )

else:

    st.warning(
        "Please select a folder to start."
    )