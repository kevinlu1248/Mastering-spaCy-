#!/usr/bin/env python3

import spacy
nlp = spacy.load("en")
doc = nlp("I went for working and worked for 3 years.")
for token in doc:
    print(token.text, token.lemma_)

