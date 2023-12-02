def openFile():
    try:
        file = open("input.txt", 'r')
        return file
    except:
        print("File Not Found")
        exit(-1)

