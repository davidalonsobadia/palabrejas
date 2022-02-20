import csv
import unidecode


def get_words():
    words = {}

    f = open('data/def_spa.csv')
    csv_f = csv.reader(f)

    for index, row in enumerate(csv_f):
        if index == 0:
            continue

        ascii_word = unidecode.unidecode(row[0])

        if " " not in ascii_word and ascii_word not in words:
            word_metadata = {
                'raw_word': row[0].replace("'", " "),
                'ascii_word': ascii_word.replace("'", " "),
                'definition': row[1].replace("'", " ")
            }
            words.update({ascii_word: word_metadata})

    return words
