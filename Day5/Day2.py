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

    sortedData = []
    for obj in data:
        if sortedData:
            index = 0
            while index < len(sortedData) and obj[0] > sortedData[index][0]:
                index += 1

            sortedData.insert(index, obj)
        else:
            sortedData.append(obj)

    return sortedData


def inRange(targetMin, targetMax, currentMin, currentMax):
    # Smaller than object
    if currentMax < targetMin:
        return []

    # Includes the minimum but not the max
    if currentMin < targetMin < currentMax < targetMax:
        return (
            [currentMin, targetMin - 1],
            [targetMin, currentMax],
            [currentMax + 1, targetMax],
        )

    # Includes the max but not the minimum
    if targetMin < currentMin < targetMax < currentMax:
        return (
            [targetMin, currentMin - 1],
            [currentMin, targetMax],
            [targetMax + 1, currentMax],
        )

    # Target includes all of current
    if targetMin < currentMin and currentMax < targetMax:
        return (
            [targetMin, currentMin - 1],
            [currentMin, currentMax],
            [currentMax + 1, targetMax],
        )

    # Target is within current
    if currentMin < targetMin and targetMax < currentMax:
        return (
            [currentMin, targetMin - 1],
            [targetMin, targetMax],
            [targetMax + 1, currentMax],
        )

    return [currentMin, currentMax]


def inRange_SourceToDest(currentSet, targetSet):
    # Dest Source Range
    print("This Set", currentSet, end=" Size: ")
    print(len(currentSet))
    if len(currentSet) == 1:
        return inRange(
            targetSet[0], targetSet[0] + targetSet[2], currentSet[0], currentSet[1]
        )
    return inRange(
        targetSet[0],
        targetSet[0] + targetSet[2],
        currentSet[1],
        currentSet[1] + currentSet[2],
    )


def inRange_DestToSource(currentSet, targetSet):
    # Dest Source Range
    if len(currentSet) == 1:
        return inRange(
            targetSet[1], targetSet[1] + targetSet[2], currentSet[0], currentSet[1]
        )
    return inRange(
        targetSet[1],
        targetSet[1] + targetSet[2],
        currentSet[0],
        currentSet[0] + currentSet[2],
    )


def checkData(dataSet, currentSet):
    for info in dataSet:
        print("CheckData: ", currentSet, info)
        values = inRange_SourceToDest(currentSet, info)
        if values != -1:
            print("Values:", values)
            return values


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

    # DEST LOCAL -> Source Humid -> Dest Humid -> Source Light

    validSeeds = []
    answer = 0

    for objHL in humidLoca:
        humidLocaRange = checkData(tempHumid, objHL)

        for objLT in humidLocaRange:
            tempHumidRange = checkData(lightTemp, objLT)

            for objHR in tempHumidRange:
                tempWaterLight = checkData(waterLight, objHR)

                for objWL in tempWaterLight:
                    tempFertWater = checkData(fertWater, objWL)

                    for objFW in tempFertWater:
                        tempSoilFert = checkData(soilFert, objFW)

                        for objSS in tempSoilFert:
                            tempSoilSeeds = checkData(seedSoil, objSS)

                            for objSeeds in tempSoilSeeds:
                                validSeeds.append(objSeeds)
                                if validSeeds:
                                    print("Seeds: ", validSeeds)
                                    return


if __name__ == "__main__":
    main()
