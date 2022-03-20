# =====================================
# =====================================
# =====================================
# Function to grab all lines from text file, and remove any line with any numbers
def removeLinesWithNumbers():
    # Gather the directory holding this file
    import os
    localDirectory = os.path.dirname(os.path.realpath(__file__))
    # Add file name to the directory
    # Need an extra backslash to indicate the second is just part of the string and not a \n   etc.
    fileName = "10000passwords.txt"
    fileAddress = (localDirectory + "\\" + fileName)

    # Open file, read each line into an array
    f = open(fileAddress, 'r')
    fileContents = f.readlines()
    for line in range(len(fileContents)):  # 10001
        # Array elements have newline at end. Strip that off each.
        fileContents[line] = fileContents[line].rstrip()

    cleanArray = []  # To hold lines with no numbers
    for line in range(len(fileContents)):  # 10001
        # Don't hit end of array
        if line == len(fileContents) - 1:
            break
        # If number is found break, may be int or str. Or else add line to new array
        for char in (fileContents[line]):
            if char.isdigit():
                break
            elif any(char.isdigit() for char in fileContents[line]):
                break
            else:
                cleanArray.append(fileContents[line])
                print(fileContents[line])
                break

    # Create new file, and allow write to file
    f = open("10000passwordsNoNumbers.txt", "w")
    for x in range(len(cleanArray)):
        f.write(cleanArray[x])
        f.write("\n")
    return cleanArray
    #print(cleanArray)
# =====================================
# =====================================
# =====================================

# Main section to call the function in to
if __name__ == '__main__':

    # -----------------------------------
    # Call Functions
    removeLinesWithNumbers()
    # -----------------------------------
