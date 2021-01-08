

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

#intialize a total vote counter and candidate list and a candidate vote counter
total_votes = 0
candidate_options =[]
candidate_votes={}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # total all votes
    for row in file_reader:
        total_votes += 1
        # add candidate to unique list of candidates
        if row[2] not in candidate_options:
            candidate_options.append(row[2])
            candidate_votes[row[2]]=0
        candidate_votes[row[2]]+=1


    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes)*100
        #print(f"{candidate_name}: recieved {vote_percentage:.2f}% of the vote")
        if (votes > winning_count) and (vote_percentage>winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name


    # To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)    