import re
import requests
import csv

urls = []
EXCLUSIONS = ['id', 'media', 'font', 'type', 'web' ] #CSS/JS reserved keywords to be excluded 

# Read urls from urls.csv and saving as url list
with open('urls.csv', newline='') as csvfile:
    urlReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in urlReader:
        urls.append(''.join(row))

def findHandles(text):
    #A regex expression to find handles
    handles = re.findall('(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)', text)
    return cleanHandles(handles)

def cleanHandles(handles):
    cleanedHandles = set(handles) #Remove duplicates and sort alphabetically
    for exclusion in EXCLUSIONS:
        if exclusion in cleanedHandles:
            cleanedHandles.remove(exclusion)
    return sorted(cleanedHandles)

def getHandlesforURL(url):
    r = requests.get(url)
    text = r.text
    return findHandles(text)

def getAllHandles():
    response = {}
    for url in urls:
        response[url] = getHandlesforURL(url)
    return response

# Print all handles
allHandles = getAllHandles()
print(allHandles)