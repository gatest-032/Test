myfile = open("C:\\Users\\g679667\\OneDrive - General Mills\\My Folder\\Work Items\\Codes\\Test Files\\Names.txt", "r")
listName = []
for readline in myfile:
    listName.append(readline.replace("\n", ''))
myfile.close()

print(listName)

myfile = open("C:\\Users\\g679667\\OneDrive - General Mills\\My Folder\\Work Items\\Codes\\Test Files\\Test.txt", "r")
strRead = myfile.read()
myfile.close()

for name in listName:
    myOutFile = open("C:\\Users\\g679667\\OneDrive - General Mills\\My Folder\\Work Items\\Codes\\Test Files\\" + str(name) + ".html", "w")
    strNew = strRead.replace("`NAME", str(name))
    myOutFile.write(strNew)
    myOutFile.close()
