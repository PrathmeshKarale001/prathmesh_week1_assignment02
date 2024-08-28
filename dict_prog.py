def count_word_frequencies(text):
    word_frequencies = {}
    words = text.split()
    for word in words:
        word = word.lower()
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
    return word_frequencies

text = "The quick brown fox jumps over the lazy dog. The dog is very lazy."
result = count_word_frequencies(text)
print(result)