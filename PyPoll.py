#PyPoll.PyPoll
# #steps
# Open the data file.
# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.
# Winner based on popular vote - total votes each candidate/total votes
import csv
import os

# Assign a variable for the file to load and the path. use the os.path.join tofind the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
# election_data = open(file_to_load, 'r')

with open (file_to_load) as election_data:

    # To do: perform analysis.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
     # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    
    
    
    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)











    # Close the file. not needed if doing with
    # election_data.close()


    # Create a filename variable to a direct or indirect path to the file.
    # file_to_save = os.path.join("analysis", "election_analysis.txt")
    
    # # Using the with statement open the file as a text file.
    # with open(file_to_save, "w") as txt_file:
    
    # # Write some data to the file.
    #     txt_file.write("Counties in the Election\n__________________________________\nArapahoe\nDenver\nJefferson")
        

    # # Close the file
    #     txt_file.close()