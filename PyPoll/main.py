import os
import csv

csv_path = os.path.join('../..', 'UCIRV201807DATA4-Class-Repository-DATA/02-Homework/03-Python/'
                                 'Instructions/PyPoll/Resources/election_data.csv')

with open(csv_path, newline='', encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    next(csv_reader)

    voter_ID_list = []
    county_list = []
    candidate_list = []

    for row in csv_reader:
        voter_ID_list.append(row[0])
        county_list.append(row[1])
        candidate_list.append(row[2])

total_votes = len(voter_ID_list)

khan_votes = candidate_list.count('Khan')
khan_percent = khan_votes/total_votes

correy_votes = candidate_list.count('Correy')
correy_percent = correy_votes/total_votes

li_votes = candidate_list.count('Li')
li_percent = li_votes/total_votes

otooley_votes = candidate_list.count("O'Tooley")
otooley_percent = otooley_votes/total_votes

if khan_votes > correy_votes and li_votes and otooley_votes:
    winner = 'Khan'
elif correy_votes > khan_votes and li_votes and otooley_votes:
    winner = 'Correy'
elif li_votes > khan_votes and correy_votes and otooley_votes:
    winner = 'Li'
elif otooley_votes > khan_votes and correy_votes and li_votes:
    winner = "O'Tooley"

print('Election Results')
print('-------------------------')
print(f'Total Votes: {len(voter_ID_list)}')
print('-------------------------')
print(f'Khan: {khan_percent:.3%} ({khan_votes})')
print(f'Correy: {correy_percent:.3%} ({correy_votes})')
print(f'Li: {li_percent:.3%} ({li_votes})')
print(f"O'Tooley: {otooley_percent:.3%} ({otooley_votes})")
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')
