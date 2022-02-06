import psycopg2

words = {
    'actinio': {
        'raw_word': 'actinio',
        'ascii_word': 'actinio',
        'definition': 'Elemento químico del grupo de los actínidos, que ocurre como producto del decaimiento del uranio. Se utiliza como partícula alfa y en la producción de neutrones.'
        },
    'publicidad': {
        'raw_word': 'publicidad',
        'ascii_word': 'publicidad',
        'definition': 'Acción de llamar la atención hacia bienes, servicios o eventos, frecuentemente a través de anuncios pagos en periódicos, revistas, televisión o radio.'
        },
}

connection = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="db", port="5432")

cursor = connection.cursor()


for i, (k, v) in enumerate(words.items()):
    insert_query = "INSERT INTO words (ascii_word, word, definition) VALUES ('%s', '%s', '%s')" % (v['ascii_word'], v['raw_word'], v['definition'])
    cursor.execute(insert_query)
    connection.commit()

if connection:
    cursor.close()
    connection.close()

