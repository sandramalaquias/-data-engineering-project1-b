## Scrip to queries to drop, create, insert and select
# DROP TABLES

## TO-DO: Drop the table for each query
query1_drop = "drop table IF EXISTS session_library"
query2_drop = "drop table IF EXISTS user_library"
query3_drop = 'drop table IF EXISTS song_library'


# CREATE TABLES

## TO-DO: Query 1:  Give me the artist, song title and song's length in the music app history 
##                  that was heard during sessionId = 338, and itemInSession = 4


query1_create = "CREATE TABLE IF NOT EXISTS session_library "
query1_create = query1_create + """(sessionId int, itemInSession int, userId int, artist text, song text, length float, 
                PRIMARY KEY (sessionId, itemInSession, userId))"""

## TO-DO: Query 2: Give me only the following: name of artist, song (sorted by itemInSession) and user 
##                 (first and last name) for userid = 10, sessionid = 182 

query2_create = "CREATE TABLE IF NOT EXISTS user_library "
query2_create = query2_create + """(userId int, sessionId int, itemInSession int, artist text, song text, firstName text, lastName text, PRIMARY KEY (userId, sessionId, itemInSession))"""

   
## TO-DO: Query 3: Give me every user name (first and last) in my music app history who listened to the song '
## 'All Hands Against His Own'

query3_create = "CREATE TABLE IF NOT EXISTS song_library "
query3_create = query3_create + """(song text, sessionId int, itemInSession int, userId int, firstName text, lastName text, 
                PRIMARY KEY (song, sessionId, iteminSession, userId))"""


# INSERT RECORDS

## TO-DO: Assign the INSERT statements into the `query` variable
query1_insert = "INSERT INTO session_library (sessionId, itemInSession, userId, artist, song, length)"
query2_insert = "INSERT INTO user_library (userId, sessionId, itemInSession, artist, song, firstName, lastName)"
query3_insert = "Insert INTO song_library (song, sessionId, itemInSession, userId, firstName, lastName)"
    
#query = query + "<ASSIGN VALUES HERE>"
query1_insert = query1_insert + " VALUES (%s, %s, %s, %s, %s, %s)"
query2_insert = query2_insert + " VALUES (%s, %s, %s, %s, %s, %s, %s)"
query3_insert = query3_insert + " VALUES (%s, %s, %s, %s, %s, %s)"


# FIND results for each query
# Query 1:. Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, 
# and itemInSession = 4

query1_select = "select * from session_library WHERE sessionId = %s and itemInSession = %s"

## Query 2: Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name)\
## for userid = 10, sessionid = 182

query2_select = "select * from user_library WHERE userId = %s and sessionId = %s"

## TO-DO: Query 3: Give me every user name (first and last) in my music app history who listened to the song '
## 'All Hands Against His Own'

query3_select = "select * from song_library WHERE song = %s"

# QUERY LISTS

create_table_queries = [query1_create, query2_create, query3_create]
drop_table_queries = [query1_drop, query2_drop, query3_drop]
select_table_queries = (query1_select, query2_select, query3_select)
insert_queries = [query1_insert, query2_insert, query3_insert]

