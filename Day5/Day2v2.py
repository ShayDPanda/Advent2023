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

    # DEST SOURCE RANGE -> [Dest Min, Dest Max][Source Min, Source Max]
    while lines[index] != "\n":
        thisLine = lines[index].split()
        data.append(
            [
                [thisLine[0], thisLine[0] + thisLine[2]],
                [thisLine[1], thisLine[1] + thisLine[2]],
            ]
        )

    sortedData = []
    for obj in data:
        if sortedData:
            index = 0
            while index < len(sortedData) and obj[0][0] > sortedData[index][0][0]:
                index += 1

            sortedData.insert(index, obj)
        else:
            sortedData.append(obj)

    return sortedData


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


if __name__ == "__main__":
    main()
