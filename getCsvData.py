import csv

# Strip data from a CSV File

def getData(url):

    text = csv.reader(open(url, 'r'))

    # Return text from column [1] ('Comments')
    words = ''
    for row in text:
        words += row[1]

    words = words.split(' ')

    # Reject words under 5 characters, URLS, or containing odd characters
    wordsStripped = []
    for w in words:
        if len(w) > 5 and not w.startswith('http') and '_' not in w:
            wordsStripped.append(w)

    return wordsStripped