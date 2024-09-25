
with open("pitone.jpeg" , mode="rb")as file :
    fileContent = file.read()
print(fileContent[:100])