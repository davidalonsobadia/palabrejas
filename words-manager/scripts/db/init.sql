CREATE TABLE words (
    id SERIAL PRIMARY KEY,
    word VARCHAR(100) NOT NULL,
    ascii_word VARCHAR(100) NOT NULL,
    definition VARCHAR(500)
)

