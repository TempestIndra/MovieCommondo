import sys
import getopt
import requests
import re
from bs4 import BeautifulSoup


def getContent(name):
    URL = "https://imsdb.com/scripts/" + setURL(name) + ".html"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find('pre')
    # try:
    # print(content)
    return content


def setURL(name):
    return name.replace(" ", "-")


def cleanUpData(data):
    stringData = str(data).lower()
    stringData = stringData.replace("<b>", " ")
    stringData = stringData.replace("</b>", " ")
    stringData = stringData.replace("<pre>", " ")
    stringData = stringData.replace("</pre>", " ")
    stringData = stringData.replace("?", " ")
    stringData = stringData.replace(".", " ")
    stringData = stringData.replace("-", " ")
    stringData = stringData.replace(",", " ")
    stringData = stringData.replace(":", " ")
    stringData = stringData.replace(")", " ")
    stringData = stringData.replace("(", " ")
    stringData = stringData.replace("'", " ")
    stringData = stringData.replace("\"", " ")
    stringData = stringData.replace("!", " ")
    stringData = stringData.replace(";", " ")
    stringData = stringData.split()
    for i in stringData:
        if(i.isdigit() == True):
            stringData.remove(i)
    return convertListToString(stringData)


def convertListToString(listData):
    rString = ""
    for ele in listData:
        rString += ele + " "
    return rString


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print("whenGet erroe sections")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("help section")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    data = cleanUpData(getContent(sys.argv[1]))
    print(data)


if __name__ == "__main__":
    main(sys.argv[1:])
