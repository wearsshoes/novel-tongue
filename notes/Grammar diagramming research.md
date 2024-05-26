---
title: Grammar diagramming research
created: '2024-04-30T21:57:34.535Z'
modified: '2024-04-30T22:20:51.891Z'
---

# Grammar diagramming research

## main questions
* Feed to LLM via API or use older system?


## Research to do

* Grammar frequency study (e.g. is it better to do infinitives first?)
    * Can just do this experimentally
    * Might be easier to just do the easy transitions first: *-tion/-cion*, *-ly/-mente*
* Does conjugation tokenization improve LLM comprehension for cross/lingual purposes?

### Grammar

## Treebank
https://en.wikipedia.org/wiki/Treebank




## idea for grammar transfer
* modification of translation model
* Transfer between latent spaces as normal, for syntax
* When taking out of latent space, you want to then re-lexicalize with nearest-neighbor english word, with the lexicalizer trained on extremely masked context (like prev/next token). So it's sort of like real translation and then shitty back-translation? (or: it's an encoder/decoder with a powerful encoder and a silly decoder tacked on)
* doesn't quite capture scott's string-literal idea of "Ryuk-about, Death Note-of secret Light-to taught." -- well, it could - if it's a word alignment model with the right tokenization?

## idea for word alignment leaderboard run
* also a panelist grab-bag method, like combAlign
* just update to use awesome-align and mask-align
* fine-tune gpt on gold standard, then have gpt act as one of the panelists
* don't forget to have gpt do validation w/o finetuning just to see where it's at
* train on low-resource languages and see how you do
* it's just obscure enough a task that there's low hanging fruit everywhere.