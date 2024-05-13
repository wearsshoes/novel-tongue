---
title: MVP
created: '2024-04-30T21:58:36.414Z'
modified: '2024-04-30T21:58:38.556Z'
---

# MVP

- Source material: Little Prince
- Layout: Plaintext
- Still want to highlight key words
- Basic tokenizer
    - Basic word swap selector
        - this might want lists of conjugations?
- Basic semantic mapping
    - Basic grammar swap selector
- First instance of word has a grammar highlight (this can be nonfunctional) - can also revisit at any time?
- does it make sense to have color-coded language? I’m not sure how you would make this look not insane? quizas light highlights?
    - for bastardized words we can do a sort of **redblue** thing
    - new words are always bold-blue
- eventually you’ll have to switch from one language being highlighted to the other. Maybe when >50% of the words are one language, the other language is in highlights instead?
-



## Future

- Idiomatics get filtered out first, maybe, and get their own notes?

---
title: Report writeup
created: '2024-05-01T00:56:21.918Z'
modified: '2024-05-01T01:06:22.545Z'
---

# Report writeup

https://github.com/explosion/spacy-models/releases/tag/es_core_news_sm-3.7.0
https://github.com/explosion/spacy-models/releases/tag/en_core_web_sm-3.7.1

chose alice in wonderland because relatively simple and sufficiently long and stuff.

https://github.com/facebookresearch/MUSE/blob/main/README.md
https://dl.fbaipublicfiles.com/arrival/dictionaries/es-en.txt
https://dl.fbaipublicfiles.com/arrival/dictionaries/en-es.txt

-- doesn't seem to need lemmatization

What's hard
- producing mappings
- phrases eg "llevarlo a cabo"


Bertalign
https://github.com/bfsujason/bertalign

https://github.com/explosion/spacy-streamlit
-- for visualization

Streamlit pieces

https://github.com/ddobrinskiy/streamlit-jupyter
https://st-annotated-text.streamlit.app/

https://github.com/arnaudmiribel/streamlit-extras


https://github.com/Mohamed-512/Extra-Streamlit-Components
- stepper bar

tooling
https://github.com/pydantic/pydantic
https://github.com/arnaudmiribel/streamlit-faker