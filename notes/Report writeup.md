# Language Learning

## Theory

### Narrative

Scott Alexander had this idea for a way to learn a language:
You have a novel which is in your language.
As you read on, the novel takes on the language you want to learn.
First the grammar, then the vocabulary transform, until you're reading mostly in the other language, with unfamiliar words either explained or left untranslated.

I thought this was a pretty interesting idea to look into, so I decided to see how I might go about doing something like this. Alice in Wonderland is available in the public domain in English and Spanish, so I decided to test the idea with a book I was familiar with and two languages I was familiar with. But even starting with the existing bilingual version, I immediately saw it would be far too much manual labor to try to refrormat things like "from now on, nouns come before adjectives instead of after them", so I thought about how you might make it work using a computer. The things you'd have to do would be:

- Figure out which English sentences match which Spanish sentences
- Within sentences, figure out which English words match which Spanish words.
- Set rules for transforming grammar and vocabulary, and decide where in the novel they start to apply.
- Account for turns of phrase and idioms, that is to say, ways of communicating which don't translate exactly.

How hard could it be to get computers to do these things? Well, it turns out that these are some of the classic problems in natural language processing (NLP), and thus of AI in general. Machine translation is hard enough; and it's usually done by putting text in one side of a complicated neural algorithm and getting the translation out the other; the computer can't really tell you how it's done, because it doesn't know, and it can't programmatically step through each translation step and tell you what's going on, or what relates to what.

In fact, as [this paper](https://arxiv.org/pdf/2212.00138) explains, one of the major reasons why we have modern large language models (LLMs) now is because researchers needed to find ways to track context dependent meanings across long distances for translation purposes, and this led to the invention of the transformer architecture, which is able to hold information about the entire text sequence when evaluating the meaning of a word (or determining what word should go in a position).

LLMs (and other transformer-based models in various ways) are the key to making this project possible now. It would have been an incredibly tedious project when Scott Alexander proposed the idea in 2013. I'm using LLMs for much of the project, but because of the precision of the task, it's been incredibly helpful to learn the history of this field.


## Process

### Scraping text
I took the text of Alice in Wonderland in English and Spanish from [Bilinguis](http://bilinguis.com/), which is an educational website that presents some public domain texts in multiple languages side by side. It's pretty neat, and I'd recommend it as a language learning tool.

### Processing sentence alignments
Sentence alignment is the process of figuring out which sentences from each of two texts are the same as each other. For example:

1.   > CHAPTER I.

     > Capítulo I


2.   > Down the Rabbit-Hole

     > En la madriguera del conejo

3.   > Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversation?'

     > Alicia empezaba ya a cansarse de estar sentada con su hermana a la orilla del río, sin tener nada que hacer: había echado un par de ojeadas al libro que su hermana estaba leyendo, pero no tenía dibujos ni diálogos. «¿Y de qué sirve un libro sin dibujos ni diálogos?», se preguntaba Alicia.

For this, I used [Bertalign](https://github.com/bfsujason/bertalign), which is a multilingual-BERT based sentence aligner. Multilingual-BERT is a machine learning model trained on translations, so is good at telling when two sentences in different languages have similar abstract meanings.

Bertalign is designed to align entire translated works, so it assumes that most of the sentences match, and roughly in linear order. It first goes straight down the page matching the sentences in each language which have the closest meaning to each other, and covers most of the sentences this way. It then looks between the matched sentences to find groups of sentences which match. For example, where perhaps the English says in one long sentence what is best expressed in Spanish as two shorter sentences, it can find those matches as well.

This works extremely well, although being somewhat new to working with torch models, I could only get it to run inside of a colab.

### Processing word alignments
One major problem in general here is that sentences often have lots of words that don't match between translations, because each language has its own turns of phrase. For example, take these sentences:

> And she went on planning **to herself** how she would **manage it**.

> Y siguió planeando cómo iba a **llevarlo a cabo** (*carry it to completion*).

First, the clause "to herself", which is mostly unnecessary even in English, has no corresponding words in the Spanish version. Second, the colloquial English phrase "manage it" has an equivalent colloquialism in Spanish that doesn't mention managing.

It requires a deeper method of reasoning about sentence alignment to be able to account for those turns of phrase.

Nevertheless, it's part of a good starting point, so I used [awesome-align](https://github.com/neulab/awesome-align), which is also based on multilingual-BERT. I don't have the sophistication to easily understand what it's doing, but basically they are trying to find the words that are the most similar in meaning, and have the most similar role in each sentence, and then listing a match if the significance is above a certain threshold.

Frankly, awesome-align doesn't work terribly well out of the box for English to Spanish, and would probably benefit from being fine-tuned on the source and target languages. It misses a bunch of obvious connections.

### Getting syntax trees
Syntax trees

Used spaCy

### Getting bilingual token dictionaries
Bilingual token dictionaries are a simplified form of dictionary which simply lists each source language word with each of its correspondences in the target language. For example, "the el", "the los", "the la", "the las". It doesn't tell you grammar or meaning. The value is quickly finding words to substitute, and I can use the parse tree, parts of speech, and word alignments to double check whether or not the substitution is valid.

Obtaining this was really easy. Meta AI has published several dozen bilingual dictionaries as part of the [MUSE project](https://github.com/facebookresearch/MUSE).

### Aligning tokenizations
This was a pretty annoying intermediate step, which I am mentioning just because it was an annoying coding problem. BERT and Spacy use different tokenizers, which means they cut up words differently into tokens that they can process. There's a library published by spaCy's parent company which aligns the tokenizations, but you further have to align the data associated with the tokens. Ultimately, it turned out that mostly I could just merge BERT tokens together and finesse them into spaCy's scheme.

### Applying word substitutions
*

### Applying rules
*

### Transforming the text

### Creating tools for educators
I'm really stuck here. Even writing a

Probably the thing to do is to

### Presentation