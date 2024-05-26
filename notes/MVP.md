---
title: MVP
created: '2024-04-30T21:58:36.414Z'
modified: '2024-04-30T21:58:38.556Z'
---

# Original MVP: before I knew much
- Source material: Little Prince
- Layout: Plaintext
- Still want to highlight key words maybe
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

# Example data
src_tokens = ["I", "love", "coding"]
tgt_tokens = ["J'aime", "coder"]
alignment = [[0, 0], [1, 0], [2, 1]]

## Future
- Idiomatics get filtered out first, maybe, and get their own notes?


### parts of toolchain
*   **Preprocessing**
    *   Scraping/import
    *   Text cleaning
    *   Parameter adjustments (which models, etc)
    *   Sample preview
    *   possibly - marketplace for licensing bilingual books in copyright?
*   **ML pass**
    *   Visualizations? Probably just a progress bar
    *   Bertalign (works already)
    *   Look for a multilingual phrase detector, build your own
        *   With MT
    *   Write your own word aligner, eventually
        *   With dict?
*   **Realignment suite**
    *   sentence realignment *(super easy to build)*
        *   vertical presentation
        *   split/merge/shift/swap/redraw

    *   phrase realignment *(sort of exists already)*
        *   MT for idiom lookup
        *   probable phrase highlighting (llm?)
    *   word alignment *(manAlign)*
        *   popout from horizontal presentation
        *   horizontal presentation
        *   redraw (hotkeys)
    *  attention-informed heatmap/subalignments
*   **CAT suite**
    *   (part of toolchain which already is closest to existing)
    *   named element tagging
    *   pos tagging
    *   treebank adjustment
        *   (might help to use typing on granular types of parts of speech based on argument order, like lojban? seems annoying though)
*   **Lesson prep suite**
    *   word/definition replacement
    *   syntax switching rule builder (this seems really hard.)
*   **Presentation suite**
    *   language-specific options (toggle transliteration, etc?)
    *   book-independent progress memory? (then how will teachers toggle lesson levels? maybe lessons can be presented as total XP across books?)
    *   feedback