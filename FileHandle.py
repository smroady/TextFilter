import os
import sys
import fileinput

def take_file_input(filepath):
    try:
        with open(filepath, 'r') as f:
            content = f.readline()
            return content
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"Error: '{e}'")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        # Format is: scriptname metadata1.txt data1.txt
        metadata = sys.argv[1]
        data = sys.argv[2]
        metaDataContent = take_file_input(metadata)
        dataContent = take_file_input(data)
    else :
        print("Use format {python scriptname <filepath/metadata.txt> <filepath/data.txt>")
        print("Example: python script.py meta.txt data.txt")


