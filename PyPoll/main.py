import os
import csv

#set the initial values
count = 0

csvpath = os.path.join('/Users','tiffanyharris','Desktop','git_things','myGitRepos','python-challenge','PyPoll','Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.DictReader(csvfile) #Use DictReader instead of reader to skip header
    for row in csvreader:
        count += 1  #number of rows after the header


print("Election Results")
print("--------------------")  
print("Total Votes: " + str(count))
print("--------------------")  