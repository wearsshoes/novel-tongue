"""
Main application script for the app.
"""

import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title("NovelTongue")
st.sidebar.image(
    "https://files.oaiusercontent.com/file-QYbvhFOy3UtWZUocs19A1mXe?se=2024-05-14T03%3A42%3A47Z&sp=r&sv=2023-11-03&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3Dddba2758-b759-4ecf-946c-8e62570edf54.webp&sig=ZoPIglT7PqPZwwM2vo11p6MQN0rVjEcfctZHIUf8PNw%3D",
    width=200,
)


@st.cache_data
def load_aligned_texts(file_path):
    """
    Load aligned texts from a file.
    """
    src_text = []
    tgt_text = []
    with open(file_path, "r", encoding="UTF-8") as f:
        c1 = f.read()

        lines = c1.splitlines()
        for j in range(0, len(lines), 3):
            src_text.append(lines[j])
            tgt_text.append(lines[j + 1])
    return src_text, tgt_text


FILE_PATH = "notebooks/hb_aligned_texts/c1_aligned.txt"
src_sents, tgt_sents = load_aligned_texts(FILE_PATH)
mix_sents = load_aligned_texts("notebooks/hb_calque_texts/c1_mix_aligned.txt")[0]

for i, (src, mix, tgt) in enumerate(zip(src_sents, mix_sents, tgt_sents)):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"{i}, :red[{src}]")
    with col2:
        st.markdown(f":red[{mix}]")
    with col3:
        st.markdown(f":blue[{tgt}]")
    if i % 3 == 0 and i > 0:
        st.write("----")
