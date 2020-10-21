import csv
l = dict()
with open('listname.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        l[row['name']]= 0

