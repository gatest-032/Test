import csv

file_1 = open("C:/Users/g679667/OneDrive - General Mills/My Folder/Work Items/Codes/Test Files/Registration Details.csv")

csvreader = csv.reader(file_1)

header_1 = []
header_1 = next(csvreader)

header_1[0] = header_1[0].strip()

print(header_1)

list_1 = []
for readline in file_1:
    list_1.append(readline.split(','))

for item in list_1:
    item[-1] = item[-1].strip()

print(list_1)

file_1.close()


file_2 = open("C:/Users/g679667/OneDrive - General Mills/My Folder/Work Items/Codes/Test Files/Exam Results.csv")

csvreader = csv.reader(file_2)

header_2 = []
header_2 = next(csvreader)

header_2[0] = header_2[0].strip()

print(header_2)

list_2 = []
for readline in file_2:
    list_2.append(readline.split(','))

for item in list_2:
    item[-1] = item[-1].strip()

print(list_2)

file_2.close()

result_list_header = header_2 + [i for i in header_1 if i not in header_2]
print(result_list_header)

for l1 in list_1:
    for l2 in list_2:
        if(l1[0] == l2[0]):
            print('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(l2[0], l2[1], l2[2], l2[3], l2[4], l2[5], l2[6], l1[1], l1[2], l1[3], l1[4], l1[5], l1[6]))

