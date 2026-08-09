import streamlit as st
import os

st.title("🔍 Search Files")

if "folder_path" not in st.session_state:

    st.warning(
        "⚠️ First select a folder from Home."
    )

    st.stop()


folder_path = st.session_state["folder_path"]

st.info(
    f"📂 Searching in: {folder_path}"
)


search = st.text_input(
    "🔍 Enter file name",
    placeholder="Example: photo"
)


if search:

    results = []

    for root, folders, files in os.walk(folder_path):

        for filename in files:

            if search.lower() in filename.lower():

                results.append(
                    os.path.join(
                        root,
                        filename
                    )
                )


    st.subheader(
        f"🔎 {len(results)} file(s) found"
    )


    if results:

        for file in results:

            st.write(
                "📄",
                os.path.basename(file)
            )

            st.caption(file)

    else:

        st.info("No matching files found.")