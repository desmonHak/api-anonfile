from subprocess import getstatusoutput

def func(fileNumber):
    for c in range(0, int(fileNumber)):
        file = str(input("archivo numero "+str(c)+" que subir: "))
        list.append(str(file))

    for filecreate in list:

        response = getstatusoutput("curl -F \"file=@"+str(filecreate)+"\" https://api.anonfile.com/upload")[1]
        print(str(response))

list = []

fileNumber = str(input("introduce la cantidad de archivo a subir: "))

if fileNumber == 1:
    fileNumber = fileNumber + 2
    func(fileNumber)
else:
    func(fileNumber)
