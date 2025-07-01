import os
import sys
import fileinput


#takes file path, opens file at that location, removes \n
def take_file_input(filepath):
    try:
        with open(filepath, 'r') as f:
            contents = []
            for lines in f:
                row = lines.strip()
                row = splitValues(row)
                contents.append(row)
            return contents
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"Error: '{e}'")

def splitValues(contents):
    line = contents.split("\t")
    return line

def fileExcluder(metaDataContent):
    try:
        filterdata = ""
        valuepairs = {}
        while filterdata != 113:
            print("Attributes are: " + str(metaDataContent[0]))
            filterdata = input("Enter an attribute you would like to filter for or q to exit: "
                               "Enter a value between 0 and " + str(metaDataContent[0].__len__() - 1) + ": ")
            temp = ord(filterdata)
            if temp == 113:
                break
            else:
                colAtt = int(filterdata)
            print("Filtering for : " + metaDataContent[0][colAtt])
            print("Enter items you would like to exclude, enter q when done: ")
            inclusionArray = []
            item = ""
            while item != "q":
                item = input("Enter a value or q: ")
                if item != "q":
                    inclusionArray.append(item)
                print(item + " entered")
            valuepairs[colAtt] = inclusionArray
            inclusionArray = []
        return valuepairs
    except Exception as e:
        print(f"Error: '{e}'")

def parseFile(valuePair, file):
    newFile = []
    flag = 0
    for i in file:
        for key in valuePair:
            if file[i][key] in valuePair[key]:
                flag = 1
        if flag != 1:
            newFile.append(file[i])
        flag = 0
    return newFile

if __name__ == "__main__":
    if len(sys.argv) == 3:
        # Format is: scriptname metadata1.txt data1.txt
        metadata = sys.argv[1]
        data = sys.argv[2]
        directory = os.getcwd() + "\\input" + "\\"
        metaDataContent = take_file_input(directory + metadata)
        dataContent = take_file_input(directory + data)

        metaDataValue = fileExcluder(metaDataContent)
        dataValue = fileExcluder(dataContent)

        filteredMetaData = parseFile(metaDataValue, metaDataValue[1:])
        filteredData = parseFile(dataContent, dataContent[1:])



    else :
        print(os.getcwd())
        print("Use format {python scriptname <filepath/metadata.txt> <filepath/data.txt>")
        print("Example: python script.py meta.txt data.txt")

