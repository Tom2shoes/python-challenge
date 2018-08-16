import os
import csv

csv_path = os.path.join('../..', 'UCIRV201807DATA4-Class-Repository-DATA/02-Homework/03-Python/'
                                 'Instructions/PyBank/Resources/budget_data.csv')

with open(csv_path, newline='', encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # parse out header
    next(csv_reader)

    # add month-year column and profit/loss column into their own lists
    months_list = []
    change_list = []
    for row in csv_reader:
        months_list.append(row[0])
        change_list.append(int(row[1]))

total_net_amount = sum(i for i in change_list)

# profit change between months. Starting at index 1 to avoid using a negative index
monthly_change = [change_list[i] - change_list[i - 1] for i in range(1, len(change_list))]

average_change = round(sum(monthly_change)/(len(monthly_change)), 2)

# index of the max/min profit change
max_change = max(monthly_change)
min_change = min(monthly_change)
max_change_index = monthly_change.index(max_change)
min_change_index = monthly_change.index(min_change)

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {len(months_list)}')
print(f'Total: $ {total_net_amount}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits {months_list[max_change_index]} (${max_change})')
print(f'Greatest Decrease in Profits {months_list[min_change_index]} (${min_change})')

output_path = os.path.join('main.txt')

with open(output_path, 'w', newline='') as text_file:
    csv_writer = csv.writer(text_file)
    csv_writer.writerow('Financial Analysis')
    csv_writer.writerow('----------------------------')
    csv_writer.writerow(f'Total Months: {len(months_list)}')
    csv_writer.writerow()
    csv_writer.writerow()
