import fileUtil as util


def points(score):
    if score == 0:
        return 1
    else:
        return score * 2


def main():
    lines = util.openFile()

    answer = 0
    for line in lines:
        line = line.split()

        currentPoints = 0
        winningLines = line[2:12]
        givenNums = line[13:]

        for obj in givenNums:
            if obj in winningLines:
                currentPoints = points(currentPoints)

        answer += currentPoints

    print(answer)


if __name__ == "__main__":
    main()
