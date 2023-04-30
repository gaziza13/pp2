import psycopg2
from config import *

params = {
    "host": "localhost",
    "port": 5432,
    "database": "snake",
    "user": "postgres",
    "password": 112233
}
config = psycopg2.connect(**params)
current = config.cursor()
config.autocommit = True

create_table1 = '''
    CREATE TABLE snake_user(
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    level INTEGER DEFAULT 1
);
'''
create_table2 = '''
    CREATE TABLE score (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES snake_user(id),
    score INTEGER NOT NULL,
    level INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
'''
current.execute(create_table1)
current.execute(create_table2)

current.close()
config.commit()
config.close()