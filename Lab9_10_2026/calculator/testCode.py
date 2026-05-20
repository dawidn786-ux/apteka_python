## option 1
# import csv
# with open('customer.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)     # each line as dict
#     list_customer = list()
#     for row in csv_reader:
#         if row['ID'] != '204':
#             list_customer.append(row)
#
# csv_file.close()
# with open('customer.csv', mode='w') as csv_file:
#     fieldnames = ['ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     for row in list_customer:
#         writer.writerow(row)

import csv
with open('../../../../../../PycharmProjects/biblioteka/biblio/customer.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)     # each line as dict
    for row in csv_reader:
        if row['ID'] != '204':
            row.replece
