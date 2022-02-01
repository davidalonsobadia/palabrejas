import csv
import unidecode

f = open('../../data/def_spa.csv')
csv_f = csv.reader(f)

# row for the DB: closest ASCII transliteration, unicode word, definition

dict = {}

for index, row in enumerate(csv_f):
    if index == 0:
        continue

    ascii_word = unidecode.unidecode(row[0])

    word_metadata = {
        'raw_word': row[0],
        'ascii_word': ascii_word,
        'definition': row[1]
        }

    if ascii_word not in dict:
        dict.update({ascii_word: word_metadata})

for i, (k, v) in enumerate(dict.items()):
    print(k, v)
    if i > 10:
        break