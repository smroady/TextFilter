import os
import sys
import fileinput

def take_file_input(filepath):
    try:
        with open(filepath, 'r') as f:
            content = f.readlines()
            content = [line.strip() for line in content]
            return content
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"Error: '{e}'")

def splitValues(contents):
    line = contents.split("\t")
    return line

if __name__ == "__main__":
    if len(sys.argv) == 3:
        # Format is: scriptname metadata1.txt data1.txt
        metadata = sys.argv[1]
        data = sys.argv[2]
        directory = os.getcwd() + "\\input" + "\\"
        metaDataContent = take_file_input(directory + metadata)
        dataContent = take_file_input(directory + data)

        firstLineMeta = splitValues(metaDataContent[0])
        firstLineData = splitValues(dataContent[0])
        print(firstLineMeta)
        print(firstLineData)
        try:
            filterData = input("Enter an attribute you would like to filter for: "
                               "Enter a value between 0 and " + str(firstLineMeta.__len__() - 1) + ": ")
            colLocation = int(filterData)
            print("Filtering for " + firstLineMeta[colLocation])
        except Exception as e:
            print(f"Error: '{e}'")

    else :
        print(os.getcwd())
        print("Use format {python scriptname <filepath/metadata.txt> <filepath/data.txt>")
        print("Example: python script.py meta.txt data.txt")

