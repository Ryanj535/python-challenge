import csv
import os

candidates = []
dic = {}
vote = 0
percentvote = 0


count = 0
csvpath = os.path.join("election_data.csv")

with open(csvpath, newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)
    for row in csvreader:
        count = count + 1
        #Making a list of candidates
        if row[2] not in candidates:
            candidates.append(row[2])
        #Calculating the total number of candidates
        numcandidates = len(candidates)
        #for candidate in candidates:
            #dic[candidate] = list((candidate, int(vote), int(percentvote)))

    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {count}')
    print("-------------------------")
    #print(f')
