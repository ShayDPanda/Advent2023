import fileUtil as util

lines = util.openFile()


def checkCard(currentCard):
    cardInfo = lines[currentCard].split()
    winningLines = cardInfo[2:12]
    givenNums = cardInfo[13:]

    numMatches = 0
    for obj in givenNums:
        if obj in winningLines:
            numMatches += 1

    if numMatches == 0:
        return 1
    else:
        answer = 1
        for y in range(currentCard + 1, currentCard + 1 + numMatches):
            answer += checkCard(y)

        return answer


def main():
    answer = 0
    for y in range(len(lines)):
        answer += checkCard(y)

    print(answer)


if __name__ == "__main__":
    main()
