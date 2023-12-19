import fileUtil as util

numbers = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
    "1": 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "0" : 0
}

def main():
    lines = util.openFile()

    answer = 0

    for line in lines:
        first = 0
        last = 0
        # First number
        firstIndex = len(line) + 10
        for element in numbers:
            thisIndex = line.find(element)
            if thisIndex < firstIndex and thisIndex != -1:
                firstIndex = line.find(element)
                first = numbers[element]

        # Last number
        lastIndex = -1
        for element in numbers:
            thisIndex = line.rfind(element)
            if thisIndex > lastIndex and thisIndex != -1:
                lastIndex = thisIndex
                last = numbers[element]

        currentNumber = (10 * first) + last
        answer += currentNumber

    print(answer)


if __name__ == "__main__":
    main()

    # 54766