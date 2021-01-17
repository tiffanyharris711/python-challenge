import os
import csv

#set the initial values
count = 0 #count total number of rows to account for total votes
khan_votes = 0 
correy_votes = 0
li_votes = 0
otooley_votes = 0
max_vote = 0

csvpath = os.path.join('.','Resources','election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    csvheader = next(csvreader) #store header row and skip it for data counts

    for row in csvreader:
        count += 1  #number of rows after the header
        if row[2] == "Khan": #this if stmt adds the number of votes by candidate
            khan_votes += 1
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "Li":
            li_votes += 1
        elif row[2] == "O'Tooley":
            otooley_votes += 1
        if khan_votes > max_vote: #this if stmt compares the different vote counts to determine the max and declare the winner
            max_vote = khan_votes
            winner = "Khan"
            if correy_votes > max_vote:
                max_vote = correy_votes
                winner = "Correy"
                if li_votes > max_vote:
                    max_vote = li_votes
                    winner = "Li"
                    if otooley_votes > max_vote:
                        max_vote = otooley_votes
                        winner = "O'Tooley"
    #print results to terminal
    print("Election Results")
    print("--------------------")  
    print("Total Votes: " + str(count)) #use str to concatenate a number with a string
    print("--------------------")  
    print("Khan Votes: " + str(round(int(khan_votes)/int(count)*100,3)) + "%  (" + str(khan_votes)+")")
    print("Correy Votes: " + str(round(int(correy_votes)/int(count)*100,3)) + "%  (" + str(correy_votes)+")")
    print("Li Votes: " + str(round(int(li_votes)/int(count)*100,3)) + "%  (" + str(li_votes)+")")
    print("O'Tooley Votes: " + str(round(int(otooley_votes)/int(count)*100,3)) + "%  (" + str(otooley_votes)+")")
    print("--------------------")  
    print("Winner: " + winner)
    print("--------------------")  

#the following code is writes the financial analysis out to a text file
save_path = "./analysis/" #save the file in the analysis folder
file_name = ("PyPoll_Analysis.txt") #name of the new file
completeName = os.path.join(save_path,file_name) #us os module to adjust for oper system
f = open(completeName,"w") #specify w to write the file

#this code writes the lines to the text files
#the \n creates new line feeds
f.write("Election Results\n")
f.write("--------------------\n") #use \n to create a new line on the text file
f.write("Total Votes: " + str(count) +"\n")
f.write("--------------------\n")
f.write("Khan Votes: " + str(round(int(khan_votes)/int(count)*100,3)) + "%  (" +
    str(khan_votes) + ")\n")
f.write("Correy Votes: " + str(round(int(correy_votes)/int(count)*100,3)) + "%  (" + str(correy_votes)+")\n")
f.write("Li Votes: " + str(round(int(li_votes)/int(count)*100,3)) + "%  (" + str(li_votes)+")\n")
f.write("O'Tooley Votes: " + str(round(int(otooley_votes)/int(count)*100,3)) + "%  (" + str(otooley_votes) + ")\n")
f.write("--------------------\n")
f.write("Winner: " + winner + "\n")
f.write("--------------------\n")
f.close() #close the file after finished writing
