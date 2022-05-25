"""
    Description: This script is responsible for create sparkify Cassandra database and its tables based on new files create in steop create_new_file.py and then executing the ingest process in according to the function that performs the transformation to save it to the database.
    
    To get details about these tables structure, please, see on README
"""

# Import Python packages 
import cassandra

from cql_queries import create_table_queries, drop_table_queries
from cassandra.cluster import Cluster

#Creating a Cluster 
#Return session, cluster connect
def create_cluster():
    """
    - Creates and connects to the sparkifydb
    - Returns the connection
    """
    
    # This should make a connection to a Cassandra instance your local machine 
    # (127.0.0.1)
    cluster = Cluster()

    # To establish connection and begin executing queries, need a session
    session = cluster.connect()
    
    # Create a Keyspace 
    try:
        session.execute("""
        CREATE KEYSPACE IF NOT EXISTS udacity 
        WITH REPLICATION = 
        { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }""")

    except Exception as e:
        print(e)
        
    #Set KEYSPACE to the keyspace specified above
    try:
        session.set_keyspace('udacity')
    except Exception as e:
        print(e)
        
    return session, cluster


def drop_tables(session):
    """
    Drops each table using the queries in `drop_table_queries` list.
    The queries are in cql_queries.py
    """
    for query in drop_table_queries:
        try:
            rows = session.execute(query)
        except Exception as e:
            print(e)


def create_tables(session):
    """
    Creates each table using the queries in `create_table_queries` list.
    The queries are in Cql_queries.py
    """
    for query in create_table_queries:
        try:
            session.execute(query)
        except Exception as e:
            print(e)  
            
def describe_tables(session):
    tables = session.execute("SELECT * FROM system_schema.tables WHERE keyspace_name = 'udacity';")
    
    for table in tables:
        print ("Table created:", table[1])
        
def start_tables():
    #this funcion is responsabel to create connection and tables
    print ("------Create Tables - Start")

    session, cluster = create_cluster()
    drop_tables(session)
    create_tables(session)
    describe_tables(session)
    return session, cluster
    
def main():
    """
    - Drops (if exists) and Creates the sparkify database. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    session_cql, cluster_cql = start_tables()
    drop_tables(session_cql)

    session_cql.shutdown()
    cluster_cql.shutdown()
    
    print ("------Create Tables - End of process")


if __name__ == "__main__":
    main()