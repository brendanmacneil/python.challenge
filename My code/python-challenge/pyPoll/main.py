#Import file
import os, csv
from pathlib import Path 

#Assign file local with pathlib library
csv_file_path = Path("python-challenge", "PyPoll", "election_data.csv")

#Variables needed
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#Open csv in default read mode with context manager
with open(csv_file_path,newline="", encoding="utf-8") as elections:

    #Store data under the csvreader variable
    csvreader = csv.reader(elections,delimiter=",") 

    #Skip header as it is not needed for the values
    header = next(csvreader)     

    #Go through each row in the csv
    for row in csvreader: 

        #Count unique Voter ID's and store in variable "total_votes"
        total_votes +=1

        #There are four candidates, if the name is found, count the times it shows up in the given data set
        #Use values in our percent vote calculation found in the print statements
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

 #In order To find the winner, a dictionary needs to be made out of the two lists that were previously created 
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

#Tie them together the list of candidate(key) and the total votes(value)
#Bring back the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

#Print out a the summary
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

#Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

#Output files and assign output file location and with pathlib
output_file = Path("python-challenge", "PyPoll", "Election_Results_Summary.txt")

with open(output_file,"w") as file:

#Write methods to print to Elections_Results_Summary 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")
