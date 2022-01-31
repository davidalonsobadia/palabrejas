import csv
import unidecode

f = open('../../data/def_spa.csv')
csv_f = csv.reader(f)

# row for the DB: closest ASCII transliteration, unicode word, definition
normalized_row = []

for index, row in enumerate(csv_f):
    ## remove expressions with more than one word, and remove duplicates
    if len(row[0].split()) == 1:
        normalized_row.append({
            'word': row[0],
            'ascii_word': unidecode.unidecode(row[0]),
            'definition': row[1]
        })

print(normalized_row[1])