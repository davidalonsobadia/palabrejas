import psycopg2


def insert_in_db(words):
    connection = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5432")
    cursor = connection.cursor()

    for (k, v) in words.items():
        insert_query = "INSERT INTO words (ascii_word, word, definition) VALUES ('%s', '%s', '%s')" % (v['ascii_word'], v['raw_word'], v['definition'])
        cursor.execute(insert_query)
        connection.commit()

    if connection:
        cursor.close()
        connection.close()
