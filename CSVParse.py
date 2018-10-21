import csv
import math
import pygame
import sys
# takes a wave absolute row and gives accumulates the values and counts


def addabsolute(row):
    count = 0
    res = 0
    for i in range(2, 6):
        if row[i] != "nan" or row[i] != "0":
            count += 1
            res += float(row[i])
    return res, count;

# Resets the dictionary for next segment


def resetWavesDict():
    return {" /muse/elements/alpha_absolute": (0, 0),
            " /muse/elements/beta_absolute": (0, 0),
            " /muse/elements/gamma_absolute": (0, 0),
            " /muse/elements/experimental/concentration": (0, 0)}

# calculates the wave data and puts it into a list


def calculatewaves(wavesDict):
    listres = []
    for key in wavesDict.keys():
        listres.append(float(wavesDict[key][0]) / (float(wavesDict[key][1]) + 1.0))
    return listres


def rateWaves(lower, upper, compare):
    waveNames = ["alpha", "beta", "gamma", "concentration"]
    waveRatings = [None] * 4
    flipped = False
    for i in range(0, 4):
        if lower[i] > upper[i]:
            flipped = True
            temp = lower[i]
            lower[i] = upper[i]
            upper[i] = temp
            waveRatings[i] = 0.0
        if compare[i] <= lower[i]:
            print(waveNames[i] + ": very relaxing")
            if flipped is False:
                waveRatings[i] = 0.0
            if flipped is True:
                waveRatings[i] = 10.0
        elif compare[i] >= upper[i]:
            print(waveNames[i] + ": not relaxing")
            if flipped is False:
                waveRatings[i] = 10.0
            if flipped is True:
                waveRatings[i] = 0.0
        else:
            print(i)
            print(upper[i])
            if flipped is False:
                waveRatings[i] = ((float(compare[i]) - float(lower[i])) * 10.0) / (float(upper[i]) - float(lower[i]))
            if flipped is True:
                waveRatings[i] = 10 - ((float(compare[i]) - float(lower[i])) * 10.0) / (float(upper[i]) - float(lower[i]))

    return waveRatings


if __name__ == '__main__':
    f = open("C:/Users/binph/Downloads/recording_8.csv", 'rt');
    reader = csv.reader(f)
    firstrow = next(reader)
    count = 0
    wavesDict = {" /muse/elements/alpha_absolute": (0, 0),
                 " /muse/elements/beta_absolute": (0, 0),
                 " /muse/elements/gamma_absolute": (0, 0),
                 " /muse/elements/experimental/concentration": (0, 0)}
    amountofpics = 8
    timePer = 20
    starttime = int(math.floor(float(firstrow[0])))
    lasttime = starttime + timePer
    currentQuestion = 1
    resList = []

    for row in reader:
        if (int(math.floor(float(row[0]))) >= lasttime):
            starttime = lasttime
            lasttime = starttime + timePer
            newlist = calculatewaves(wavesDict)
            resList.append(newlist)
            wavesDict = resetWavesDict()
            currentQuestion += 1

        if (currentQuestion > amountofpics):
            break
        # tuple to carry values and count of a eeg
        currRes = (0, 0)
        if row[1] == " /muse/elements/alpha_absolute":
            # get values and count, update dictionary, and also the result page
            currRes = addabsolute(row)
            oldValues = wavesDict[row[1]]
            wavesDict[row[1]] = (oldValues[0] + currRes[0], oldValues[1] + currRes[1])
        if row[1] == " /muse/elements/beta_absolute":
            currRes = addabsolute(row)
            oldValues = wavesDict[row[1]]
            wavesDict[row[1]] = (oldValues[0] + currRes[0], oldValues[1] + currRes[1])
        if row[1] == " /muse/elements/gamma_absolute":
            currRes = addabsolute(row)
            oldValues = wavesDict[row[1]]
            wavesDict[row[1]] = (oldValues[0] + currRes[0], oldValues[1] + currRes[1])
        if row[1] == " /muse/elements/experimental/concentration":
            oldValues = wavesDict[row[1]]
            if row[1] != "nan":
                wavesDict[row[1]] = (oldValues[0] + float(row[2]), oldValues[1] + 1)

    print(len(resList))
    upperbound = resList[1]
    lowerbound = resList[3]
    compare = resList[5]
    compare2 = resList[7]
    print(resList)
    results = (rateWaves(lowerbound, upperbound, compare))
    results2 = (rateWaves(lowerbound, upperbound, compare2))
    #display results

    pygame.init()
    display_width = 800
    display_height = 600
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("hi")
    basicfont = pygame.font.SysFont(None, 40)
    crashed = False
    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            text = basicfont.render("Old Spice", True, (255, 255, 255), (0, 0, 0))
            textrect = text.get_rect()
            textrect.center = ((display_width / 2), (1 * display_height / 11))
            gameDisplay.blit(text, textrect)
            text = basicfont.render('Alpha:     ' + str(results[0]), True, (255, 255, 255), (0, 0, 0))
            textrect = text.get_rect()
            textrect.center = ((display_width / 2), (2 * display_height / 11))
            gameDisplay.blit(text, textrect)
            text2 = basicfont.render('Beta:     ' + str(results[1]), True, (255, 255, 255), (0, 0, 0))
            textrect2 = text.get_rect()
            textrect2.center = ((display_width / 2), (3*display_height / 11))
            gameDisplay.blit(text2, textrect2)
            text3 = basicfont.render('Gamma:     ' + str(results[2]), True, (255, 255, 255), (0, 0, 0))
            textrect3 = text3.get_rect()
            textrect3.center = ((display_width / 2), (4*display_height / 11))
            gameDisplay.blit(text3, textrect3)
            text4 = basicfont.render('Concentration:     ' + str(results[3]), True, (255, 255, 255), (0, 0, 0))
            textrect4 = text4.get_rect()
            textrect4.center = ((display_width / 2), (5*display_height / 11))
            gameDisplay.blit(text4, textrect4)
            ##########################################
            text = basicfont.render("Chevy", True, (255, 255, 255), (0, 0, 0))
            textrect = text.get_rect()
            textrect.center = ((display_width / 2), (6 * display_height / 11))
            gameDisplay.blit(text, textrect)

            text = basicfont.render('Alpha:     ' + str(results2[0]), True, (255, 255, 255), (0, 0, 0))
            textrect = text.get_rect()
            textrect.center = ((display_width / 2), (7*display_height / 11))
            gameDisplay.blit(text, textrect)
            text2 = basicfont.render('Beta:     ' + str(results2[1]), True, (255, 255, 255), (0, 0, 0))
            textrect2 = text.get_rect()
            textrect2.center = ((display_width / 2), (8 * display_height / 11))
            gameDisplay.blit(text2, textrect2)
            text3 = basicfont.render('Gamma:     ' + str(results2[2]), True, (255, 255, 255), (0, 0, 0))
            textrect3 = text3.get_rect()
            textrect3.center = ((display_width / 2), (9 * display_height / 11))
            gameDisplay.blit(text3, textrect3)
            text4 = basicfont.render('Concentration:     ' + str(results2[3]), True, (255, 255, 255), (0, 0, 0))
            textrect4 = text4.get_rect()
            textrect4.center = ((display_width / 2), (10 * display_height / 11))
            gameDisplay.blit(text4, textrect4)
            pygame.display.update()

    #f.close()
