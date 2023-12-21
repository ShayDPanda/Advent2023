import fileUtil as util

SEED_SOIL_START = 3
SOIL_FERT_START = 37
FERT_WATER_START = 68
WATER_LIGHT_START = 105
LIGHT_TEMP_START = 132
TEMP_HUMID_START = 148
HUMID_LOCA_START = 182


def getData(lines, index):
    data = []
    while lines[index] != "\n":
        thisLine = lines[index].split()
        data.append([int(thisLine[0]), int(thisLine[1]), int(thisLine[2])])
        index += 1

    return data


def checkData(dataSet, currentValue):
    for info in dataSet:
        if info[1] <= currentValue <= info[1] + info[2]:
            return info[0] + (currentValue - info[1])

    return currentValue


def main():
    lines = util.openFile()

    seedsLine = lines[0].split()[1:]
    seeds = []
    for obj in seedsLine:
        seeds.append(int(obj))

    seedRange = []
    for obj in range(0, len(seeds), 2):
        seedRange.append([seeds[obj], seeds[obj + 1] + seeds[obj]])

    seedRange.sort()

    seedSoil = getData(lines, SEED_SOIL_START)
    soilFert = getData(lines, SOIL_FERT_START)
    fertWater = getData(lines, FERT_WATER_START)
    waterLight = getData(lines, WATER_LIGHT_START)
    lightTemp = getData(lines, LIGHT_TEMP_START)
    tempHumid = getData(lines, TEMP_HUMID_START)
    humidLoca = getData(lines, HUMID_LOCA_START)

    finalValues = ""
    for x in seedRange:
        for y in range(x[0], x[1] + 1):
            currentValue = checkData(seedSoil, y)
            currentValue = checkData(soilFert, currentValue)
            currentValue = checkData(fertWater, currentValue)
            currentValue = checkData(waterLight, currentValue)
            currentValue = checkData(lightTemp, currentValue)
            currentValue = checkData(tempHumid, currentValue)
            currentValue = checkData(humidLoca, currentValue)
            if finalValues:
                finalValues = min(currentValue, finalValues)
            else:
                finalValues = currentValue

    print(finalValues)

    output = open("output.txt", "w")
    output.write(str(finalValues))
    output.close()


if __name__ == "__main__":
    main()
