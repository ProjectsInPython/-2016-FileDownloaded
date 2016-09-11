import webbrowser
import os
import time
preLink = 'http://midi-files-for-free.biz/MIDI/'
pathToSoundNames = r'D:\Scripts\OpenLinkInBrowser\All Files.txt'
pathToDownloadFiles = r'D:\Scripts\OpenLinkInBrowser\DownloadedSounds'

def deleteEndLines(soundNames):
    allSoundNamesWithoutNewLines = []
    for soundName in soundNames:
        allSoundNamesWithoutNewLines.append(soundName[0:len(soundName)-1])
    return allSoundNamesWithoutNewLines

def downloadSoundsFromList(soundNamesLines):
    rangeStart = 0
    rangeEnd = 100
    while rangeEnd < len(soundNamesLines)+100:
        for soundName in soundNamesLines[rangeStart: rangeEnd]:
            webbrowser.open(preLink + soundName)

        print str(rangeStart) + ',' + str(rangeEnd)
        time.sleep(12)
        rangeStart += 101
        rangeEnd += 100

soundNames = deleteEndLines(open(pathToSoundNames, 'r').readlines())
downloadSoundsFromList(soundNames)
time.sleep(12)
subtractFromSourceAndDestiny = list(set(soundNames) - set(os.listdir(pathToDownloadFiles)))

if subtractFromSourceAndDestiny:
    downloadSoundsFromList(subtractFromSourceAndDestiny)
