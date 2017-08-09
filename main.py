from collections import Counter, OrderedDict
import sys
from getCsvData import getData
from plot import plot
import os

def main():

    print("###################")
    print("Welcome to Plottit! ")
    print("###################\n")

    files = os.listdir("csvData/")
    del files[0]

    userChoice = -1

    while True:
        i = 1
        for f in range(0, len(files)):

            print i, ": ", files[f]
            i += 1
        try:
            userChoice = int(raw_input("\nPlease select a file (by index number)\n"))
        except ValueError:
            print("Whole number please!\n")

        if userChoice not in range(1, len(files)+1):
            print("Try again - pick a number in the list")
            continue
        else:
            break

    # align user choice to array index
    userChoice -= 1
    print "\nYou selected:"
    print files[userChoice]

    minLength = 0
    while True:

        try:
            minLength = int(raw_input("\nMinimum character length (recommended: 5)\n"))
        except ValueError:
            print("Whole number please!\n")

        if minLength not in range(1, 50):
            print("Try again - between 1 and 50 please")
            continue
        else:
            break

    # Return array string of words
    words = getData("csvData/" + files[userChoice], minLength)
    # create dictionary of counted words
    wordCount = Counter(words)

    values = 0
    while True:

        try:
            values = int(raw_input("\nNumber of top values to display (1-25)\n"))
        except ValueError:
            print("Whole number please!\n")

        if (values not in range(1,26)):
            print("Between 1 and 25 please")
            continue
        else:
             break

    print("\nProcessing... Enjoy!")

    wordCountTop = dict(wordCount.most_common(values))
    # sorted Dictionary
    sortedList = OrderedDict(sorted(wordCountTop.items(), key=lambda t: t[1]))
    for i in sortedList:
        print i, ": ", sortedList[i]

    titleStripped = files[userChoice].strip('.csv')
    titleStripped = titleStripped.split('_', 1)[-1]

    title = "Most Common Words in /r/" + titleStripped
    plot(sortedList, 'h', title)

if __name__ == '__main__':

    sys.exit(main())




