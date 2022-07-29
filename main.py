import csv 

data_1 = []
data_2 = []

with open('archive_dataset.csv', 'r') as f:
    reader = csv.reader(f)

    for row in reader:
        data_1.append(row)

with open('dataset_1.csv', 'r') as f:
    reader = csv.reader(f)
    
    for row in reader:
        data_2.append(row)

headers_1 = data_1[0] 
planet_data_1 = data_1[1:]

headers_2 = data_2[0]
planet_data_2 = data_2[1:]

headers = headers_1 + headers_2

planet_data = []

for index, data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index] + planet_data_2[index])

with open('final.csv', 'a+') as f:
    writer = csv.writer(f)
    writer = writerow(headers)
    writer = writerows(planet_data)