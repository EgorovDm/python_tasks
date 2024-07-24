#!/usr/bin/env python3

def single_root_words(root_word: str, *other_words: str) -> list[str]:
    '''Finds word with defined (1st arg, root_word) substring'''
    root_word = root_word.lower()
    same_words = []
    for w in other_words:
        if ((root_word in w.lower()) or (w.lower() in root_word)):
            same_words.append(w)
    return same_words

print(
    single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
)
print(
    single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
)