# election_analysis

## Overview of Election Audit
The Colorado Board of Elections employee gave me a task to calculate the election results including the total of votes, total of votes by candidate, total votes by county, percent of votes by county and candidate, county with most vodes and calculation of the winner.

## Resources
The file used to calculate the data was the election_results.csv.
I am using python 3.7.6 for this analysis.

## Election Audit Results
Here's a summary of the results of the election.
- Total votes cast: 369,711
- Votes by county:
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
- County with largest number of votes: Denver
- Number of votes and percentage of total votes received by candidate:
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)
- Winner of the election: 
  - Winner: Diana DeGette
  - Winning Vote Count: 272,892
  - Winning Percentage: 73.8%

For reference, see screenshots of results as shown on terminal and text file.

![screenshots](https://user-images.githubusercontent.com/72076683/96385697-2d060f00-115b-11eb-8902-2740ff27a901.png)

![screenshots](https://user-images.githubusercontent.com/72076683/96385712-41e2a280-115b-11eb-8b77-768314a47cdc.png)

## Challenge Summary
The way this script is written, you can use it for future elections. All you need to ensure is that the data of the CSV is formatted in the same way with votes, counties and candidates in the same columns. To use it for the next year, you will only need to update this line of code in the file: pypoll_challenge.py

** file_to_load = os.path.join("Resources", "election_results.csv") **

To find this line, you can simply to control F and do a search for it. What you will need to change is the path where the new csv file is located. (Resources is the folder and election_results.csv is the file name.)

You will also want to output the results to a new text file. Here is the line of code that specifies where to place the output.

** file_to_save = os.path.join("analysis", "election_analysis.txt") **

In the code above, you will replace the 'analysis' with your new folder name and update the election analysis.txt file name if you want (maybe include the year).

If you want to do further analysis on the election results, you could if the data exists. Let's say in column 4 of the csv file you have city. You could copy the code used for county totals (including the variable names), and do the same for city totals. 
