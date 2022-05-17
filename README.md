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



## Run the scripts
There is one scripts in this project, made in Python 

#### The environment:
-  Python versions from 3.6 to 3.10    
- Pandas
- ![Cassandra](https://docs.datastax.com/en/archived/cassandra/3.0/index.html)
- Re
- Os
- Glob
- Numpy
- json
- Csv.

### Queries to be answered

1. Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4)

2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182

3. Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'

