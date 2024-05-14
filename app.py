"""
Main application script for the app.
"""

import streamlit as st
from gptify import gpt, clod

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title("NovelTongue :book::tongue:")


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


@st.cache_data
def ask_gpt_to_do_it(task, text1, text2):
    """
    Get the GPT response for the given task and sentences.
    """
    return gpt(task, text1, text2)

@st.cache_data
def ask_clod_to_do_it(task, text1, text2):
    """
    Get the GPT response for the given task and sentences.
    """
    return clod(task, text1, text2)

FILE_PATH = "notebooks/aligned_texts/c1_aligned.txt"
src_sents, tgt_sents = load_aligned_texts(FILE_PATH)

def tasks(n):
    """
    Return the task for the given index.
    """

    definite_article_rule= (
        "Definite article rule: If the English sentence contains the word 'the' "
        "and the Spanish sentence contains a corresponding 'el', 'la', 'los', or 'las', "
        "replace 'the' in the English sentence with the corresponding Spanish definite article, "
        "wrapped in `:blue[]`. Don't do 'del' yet. \n\n"
    )

    punctuation_rule = (
        "Punctuation rule: Use all Spanish punctuation marks in the English sentence, strictly following the Spanish sentence's example. Match style. "
        "Put each punctuation mark, original or newly added, inside the Streamlit tag ':blue[]'. Don't wrap text in the tag. \n"
        "Example 1: `'Well!'` | `«¡Vaya! »` Result: `:blue[«¡]Well:blue[! »]` \n"
        "Example 2: `Do you think you could manage it?) 'And` | `¿Creéis que esto es posible? - ¡Y` Result: `:blue[¿]Do you think you could manage it:blue[? - ¡]And` \n\n"
    )

    noun_phrase_rule = (
        "Noun phrase rule: In the English sentence, make adjectives follow nouns, as in Spanish. "
        "Wrap the modified phrases in the Streamlit tag `:blue[]`.. \n\n"
    )

    phrase_swap_rule = (
        "Phrase swap rule: If there is a turn of phrase in the English sentence "
        "for which the Spanish sentence does not contain a literal translation, wrap it in `:green[]`. "
        "In parentheses behind it, place the Spanish colloquialism that replaces it in the translation, wrapped in `:blue[]`. "
        "Example: `rather glad` | `se alegro` Result: `:green[rather glad]:blue[(se alegró)]` \n\n"

    )

    task = "Here is an English sentence with a reference Spanish translation. Apply each of the following transformations sequentially: \n\n"
    task += definite_article_rule
    if n > 3:
        task += punctuation_rule
    if n > 6:
        task += noun_phrase_rule
    if n > 9:
        task += phrase_swap_rule
    task += "Discard the Spanish sentence, do not translate or copy. Return only the modified or unmodified English sentence."
    return task


for i, (src, tgt) in enumerate(zip(src_sents[36:66], tgt_sents[36:66])):

    merge = ask_clod_to_do_it(tasks(i), src, tgt)
    # merge = "All in :blue[la] golden afternoon"

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"{i}, :red[{src}]")
    with col2:
        st.markdown(f":red[{merge}]")
    with col3:
        st.markdown(f":blue[{tgt}]")
    if i % 3 == 0 and i > 0:
        st.write("----")
