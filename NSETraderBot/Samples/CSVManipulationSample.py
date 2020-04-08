import csv


with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_csv_names.csv', 'w') as new_csv_file:
        fieldnames = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_csv_file,fieldnames= fieldnames,delimiter='\t')
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)


# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     # next(csv_reader)
# # ['first_name', 'last_name', 'email']
#
#     with open('new_csv_names.csv', 'w') as new_csv_file:
#         csv_writer = csv.writer(new_csv_file,delimiter='\t')
#         for line in csv_reader:
#             csv_writer.writerow(line)
