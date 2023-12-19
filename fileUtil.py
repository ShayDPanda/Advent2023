def openFile():
    try:
        file = open("input.txt", 'r')
        lines = file.readlines()
        file.close()
        return lines
    except:
        print("File Not Found")
        exit(-1)

def validRange(value, maximum):
    if value < 0:
        return 0
    elif value >= maximum:
        return maximum - 1
