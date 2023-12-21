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


def checkRange(obj, start, thisRange):
    if start <= obj <= start + thisRange:
        return True
    else:
        return False


def checkData(dataSet, currentValue):
    for info in dataSet:
        if checkRange(currentValue, info[1], info[2]):
            return info[0] + (currentValue - info[1])

    return currentValue


def main():
    lines = util.openFile()

    seedsLine = lines[0].split()[1:]
    seeds = []
    for obj in seedsLine:
        seeds.append(int(obj))

    # SOURCE-TO-DESTINATION
    # DESTINATION # SOURCE # RANGE

    seedSoil = getData(lines, SEED_SOIL_START)
    soilFert = getData(lines, SOIL_FERT_START)
    fertWater = getData(lines, FERT_WATER_START)
    waterLight = getData(lines, WATER_LIGHT_START)
    lightTemp = getData(lines, LIGHT_TEMP_START)
    tempHumid = getData(lines, TEMP_HUMID_START)
    humidLoca = getData(lines, HUMID_LOCA_START)

    finalValues = []
    for seed in seeds:
        currentValue = checkData(seedSoil, seed)
        currentValue = checkData(soilFert, currentValue)
        currentValue = checkData(fertWater, currentValue)
        currentValue = checkData(waterLight, currentValue)
        currentValue = checkData(lightTemp, currentValue)
        currentValue = checkData(tempHumid, currentValue)
        currentValue = checkData(humidLoca, currentValue)
        finalValues.append(currentValue)

    print(min(finalValues))


if __name__ == "__main__":
    main()
