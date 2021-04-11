import sys
import getopt
import requests
import re
from bs4 import BeautifulSoup
from findFrequency import findFrequency, combine


def getContent(name):
    URL = "https://imsdb.com/scripts/" + name + ".html"
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
    stringData = stringData.replace("[", " ")
    stringData = stringData.replace("]", " ")
    stringData = stringData.replace("{", " ")
    stringData = stringData.replace("}", " ")
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
    setOutput = False
    outputfile = ''

    try:
        opts, args = getopt.getopt(argv, "hi:o:s:", ["ifile=", "ofile="])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print("Options and Arguments")
            print("\t-s [Movie Name]\t: Choose movie to examine the script of.")
            print(
                "\t-i\t\t: Specify input file. One movie title at the start of each line.")
            print("\t-o\t\t: Output file.")
            print("\t-h\t\t: Help section.")
            sys.exit()

        elif opt in ("-i", "--ifile"):
            inputfile = arg
            try:
                with open(arg, "r") as f:
                    for line in f:
                        sLine = line.strip()
                        inputData.append(setURL(sLine))
            except IOError:
                print("input file not ccessible")

        elif opt in ("-o", "--ofile"):
            outputfile = arg

            try:
                f = open(arg, "w+")
                f.close
                setOutput = True
            except IOError:
                print("unable to create output file")

        elif opt in ("-s", "--single"):
            print(str(sys.argv[2]))
            inputData.append(setURL(sys.argv[2]))

        else:
            assert False

    for i in range(len(inputData)):
        scriptData.append(cleanUpData(getContent(inputData[i])).split(" "))

    print(inputData)
    outPutStuffs = combine(scriptData, inputData)

    if(setOutput):
        outputData = open(outputfile, "w")
        outputData.writelines(str(outPutStuffs))
        outputData.close()


if __name__ == "__main__":
    main(sys.argv[1:])
