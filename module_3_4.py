def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.upper()
    x = len(other_words)
    for i in range(x):
        o_w = other_words[i]
        o_w = o_w.upper()
        if o_w in root_word:
            same_words.append(other_words[i])
        elif root_word in o_w:
            same_words.append(other_words[i])
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)