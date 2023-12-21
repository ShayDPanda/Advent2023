import fileUtil as util


def arrayToInt(numArray):
    answer = 0

    for num in numArray:
        answer *= 10
        answer += int(num)

    return answer


def main():
    lines = util.openFile()

    maxY = len(lines)
    maxX = len(lines[0]) - 1  # New Line Character

    answer = 0
    for y in range(maxY):
        for x in range(maxX):
            if lines[y][x] == "*":
                numAdjacent = 0
                currentValue = 1
                currentNum = []

                # ===================== Left =====================
                if x > 0:
                    if lines[y][x - 1].isdigit():
                        numAdjacent += 1

                        thisX = x - 1

                        while thisX != -1 and lines[y][thisX].isdigit():
                            currentNum.insert(0, lines[y][thisX])
                            thisX -= 1

                        currentValue *= arrayToInt(currentNum)
                        currentNum = []

                # ===================== Right =====================
                if x < maxX:
                    if lines[y][x + 1].isdigit():
                        numAdjacent += 1

                        thisX = x + 1

                        while thisX < maxX + 1 and lines[y][thisX].isdigit():
                            currentNum.append(lines[y][thisX])
                            thisX += 1

                        currentValue *= arrayToInt(currentNum)
                        currentNum = []

                # ===================== Top =====================
                rowCheckBools = [0, 0, 0]

                if y > 0:
                    if x > 0:
                        if lines[y - 1][x - 1].isdigit():
                            rowCheckBools[0] = 1

                    if lines[y - 1][x].isdigit():
                        rowCheckBools[1] = 1

                    if x < maxX:
                        if lines[y - 1][x + 1].isdigit():
                            rowCheckBools[2] = 1

                    if rowCheckBools == [1, 0, 1]:
                        numAdjacent += 2

                        if numAdjacent == 2:
                            thisX = x - 1

                            while thisX != -1 and lines[y - 1][thisX].isdigit():
                                currentNum.insert(0, lines[y - 1][thisX])
                                thisX -= 1

                            currentValue *= arrayToInt(currentNum)
                            currentNum = []

                            thisX = x + 1

                            while thisX < maxX + 1 and lines[y - 1][thisX].isdigit():
                                currentNum.append(lines[y - 1][thisX])
                                thisX += 1

                            currentValue *= arrayToInt(currentNum)
                            currentNum = []

                    elif 1 in rowCheckBools:
                        numAdjacent += 1

                        if lines[y - 1][x].isdigit():
                            currentNum.append(lines[y - 1][x])

                        thisX = x - 1

                        while thisX != -1 and lines[y - 1][thisX].isdigit():
                            currentNum.insert(0, lines[y - 1][thisX])
                            thisX -= 1

                        thisX = x + 1

                        while thisX < maxX + 1 and lines[y - 1][thisX].isdigit():
                            currentNum.append(lines[y - 1][thisX])
                            thisX += 1

                        currentValue *= arrayToInt(currentNum)
                        currentNum = []

                # ===================== Bottom =====================
                rowCheckBools = [0, 0, 0]

                if y < maxY:
                    if x > 0:
                        if lines[y + 1][x - 1].isdigit():
                            rowCheckBools[0] = 1

                    if lines[y + 1][x].isdigit():
                        rowCheckBools[1] = 1

                    if x < maxX:
                        if lines[y + 1][x + 1].isdigit():
                            rowCheckBools[2] = 1

                    if rowCheckBools == [1, 0, 1]:
                        numAdjacent += 2

                        if numAdjacent == 2:
                            thisX = x - 1

                            while thisX != -1 and lines[y + 1][thisX].isdigit():
                                currentNum.insert(0, lines[y + 1][thisX])
                                thisX -= 1

                            currentValue *= arrayToInt(currentNum)
                            currentNum = []

                            thisX = x + 1

                            while thisX < maxX + 1 and lines[y + 1][thisX].isdigit():
                                currentNum.append(lines[y + 1][thisX])
                                thisX += 1

                            currentValue *= arrayToInt(currentNum)
                            currentNum = []

                    elif 1 in rowCheckBools:
                        numAdjacent += 1

                        if lines[y + 1][x].isdigit():
                            currentNum.append(lines[y + 1][x])

                        thisX = x - 1

                        while thisX != -1 and lines[y + 1][thisX].isdigit():
                            currentNum.insert(0, lines[y + 1][thisX])
                            thisX -= 1

                        thisX = x + 1

                        while thisX < maxX + 1 and lines[y + 1][thisX].isdigit():
                            currentNum.append(lines[y + 1][thisX])
                            thisX += 1

                        currentValue *= arrayToInt(currentNum)
                        currentNum = []

                # ===================== Answer =====================
                if numAdjacent == 2:
                    answer += currentValue

    print(answer)


if __name__ == "__main__":
    main()
