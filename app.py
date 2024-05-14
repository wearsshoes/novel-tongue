"""
Main application script for the app.
"""

import streamlit as st
from gptify import gpt, clod

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title("NovelTongue")
st.sidebar.image("https://files.oaiusercontent.com/file-QYbvhFOy3UtWZUocs19A1mXe?se=2024-05-14T03%3A42%3A47Z&sp=r&sv=2023-11-03&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3Dddba2758-b759-4ecf-946c-8e62570edf54.webp&sig=ZoPIglT7PqPZwwM2vo11p6MQN0rVjEcfctZHIUf8PNw%3D", width=200)


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


def default_rules():
    """
    Return the default rules.
    """
    rules = [
        ("Definite article rule: If the English sentence contains the word 'the' and the Spanish sentence contains a corresponding 'el', 'la', 'los', or 'las', replace 'the' in the English sentence with the corresponding Spanish definite article, wrapped in ':blue[]'. Don't do 'del' yet.\n\n", 0),
        ("Punctuation rule: Use all Spanish punctuation marks in the English sentence, strictly following the Spanish sentence's example. Match style. Put each punctuation mark, original or newly added, inside the Streamlit tag ':blue[]'. Don't wrap text in the tag. \nExample 1: ''Well!'' | '«¡Vaya! »' Result: ':blue[«¡]Well:blue[! »]' \nExample 2: 'Do you think you could manage it?) 'And' | '¿Creéis que esto es posible? - ¡Y' Result: ':blue[¿]Do you think you could manage it:blue[? - ¡]And'\n\n", 3),
        ("Similar word rule: In the English sentence, if its translation in the Spanish sentence sounds almost the same, replace that English word with the Spanish equivalent. Wrap the new word in the Streamlit tag ':blue[]'.\n\n", 6),
        ("Phrase swap rule: If there is a turn of phrase in the English sentence for which the Spanish sentence does not contain a literal translation, wrap it in ':blue[]'. In parentheses behind it, place the Spanish colloquialism that replaces it in the translation, wrapped in ':blue[]'. Example: 'rather glad' | 'se alegro' Result: ':blue[rather glad]:blue[(se alegró)]'\n\n", 9),
    ]
    return rules

def tasks(n, custom_rules):
    """
    Return the task for the given index.
    """
    task = "Here is an English sentence with a reference Spanish translation. Apply each of the following transformations sequentially: \n\n"
    rules = custom_rules
    rules = sorted(rules, key=lambda x: x[1])
    for rule, start_index in rules:
        if n >= start_index:
            task += rule
    task += "Discard the Spanish sentence, do not translate or copy. Return only the modified or unmodified English sentence.\n\n"
    return task


# Load default rules
initial_rules = default_rules()

st.sidebar.title("Custom Rules")
custom_rules = []
num_rules = st.sidebar.number_input("Number of custom rules", min_value=0, max_value=10, value=len(initial_rules), step=1)

for i in range(num_rules):
    if i < len(initial_rules):
        rule, start_index = initial_rules[i]
    else:
        rule = ""
        start_index = 0
    rule = st.sidebar.text_area(f"Rule {i + 1}", value=rule)
    start_index = st.sidebar.number_input(f"Start index for rule {i + 1}", min_value=0, value=start_index, step=1)
    custom_rules.append((rule, start_index))


for i, (src, tgt) in enumerate(zip(src_sents[36:66], tgt_sents[36:66])):
    merge = ask_gpt_to_do_it(tasks(i, custom_rules), src, tgt)
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
