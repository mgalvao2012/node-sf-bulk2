import csv

header = ['Name', 'Description']
i = 0
data = []
while i < 1000000:
    data.append(['Account-v2-'+str(i).zfill(7), 'Account generated automatically-v2-'+str(i).zfill(7)])
    i += 1

with open('GeneratedAccounts.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)
