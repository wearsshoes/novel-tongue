---
title: Language Teaching Gradu-lateral book
created: '2024-04-30T21:56:30.050Z'
modified: '2024-04-30T21:58:35.135Z'
---

# Language Teaching Gradu-lateral book

## Motivation

[[Scott's original idea]]

## My modifications to Scott’s idea:

- Want to start with switchovers immediately? Like - grammar - “to be - ser.” Just do that immediately? 1 grammar note per section.
    - Probably actually the first is THE >> EL/LA LOS/LAS
- I would expect that it’d be hopeless to get through the whole book in one go. Most of the book will remain untranslated until the end
- Probably you’d want to tokenize the whole thing? And highlight the first replacement instance of each token?
- Editing tool - want to be able to quickly tag through the work
- Want to source things that have existing bilingual versions, e.g. The Little Prince
- Might need some underlying grammar engine for programmatically mapping the bilingual versions to each other
- Noting that this project doesn’t really scale - you do it with one book, you’re sorta stuck - what level do you start the next book at?

- So for learning languages, this doesn’t super help with spoken, right? But maybe you could make it work with some sort of speech synth? Like your tia’s spanglish
- Pain points for English>>Spanish
    - Masculine/feminine
    - Ser/estar

## Austin’s advice

- MVP should almost certainly be static, not dynamic or interactive.
- Try doing the first few chapters - try doing the first chapter manually to see what will be tough
- Probably not that strong a language idea - otherwise they’d be doing it all over the place

## Extensions

- Note that you could in fact build a whole suite around this. Like, you could have the teacher choose which concepts to introduce where in the book? (Seems like somewhat annoying even with the best tooling)

## let's see
so you have the word alignments, but you also have the attentions
so if you have: --alignment, --\

## Reasons this wouldn't work
* Basic conceptual questions abound. How are you going to format languages which run in different directions?
* Most people won't have this as their first language contact, so they might be able to absorb some vocab faster. In general vocab is easier to learn, I think?
* Most interesting books have some degree of complicated grammar. A book that would otherwise be a great text for this, Alice in Wonderland, employs some incredible run-on sentences. Students usually learn a language by starting with simple grammars and moving upwards to sentences of greater complexity.
* Doesn't teach sound or pronunciation, so you're purely learning a literary language. All human languages are read out loud, so you're always missing something.
* Most machine translations focus only on the startpoints and endpoints. Being able to specify a series of intermediate transitions is a task for which there is basically no tooling.
* Doing direct vocabulary substition usually doesn't work, because almost all utterances contain turns of phrase, where semantics are embedded at levels larger than individual words. There aren't many tokenizations of these.
