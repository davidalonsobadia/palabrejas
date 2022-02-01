import psycopg2

## Example:
# actinio {
#     'raw_word': 'actinio',
#     'ascii_word': 'actinio',
#     'definition': 'Elemento químico del grupo de los actínidos, que ocurre como producto del decaimiento del uranio. Se utiliza como partícula alfa y en la producción de neutrones.'
#     }

dict = {
'actinio': {
    'raw_word': 'actinio',
    'ascii_word': 'actinio',
    'definition': 'Elemento químico del grupo de los actínidos, que ocurre como producto del decaimiento del uranio. Se utiliza como partícula alfa y en la producción de neutrones.'
    }
}

connection = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="db", port="5432")

cursor = connection.cursor()

insert_query = "INSERT INTO words (ascii_word, word, definition) VALUES ('%s', '%s', '%s')" % (dict['actinio']['ascii_word'], dict['actinio']['raw_word'], dict['actinio']['definition'] )
cursor.execute(insert_query)
connection.commit()

