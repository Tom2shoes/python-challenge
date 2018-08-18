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
counter = {}

for candidate in candidate_list:
    if candidate in counter.keys():
        counter[candidate] += 1
    else:
        counter[candidate] = 1

print('Election Results')
print('-------------------------')
print(f'Total Votes: {len(voter_ID_list)}')
print('-------------------------')

for key, value in counter.items():
    print(f'{key}:', f'{value/total_votes:.3%}', f'({value})')

print('-------------------------')


winner = max(counter, key=counter.get)

print(f'Winner: {winner}')

print('-------------------------')

output_path = os.path.join('main.csv')

with open(output_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(['Election Results'])
    csv_writer.writerow(['-------------------------'])
    csv_writer.writerow(['Total Votes:', f'{len(voter_ID_list)}'])
    csv_writer.writerow(['-------------------------'])
    for key, value in counter.items():
        csv_writer.writerow([f'{key}:', f'{value/total_votes:.3%}', f'{value}'])
    csv_writer.writerow(['-------------------------'])
    csv_writer.writerow([f'Winner: {winner}'])
    csv_writer.writerow(['-------------------------'])
