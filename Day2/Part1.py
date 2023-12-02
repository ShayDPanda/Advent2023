import fileUtil as util
def main():
    file = util.openFile()
    lines = file.readlines()

    answer = 0
    for line in lines:
        line = line.split(" ")
        valid = True
        for colorIndex in range(3, len(line) + 1, 2):
            # Red
            if line[colorIndex][0] == "r":
                if int(line[colorIndex - 1]) > 12:
                    valid = False

            # Blue
            elif line[colorIndex][0] == "g":
                if int(line[colorIndex - 1]) > 13:
                    valid = False

            # Green
            elif line[colorIndex][0] == "b":
                if int(line[colorIndex - 1]) > 14:
                    valid = False

        if valid:
            gameID = int(line[1][:len(line[1])-1])
            answer += gameID

    print(answer)
    file.close()

if __name__ == "__main__":
    main()