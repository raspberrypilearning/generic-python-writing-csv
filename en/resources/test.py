import csv
with open('some.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows([[i for i in range(10)] for i in range(5)])
