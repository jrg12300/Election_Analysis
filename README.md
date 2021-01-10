# Election_Analysis

Project Overview:

  A Colorado Board of Elections gave the following tasks to complete the election audit of a recent local congressional election: 
  
  1) Calculate total number of votes
  2) Get a complete list of candidates who received votes
  3) Calculate the total number of votes each candidate received
  4) Determine the winner
  5) Get a complete list of counties that voted in this election
  6) Determine the vote split by county
  7) Determine which county had the most voters in this election
  
  Then, write a python script that prints all of this information in the terminal, as well as prints the information to a .txt file.
  
Resources:
  election_results.csv
  software: python 3.9

Results:
  1) 369,711 votes were cast
  2) The county vote distribution was Jefferson County 10.5% (38,855), Denver County 82.8% (306,055), Arapahoe County 6.7% (24,801)
  3) Denver County had the most votes
  4) Charles Casper Stockham recieved 23.0% (85,213) of the votes, Diana DeGette recieved 73.8% (272,892) of the votes, Raymon Anthony Doane recieved 3.1%       (11,606) of the votes
  5) Diana DeGette recieved 73.8% (272,892) of the votes making her the winner of the election
  6) Here is the summary of the results ![Election_Analysis](https://github.com/jrg12300/Election_Analysis/blob/main/Election_reults_terminal_picture.png)
  
Summary:
  
  This code is useful for auditing elections because it can be used in an election with any number of counties and any number of candidates. Given that the election is winner take all, and the candidate with the most votes is deemed the winner. Also, the .csv file needs to be in the same format as the election_results.csv. This script could be modified for future use in elections where a winner is only declared winner if they recieve 50% or more of the vote. An additional if statement could determine whether or not there needed to be a run-off.
