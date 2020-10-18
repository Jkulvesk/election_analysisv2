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

#creat total votes variable
total_votes = 0
#make a list for candidate names
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

file_to_save = os.path.join("analysis", "election_analysis.txt")

with open (file_to_load) as election_data:

    # To do: perform analysis.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
     # Read and print the header row.
    headers = next(file_reader)
    #print(headers)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
      
            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count. ALIGN THIS WITH THE IF STATEMENT TO ITERATE OVER ALL CANDIDATE NAMES, OTHERWISE IT WILL JUST SHOW 1
        candidate_votes[candidate_name] += 1

        # Save the results to our text file.
        with open(file_to_save, "w") as txt_file:
            # Print the final vote count to the terminal.
            election_results = (
                f"\nElection Results\n"
                f"-------------------------\n"
                f"Total Votes: {total_votes:,}\n"
                f"-------------------------\n")
            print(election_results, end="")
            # Save the final vote count to the text file.
            txt_file.write(election_results)

            #print candidate options
            #print(candidate_votes)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        
       candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        with open(file_to_save, "a") as txt_file:
            # Save the final vote count to the text file.
            txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
# Save the winning candidate's name to the text file.
    with open(file_to_save, "a") as txt_file:
        txt_file.write(winning_candidate_summary)

#  To do: print out the winning candidate, vote count and percentage to
#   terminal.


    # 4. Print the candidate name and percentage of votes.
    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
   

    # 3. Print the total votes.
        #print(total_votes)
    
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