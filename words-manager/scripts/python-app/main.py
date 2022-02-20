from sanitize_data import get_words
from insert_data import insert_in_db


def main():
    words = get_words()
    insert_in_db(words)
    print('Data added to the DB')


if __name__ == '__main__':
    main()
