import fileUtil as util
def main():
    lines = util.openFile()

    answer = 0

    for line in lines:
        line = line.split(" ")
        red = 0
        green = 0
        blue = 0
        for colorIndex in range(3, len(line) + 1, 2):
            if line[colorIndex][0] == "r":
                if int(line[colorIndex - 1]) > red:
                    red = int(line[colorIndex - 1])
            elif line[colorIndex][0] == "b":
                if int(line[colorIndex - 1]) > blue:
                    blue = int(line[colorIndex - 1])
            elif line[colorIndex][0] == "g":
                if int(line[colorIndex - 1]) > green:
                    green = int(line[colorIndex - 1])

        answer += (red * green * blue)

    print(answer)

if __name__ == "__main__":
    main()