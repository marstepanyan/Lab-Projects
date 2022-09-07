text = open('file_name', 'rt+').read()
results = open('analyzed_file.txt', 'w')

words = text.split()
for item in words:
    if not item.isalpha():
        words.remove(item)


def number_of_words(arr):
    return len(arr)


def number_of_letters(arr):
    res = 0
    for word in arr:
        res += len(list(word))
    return res


def number_of_sentences(txt):
    sentences = [s for s in txt.split('.') if s != '']
    return len(sentences)


def most_used_letter(arr):
    counts = {}
    for letter in ''.join(arr):
        counts[letter] = ''.join(arr).count(letter)

    res = max(counts, key=counts.get)
    return res


def most_used_word(arr):
    counts = {}
    for word in arr:
        counts[word] = arr.count(word)

    res = max(counts.values())
    return res if res > 1 else 0


results.writelines(('Words: ', str(number_of_words(words)), '\n'
                    'Letters: ', str(number_of_letters(words)), '\n'
                    'Sentences: ', str(number_of_sentences(text)), '\n'
                    'Letter frequency: ', str(most_used_letter(words)), '\n'
                    'Word frequency: ', str(most_used_word(words))
                    ))


"""
print('Words: ', number_of_words(words))
print('Letters: ', number_of_letters(words))
print('Sentences: ', number_of_sentences(text))
print('Letter frequency: ', most_used_letter(words))
print('Word frequency: ', most_used_word(words))"""
