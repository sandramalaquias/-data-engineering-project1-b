"""
    Description: This script is responsible for create sparkify Cassandra database and its tables based on new files create in steop create_new_file.py and then executing the ingest process in according to the function
    that performs the transformation to save it to the database.
    
    ## To get details about these tables structure, please, see on README
"""

# Import Python packages 
import pandas as pd
import cassandra
import re
import os
import glob
import numpy as np
import json
import csv
import cassandra

import create_tables as ct
import create_newfile as cn
from cql_queries import *


# Part I. ETL Pipeline for Pre-Processing the Files
# Try insert to each tables
def insert_row(session, line, ins_list):
## insert table 1         
    try:
        session.execute(insert_queries[0],(int(line[8]), int(line[3]), line[0], line[9], float(line[5])))
    except Exception as e:
        print(e)
    else:    
        ins_list[0] += 1
                          
## insert table 2        
    try:
          session.execute(insert_queries[1],(int(line[10]), int(line[8]), int(line[3]), line[0], line[9], line[1], line[4]))
    except Exception as e:
            print(e)
    else:    
            ins_list[1] += 1
                          
## insert table 3        
    try:
          session.execute(insert_queries[2],(line[9], int(line[10]), line[1], line[4]))
    except Exception as e:
        print(e)
    else:    
        ins_list[2] += 1
                   
    return ins_list


## Print total of process   
def show_total(line_read, ins_list):
    # Show total of records       
    print ("\--------- Rows read=", line_read)
    print ("Inserts in Table sessiom_library=", ins_list[0])
    print ("Inserts in Table user_library=", ins_list[1])
    print ("Inserts in Table song_library=", ins_list[2])
    
    #check total of insert issues
    total = list(set(ins_list))
    if (len(total) == 1) & (int(total[0]) == int(line_read)):
        print ("All rows are in the tables")
    else:
        print ("Not all rows are in the tables")
        print (len(total), total[0], line_read)


# Read file and Insert records on a table 
def read_insert(session, cluster, file):
    file = 'event_datafile_new.csv'
    ins_list = [0, 0, 0]
    line_read = 0
    
    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        for line in csvreader:
            line_read += 1
            #process insert
            ins_list = insert_row(session, line, ins_list)       
            
#display total writer  
    show_total(line_read, ins_list)  
    
#### SELECT to verify that the data have been inserted into each table

## show results like Pandas Data Frame
def get_dataframe(rows, selection, list_columns):
    dict_result = {}
    i = 0
  
    for row in rows:
        dict_result[i] = [content for content in row]
        i += 1
        
    result = pd.DataFrame.from_dict(dict_result, orient='index', columns=list_columns)
        
    with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
            print ('\n ------------------ Query', selection, ' Result')
            print(result[list_columns])
    
def select_process(session):
#Query 1 select records from a table session_library
#Give me the artist, song title and song's length in the music app #history that was heard during sessionId = 338, and iemInSession = #4

    try:
        rows = session.execute(select_table_queries[0]%(338, 4))
    except Exception as e:
        print(e)
    else:    
        ##get the dataframe from result    
        get_dataframe(rows, 1, ['Artist', 'Song'])
            
#Query 2 select records from a table
###Give me only the following: name of artist, song (sorted by ###itemInSession) and user (first and last name) for userid = 10, ###sessionid = 182 """
 
    try:
        rows = session.execute(select_table_queries[1]%(10, 182))
    except Exception as e:
        print(e)
    else:    
        ##get the dataframe from result    
        get_dataframe(rows, 2, ['Artist', 'Song', 'First_Name', 'Last_ Name'])

#Query 3 select records from a table
#Give me every user name (first and last) in my music app  hstory #who listened to the song 'All Hands Against His Own' """
    song = "'All Hands Against His Own'"
    try:
        rows = session.execute(select_table_queries[2]%(song))
    except Exception as e:
        print(e)
    else:
    ##get the dataframe from result    
        get_dataframe(rows, 3, ['First_Name', 'Last_Name'])
        
    
## Process main
def main():
    """
    - create keyspace and tables  
    
    - Creates all tables needed. 
   """ 
    print ("------ETL - Start")
    
    session_cql, cluster_cql = ct.start_tables()
    print ("-------Create Table - End\n")

    
    #create new files based on create_newfile script
    cn.main()
    
    ## read new file and insert into tables   
    print ("-------Insert Records - Start")
    file = 'event_datafile_new.csv'
    read_insert(session_cql, cluster_cql, file)
    print ("-------Insert Records - End \n")
    
    ## get result using select from tables 
    print ("-------Get results - Start")
    select_process(session_cql)
    print ("-------Get results - End")
    
    ## drop tables
    ct.drop_tables(session_cql)
    
    ## close conections
    
    session_cql.shutdown()
    cluster_cql.shutdown()
                        
    print ("\n-----ETL - End of process")


if __name__ == "__main__":
    main()