#!/usr/local/bin/python3.7

from bs4 import BeautifulSoup
import requests
import pprint
import json

def main():
   scovList = getScovilleVal();

   pprint.pprint(json.dumps(scovList))

def getChilliScovilleValues():
   soup = loadPage();
   scovDict = extractScovilleVal(soup);

   return scovDict

def loadPage():

    url = "https://www.chilipeppermadness.com/chili-pepper-types/"
    url2 = "https://www.cayennediane.com/big-list-of-hot-peppers/"
    header = {'User-Agent' : 
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36' }

    r  = requests.get(url2,headers=header)
    soup = BeautifulSoup(r.text,"html.parser")
    return soup

def extractScovilleVal(soup):
    scovList = []  
    scovDict = {}
    for divBlock in soup.find_all("div",{"class":"et_pb_text_inner"}):
       subsoup = BeautifulSoup(str(divBlock), "html.parser")
       if isDataBlock(subsoup):
          chilli = subsoup.find_all("h3")[0].text
          scovNum = int(subsoup.find_all("b")[0].text.split(' ')[1])
          scovDict[chilli]=scovNum

    sortedScovDict = dict(sorted(scovDict.items()))

    for key in sortedScovDict: 
       scovList.append({ "name": key, "scoville" : sortedScovDict[key] })

    return scovList

def isDataBlock(subsoup):
    return ( (len(subsoup.find_all("b")) != 0) and (len(subsoup.find_all("h3")) != 0) )

if __name__ == "__main__":
    main();

