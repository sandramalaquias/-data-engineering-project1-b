# data-engineering-project1-b
Modelling with Apache Cassandra

![](https://miro.medium.com/max/1400/1*l6ukY_v43LK9LB9fjV2f0g.png)

# Project: Data Modeling with Apache Cassandra

A startup called **Sparkify** wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create an Apache Cassandra database which can create queries on song play data to answer the questions, and wish to bring you on the project. Your role is to create a database for this analysis. You'll be able to test your database by running queries given to you by the analytics team from Sparkify to create the results.

I used the data from a set of CSV files within a directory to create a streamlined CSV file to model, provided by Udacity.


# Datasets

For this project, I will be working with one dataset: `event_data`. The directory of CSV files partitioned by date. Here are examples of filepaths to two files in the dataset:

* event_data/2018-11-08-events.csv
* event_data/2018-11-09-events.csv



### The datafile csv contains the following columns:

-   artist
-   firstName of user
-   gender of user
-   item number in session
-   last name of user
-   length of the song
-   level (paid or free song)
-   location of the user
-   sessionId
-   song title
-   userId

The image below is a screenshot of what the denormalized data should appear.
<a href="https://ibb.co/19B8Gp0"><img src="https://i.ibb.co/4jCPRDF/Screenshot-2022-05-17-at-13-25-05-Project-Data-Modeling-with-Apache-Cassandra.png" alt="Screenshot-2022-05-17-at-13-25-05-Project-Data-Modeling-with-Apache-Cassandra" border="0"></a>


# Project Steps

Below are steps followed to complete each component of this project.

### Modeling your NoSQL database or Apache Cassandra database

1.  Design tables to answer the queries outlined in the project template
2.  Write Apache Cassandra `CREATE KEYSPACE` and `SET KEYSPACE` statements
3.  Develop your `CREATE` statement for each of the tables to address each question
4.  Load the data with `INSERT` statement for each of the tables
5.  Include `IF NOT EXISTS` clauses in your `CREATE` statements to create tables only if the tables do not already exist. We recommend you also include `DROP TABLE` statement for each table, this way you can run drop and create tables whenever you want to reset your database and test your ETL pipeline
6.  Test by running the proper select statements with the correct `WHERE` clause

 Why to use NoSql Apache Cassandra**

>- Need high-availability - always up - no downtime.
>- Have large amount of data
>- Need linear scalability tables to generate results). 
>- Choose availability and part tolerance over consistency

 As Apache Cassandra is a a NoSQL database, think about the query first which will be used to fetch the data based on  which we will create the Table required.

 The main characteristc of Apache Cassandra,  to efficiently retrieve data, the where clause in fetch query must contain all the composite partition keys in the same order as specified in the primary key definition. If this is not provided, will result in error.


## Run the scripts
There are 4 sripts in this ETL project
- cql_queries.py - in this scripts are all queries needed for this project
- create_newfile.py - in this script are all the steps to create a sample of file
- create_tables.py - in this script are all the steps to connect an create tables in Apache Cassandra
- ETL.py - in this scripts are all the steps to do the process ETL, including the scrips above

To run the ETL process is needed only process the scripts ETL.py. 

#### The environment:
-  Python versions from 3.6 to 3.10    
- Pandas
- ![Cassandra](https://docs.datastax.com/en/archived/cassandra/3.0/index.html)
- Re
- Os
- Glob
- Nump. 
- json
- Csv.

## Queries to be answered

### Query 1
#### 1. Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4. 

> a. The expected output is : "Name of the artist, title of the song and length of the track"    
> b. Based on : "sessionId and itemInSession"

From the above two points the query to get the data will be a SELECT statement like :

>SELECT Name of the artist, title of the song, length of the track FROM TABLE_NAME  
>       WHERE sessionId = value AND itemInSession = value

##### Points of interest

<ul>
<li>As the filter will be done based on session_id, the table name for this query will be "Session_library"</li>
<li>The table will be created only if it does not exist.</li>
<li>The PRIMARY KEY will be <em><strong>(sessionId and itemInSession)</strong></em> that are enougth to get unique values for this table.</li>
<li>The query result need only artist, song title and song's length, then they are the table columns.</li>
</ul>

### Query 2
#### 2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182
    
>a. The expected output is : "artist's name, song's title and user: first and last name"    
>b. Based on : "userid and sessionid" - sorted by itemInSession

From the above two points the query to get the data will be a SELECT statement like :

>Select artist name, song's title, user's firstName, user's lastName from Table_name WHERE userId = value and sessionId = value"

##### Points of interest

<ul>
<li>As the filter will be done based on userId, the table name for this query will be "User_library"</li>
<li>The table will be created only if it does not exist.</li>
<li>The PRIMARY KEY will be <em><strong>((userId, sessionId), itemInSession))</strong></em> that are enougth to get unique values for this table.<\li>
<li>Note that the cluster will be  <em><strong>userId and sessionID</strong></em>  and the column <em><strong>itemInSession</em></strong> will be used for sorted ascending.</li>
<li>The query result need only artist's name, song's title and user's name (first and last), then they are the table columns.</li>
</ul>

### Query 3
#### 3. Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'

>a. The expected output is : "user: first and last name"    
>b. Based on : "song's title" 
    
From the above two points the query to get the data will be a SELECT statement like :

>Select firstName, lastName from song_library WHERE song = value"


##### Points of interest

<ul>
<li>As the filter will be done based on song's title, the table name for this query will be "Song_library"</li>
<li>The table will be created only if it does not exist.<\li>
<li>The PRIMARY KEY will be <em><strong>(song, userId)</strong></em> that are enougth to get unique values for this table.<\li>
<li>The query result need only user's name (first and last), then they are the table columns.</li>
<li>Note that, regardless how many times the user listened the song, the table will record only once.
<\ul>

<em><strong>These answer will be showed in the terminal when ETP.py script run.</em></strong>
