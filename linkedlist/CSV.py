

def openCSV(fileName):
    fileOpen=open(fileName,'r')
    i=0


    for line in fileOpen:
        print(line)