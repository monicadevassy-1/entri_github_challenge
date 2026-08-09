import streamlit as st
import os
import hashlib
import send2trash


st.title("♻️ Duplicate Files")


# =========================
# SELECTED FOLDER
# =========================

if "folder_path" not in st.session_state:
    st.warning("⚠️ First select a folder from Home page.")
    st.stop()

folder_path = st.session_state["folder_path"]

st.info(f"📂 Selected Folder: {folder_path}")


# =========================
# FILE HASH
# =========================

def get_file_hash(file_path):

    sha256 = hashlib.sha256()

    try:

        with open(file_path, "rb") as f:

            while True:

                data = f.read(1024 * 1024)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except Exception:

        return None


# =========================
# FIND DUPLICATES
# =========================

if st.button("🔍 Find Duplicate Files"):

    file_groups = {}

    with st.spinner("🔎 Scanning files..."):

        for root, folders, files in os.walk(folder_path):

            for filename in files:

                file_path = os.path.join(root, filename)

                if not os.path.isfile(file_path):
                    continue

                file_hash = get_file_hash(file_path)

                if file_hash is None:
                    continue

                if file_hash not in file_groups:
                    file_groups[file_hash] = []

                file_groups[file_hash].append(file_path)


    duplicates = []


    # =========================
    # KEEP OLDEST AS ORIGINAL
    # =========================

    for file_hash, files in file_groups.items():

        if len(files) > 1:

            # Sort by creation time
            files.sort(
                key=lambda x: os.path.getctime(x)
            )

            # FIRST = ORIGINAL
            original = files[0]

            # REST = DUPLICATES
            for duplicate in files[1:]:

                duplicates.append(
                    {
                        "duplicate": duplicate,
                        "original": original
                    }
                )


    st.session_state["duplicates"] = duplicates


    if duplicates:

        st.success(
            f"✅ {len(duplicates)} duplicate file(s) found!"
        )

    else:

        st.info("🎉 No duplicate files found!")


# =========================
# SHOW DUPLICATES
# =========================

if "duplicates" in st.session_state:

    duplicates = st.session_state["duplicates"]


    if duplicates:

        st.subheader("🗂️ Duplicate Files")


        for item in duplicates:

            duplicate_path = item["duplicate"]
            original_path = item["original"]


            # If duplicate already removed
            if not os.path.exists(duplicate_path):
                continue


            duplicate_name = os.path.basename(
                duplicate_path
            )

            original_name = os.path.basename(
                original_path
            )


            st.write(
                f"📄 **Duplicate:** {duplicate_name}"
            )

            st.caption(
                f"Original: {original_name}"
            )

            st.caption(
                f"Duplicate Path: {duplicate_path}"
            )


            # =========================
            # DELETE DUPLICATE
            # =========================

            if st.button(
                f"♻️ Delete Duplicate - {duplicate_name}",
                key=f"delete_{duplicate_path}"
            ):

                try:

                    # IMPORTANT
                    # Delete ONLY duplicate
                    safe_path = os.path.normpath(
                        os.path.abspath(duplicate_path)
                    )


                    # Safety check
                    if safe_path == os.path.normpath(
                        os.path.abspath(original_path)
                    ):

                        st.error(
                            "🛑 Safety Stop! Original file cannot be deleted."
                        )

                        continue


                    # Check duplicate exists
                    if not os.path.isfile(safe_path):

                        st.error(
                            "❌ Duplicate file not found."
                        )

                    else:

                        # Move duplicate to Recycle Bin
                        send2trash.send2trash(
                            safe_path
                        )


                        st.success(
                            f"♻️ {duplicate_name} moved to Recycle Bin!"
                        )


                        # Remove from list
                        st.session_state[
                            "duplicates"
                        ].remove(item)


                        st.rerun()


                except Exception as e:

                    st.error(
                        f"❌ Delete failed: {e}"
                    )


    else:

        st.info(
            "🎉 No duplicate files available."
        )