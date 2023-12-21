import fileUtil as util


def arrayToInt(numArray):
    answer = 0

    for num in numArray:
        answer *= 10
        answer += int(num)

    return answer


def checkSymbol(currentBool, obj):
    if not obj.isdigit() and obj != ".":
        return True

    if currentBool:
        return True

    return False


def main():
    lines = util.openFile()

    maxY = len(lines)
    maxX = len(lines[0]) - 1  # New Line Character

    answer = 0

    for y in range(maxY):
        currentNumber = []
        valid = False

        for x in range(maxX):
            if lines[y][x].isdigit():
                # New Number (currentNumber returns true if not empty)

                # Check Left
                if not currentNumber and x != 0:
                    valid = checkSymbol(valid, lines[y][x - 1])

                    if y != 0 and not valid:
                        valid = checkSymbol(valid, lines[y - 1][x - 1])

                    if y < maxY - 1 and not valid:
                        valid = checkSymbol(valid, lines[y + 1][x - 1])

                # Check above and below
                if not valid:
                    if y != 0:
                        valid = checkSymbol(valid, lines[y - 1][x])

                    if y < maxY - 1:
                        valid = checkSymbol(valid, lines[y + 1][x])

                # Append Value
                currentNumber.append(lines[y][x])

            # Ongoing number ends
            elif currentNumber:
                # Check right
                valid = checkSymbol(valid, lines[y][x])

                if y != 0 and not valid:
                    valid = checkSymbol(valid, lines[y - 1][x])

                if y < maxY - 1 and not valid:
                    valid = checkSymbol(valid, lines[y + 1][x])

                if valid:
                    answer += arrayToInt(currentNumber)

                # Clear Values
                valid = False
                currentNumber = []

        # End of Row
        if currentNumber and valid:
            answer += arrayToInt(currentNumber)

    print(answer)


if __name__ == "__main__":
    main()
