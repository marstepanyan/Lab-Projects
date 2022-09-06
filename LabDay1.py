def compression(text):
    new_text = ''
    i = 0
    while i < len(text):
        count = 1
        letter = text[i]
        j = i
        while j < len(text) - 1:
            if text[j] == text[j + 1]:
                count += 1
                j += 1
            else:
                break

        new_text += letter + str(count)
        i = j + 1

    return new_text


def decompression(text):
    old_text = ''
    for i in range(0, len(text), 2):
        old_text += text[i] * int(text[i + 1])

    return old_text


file_object = open('file_name', 'rt+')
compressed_file = open("compressed_text.txt", "w")
decompressed_file = open("decompressed_text.txt", "w")

choose = input('choose between compression and decompression: ')

if choose == 'compression':
    compressed_file.write(compression(file_object.read()))
elif choose == 'decompression':
    decompressed_file.write(decompression(compression(file_object.read())))
else:
    raise ValueError('enter compression or decompression')
