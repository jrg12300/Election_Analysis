

#The data we need to retrieve
# 1) Total number of votes caste
# 2) A complete list of candidates who received votes
# 3) The percentage of votes each candidate won
# 4) Total number of votes each candiate won
# 5) the winner of popular vote


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    # for row in file_reader:
    #   print(row[1])
    headers = next(file_reader)
    print(headers)