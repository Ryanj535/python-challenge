import csv
import os

candidates = []
poll = {}
votes = []
percentvote = []
winnerlist = []

count = 0
csvpath = os.path.join("election_data.csv")

with open(csvpath, newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)
    for row in csvreader:
        count = count + 1
        #Making a dictionary of candidats and votes
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1

    for key, value in poll.items():
        candidates.append(key)
        votes.append(value)

    for x in votes:
        percentvote.append(round(x/count*100,1))

    table = list(zip(candidates, votes, percentvote))

    for name in table:
        if max(votes) == name[1]:
            winnerlist.append(name[0])

    winner = winnerlist[0]

    if len(winnerlist) > 1:
        for w in range(1, len(winnerlist)):
            winner = winner + ", " + winnerlist[w]

    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {count}')
    print("-------------------------")
    print(f'{table[0][0]}: {table[0][2]}% ({table[0][1]})')
    print(f'{table[1][0]}: {table[1][2]}% ({table[1][1]})')
    print(f'{table[2][0]}: {table[2][2]}% ({table[2][1]})')
    print(f'{table[3][0]}: {table[3][2]}% ({table[3][1]})')
    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")

output_file = os.path.join('PyPoll_Results.txt')

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(count) +
      '\n-------------------------\n')
    for entry in table:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')
