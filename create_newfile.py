"""
        Part I. ETL Pipeline for Pre-Processing the Files
        Description: This script is responsible to create a new file based on event_files that will be used to perform 
        the transformation to save it to the Apache Cassandra database.
"""

# Import Python packages 
import re
import os
import glob
import json
import csv


def get_file(file_name):
    """
    Description: This function is responsible for listing the files in a directory,
    and then return a list of files to be processed.

    Arguments:
        file: '/event_data'.

    Returns:
        File path list
    """
      
    
    # get all files matching extension from directory
    # checking current working directory
    print(os.getcwd())

    # Get current folder and subfolder event data
    filepath = os.getcwd() + file_name

    # Create a for loop to create a list of files and collect each filepath
    for root, dirs, files in os.walk(filepath):
    
        # join the file path and roots with the subdirectories using glob
        file_path_list = glob.glob(os.path.join(root,'*'))
    
    print("Total file_path_list =", len(file_path_list))
    
    ## to see first row, uncoment a line below
    print("Example of file:", file_path_list[0])
    
    return file_path_list



def get_data(file_path_list):
    ''' This function is responsable to create a smaller event data csv file called event_datafile_new csv that will be used
    to insert data into the Apache Cassandra tables '''
    
    # initiating an empty list of rows that will be generated from each file
    full_data_rows_list = [] 
    
    # for every filepath in the file path list 
    for f in file_path_list:

    # reading csv file 
        with open(f, 'r', encoding = 'utf8', newline='') as csvfile: 
            # creating a csv reader object 
            csvreader = csv.reader(csvfile) 
            next(csvreader)
        
     # extracting each data row one by one and append it        
            for line in csvreader:
                full_data_rows_list.append(line) 
            
    # show the total number of rows 
    print("Full data rows = ", len(full_data_rows_list))
    #print ("First row:\n", full_data_rows_list[0])


    # creating a smaller event data csv file called event_datafile_new csv that will be used to insert data into the Apache Cassandra tables

    ## The filter will be: select only records that 'artist' has value then result at smaller one

    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    
    ##list column of interes
    cols = ['artist','firstName','gender','itemInSession',   'lastName','length','level','location','sessionId', 'song', 'userId']
    qtd_writer = 0

    with open('event_datafile_new.csv', 'w', encoding = 'utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(cols)
        for row in full_data_rows_list:
            if (row[0] == ''):
                continue
            else:
                qtd_writer += 1
                writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))   
    
    print ("Total rows in new file = ",qtd_writer)
    
def main():
    """
    Description: This function is responsible to get a file path for "'/event_data' and write a new file for the data"""
    print ("---------Create newfile - Start")
    file_path_list = get_file('/event_data')
    
    get_data(file_path_list)
    print ("-------Create New File - End\n")


if __name__ == "__main__":
    main()