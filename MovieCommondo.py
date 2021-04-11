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
    try:
        if (str(content) == "<pre></pre>"):
            raise Exception("can't identify link")
        else:
            return content
    except Exception as e:
        print(str(e) + " "+name)


def setURL(name):
    rname = name.lower()
    rname = rname.split()
    for i in range(len(rname)):
        rname[i] = rname[i].capitalize()
    rname = convertListToString(rname)
    return rname.replace(" ", "-")[:-1]


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
    stringData = stringData.replace("&", " ")
    stringData = stringData.replace("#", " ")
    for i in range(0, 10):
        stringData = stringData.replace(str(i), " ")
    stringData = stringData.split()
    return convertListToString(stringData)


def convertListToString(listData):
    rString = ""
    for ele in listData:
        rString += ele + " "
    return rString


def main(argv):
    inputfile = ''
    inputData = []
    scriptData = []
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
            try:
                with open(arg, "r") as f:
                    for line in f:
                        sLine = line.strip()
                        inputData.append(setURL(sLine))
            except IOError:
                print("File not ccessible")

        elif opt in ("-o", "--ofile"):
            outputfile = arg
        else:
            inputData.append(sys.argv[1])
    for i in range(len(inputData)):
        scriptData.append(cleanUpData(getContent(inputData[i])))


if __name__ == "__main__":
    main(sys.argv[1:])
