CREATE TABLE public.words
(word_id SERIAL PRIMARY KEY,
ascii_word CHAR(100) NOT NULL,
word CHAR(100) NOT NULL,
definition CHAR(255));