'''
This script demonstrates a live data source by creating a csv and adding random data to it.
'''
import csv
import random
import time

x_value = 0
total_1 = 1000
total_2 = 1000

# give name to the columns
fieldnames = ["x_value", "total_1", "total_2"]

# This writes the column header into the data
with open('.\data09.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    
    with open('.\data09.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # create dictionary of the values
        info = {
            "x_value": x_value,
            "total_1": total_1,
            "total_2": total_2
        }

        # write the values as row
        csv_writer.writerow(info)
        print(x_value, total_1, total_2)

        # change the values randomly
        x_value += 1
        total_1 = total_1 + random.randint(-6, 8)
        total_2 = total_2 + random.randint(-5, 6)

    time.sleep(1)
