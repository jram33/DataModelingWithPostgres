# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id serial PRIMARY KEY, 
                                                                  start_time timestamp, user_id varchar, 
                                                                  level varchar, song_id varchar, 
                                                                  artist_id varchar, session_id int, 
                                                                  location varchar, user_agent varchar);""")
        
user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id varchar PRIMARY KEY, first_name varchar, 
                                                          last_name varchar, gender char, level varchar);""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id varchar, title varchar, 
                                                          artist_id varchar, year int, duration numeric,
                                                          PRIMARY KEY (song_id, artist_id));""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id varchar PRIMARY KEY, name varchar, 
                                                              location varchar, latitude numeric, 
                                                              longitude numeric);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time timestamp PRIMARY KEY, hour int, day int,
                                                         week int,month int, year int, weekday int);""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration)
                        VALUES (%s, %s, %s, %s, %s) ON CONFLICT (song_id, artist_id) DO NOTHING;""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]