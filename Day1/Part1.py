import fileUtil as util

def main():
    lines = util.openFile()

    answer = 0

    for line in lines:
        thisLine = []
        for obj in line:
            if obj.isdigit():
                thisLine.append(int(obj))

        currentNumber = (10 * thisLine[0]) + thisLine[-1]
        answer += currentNumber

    print(answer)


if __name__ == "__main__":
    main()