# Load Libraries
from psycopg2 import sql

# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id TEXT PRIMARY KEY, 
    start_time TEXT, 
    user_id INT, 
    level TEXT, 
    song_id TEXT, 
    artist_id TEXT, 
    session_id INT, 
    location TEXT, 
    user_agent TEXT
)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(
    user_id INT PRIMARY KEY, 
    first_name TEXT, 
    last_name TEXT, 
    gender TEXT, 
    level TEXT
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(
    song_id TEXT PRIMARY KEY, 
    title TEXT NOT NULL, 
    artist_id TEXT NOT NULL, 
    year INT NOT NULL, 
    duration NUMERIC NOT NULL
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(
    artist_id  TEXT PRIMARY KEY, 
    name TEXT NOT NULL, 
    location TEXT, 
    latitude NUMERIC, 
    longitude NUMERIC
    );
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time TIMESTAMP, 
    hour INT NOT NULL, 
    day INT NOT NULL, 
    week INT NOT NULL, 
    month INT NOT NULL, 
    year INT NOT NULL, 
    weekday TEXT NOT NULL
    );
""")

# INSERT RECORDS
songplay_table_insert = sql.SQL("INSERT INTO {} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) \
                            ON CONFLICT (songplay_id) DO NOTHING").format(sql.Identifier('songplays'))

user_table_insert = sql.SQL("INSERT INTO {} VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO NOTHING").format(sql.Identifier('users'))

song_table_insert = sql.SQL("INSERT INTO {} VALUES (%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING").format(sql.Identifier('songs'))

artist_table_insert = sql.SQL("INSERT INTO {} VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING").format(sql.Identifier('artists'))

time_table_insert = sql.SQL("INSERT INTO {} VALUES (%s, %s, %s, %s, %s, %s, %s)").format(sql.Identifier('time'))

# FIND SONGS
song_select = ("""
SELECT  
    songs.song_id,
    artists.artist_id
FROM songs 
LEFT OUTER JOIN artists ON
    songs.artist_id=artists.artist_id
WHERE songs.title=%s AND artists.name=%s AND songs.duration=%s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

