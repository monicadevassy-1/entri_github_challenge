import streamlit as st
import os
import shutil

st.title("📂 File Categories")

# Check folder
if "folder_path" not in st.session_state:
    st.warning("⚠️ First select a folder from Home page.")
    st.stop()

folder_path = st.session_state["folder_path"]

st.info(f"📂 Selected Folder: {folder_path}")


# Categories
categories = {
    "Images": [
        ".jpg", ".jpeg", ".png",
        ".gif", ".webp", ".bmp"
    ],

    "Documents": [
        ".pdf", ".doc", ".docx",
        ".txt", ".xls", ".xlsx",
        ".ppt", ".pptx"
    ],

    "Videos": [
        ".mp4", ".mkv", ".avi",
        ".mov", ".wmv"
    ],

    "Audio": [
        ".mp3", ".wav", ".aac",
        ".flac", ".ogg"
    ],

    "Archives": [
        ".zip", ".rar",
        ".7z", ".tar"
    ],

    "Programs": [
        ".py", ".java", ".c",
        ".cpp", ".html", ".css",
        ".js"
    ]
}


# Find category
def get_category(extension):

    for category, extensions in categories.items():

        if extension in extensions:
            return category

    return "Others"

# Confirmation popup
@st.dialog("⚠️ Confirm Organization")
def confirm_organize():

    st.warning(
        "⚠️ This will move your files into category folders."
    )

    st.write("Are you sure you want to continue?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Yes, Organize"):

            st.session_state["organize_confirmed"] = True
            st.rerun()

    with col2:
        if st.button("❌ Cancel"):

            st.rerun()


# Organize button
if st.button("📂 Organize Files"):

    confirm_organize()


# Actual organization
if st.session_state.get("organize_confirmed", False):

    st.session_state["organize_confirmed"] = False

    moved_count = 0

    for filename in os.listdir(folder_path):

        source = os.path.join(
            folder_path,
            filename
        )

        # Skip folders
        if os.path.isdir(source):
            continue

        extension = os.path.splitext(
            filename
        )[1].lower()

        category = get_category(extension)

        # Create category folder
        category_folder = os.path.join(
            folder_path,
            category
        )

        os.makedirs(
            category_folder,
            exist_ok=True
        )

        destination = os.path.join(
            category_folder,
            filename
        )

        # Avoid moving if already exists
        if os.path.exists(destination):
            continue

        try:

            shutil.move(
                source,
                destination
            )

            moved_count += 1

        except Exception as e:

            st.error(
                f"Could not move {filename}: {e}"
            )

    st.success(
        f"✅ {moved_count} file(s) organized successfully!"
    )

    st.info(
        "📂 Category folders have been created."
    )