

from collections import Counter, OrderedDict
import plotly as py
import plotly.graph_objs as go
from colourGen import *
import sys
from getCsvData import getData

VALUES = 20

def main():

    # Return array string of words
    words = getData('csvData/askScience.csv')

    # create dictionary of counted words
    wordCount = Counter(words)
    # new dictionary of top most common values
    wordCountTop = dict(wordCount.most_common(VALUES))
    # sorted Dictionary
    sortedList = OrderedDict(sorted(wordCountTop.items(), key=lambda t: t[1]))

    # create separate arrays of words/counts to feed into Plotly
    werds = []
    counts = []

    colours = colourGen(VALUES)

    for w in sortedList:
        werds.append(w)
        counts.append(sortedList.get(w))

    # flip to display graph in reverse order
    werds.reverse()
    counts.reverse()

    data = [go.Bar(
            x=counts,
            y=werds,
            orientation = 'h',
            marker=dict(
                color=colours,
            )
    )]

    layout = go.Layout(
            title='/r/AskScience Word Occurences in Comments - May 2015 (> 5 characters)',
            plot_bgcolor='rgba(240,240,240,1)',
            )

    fig = go.Figure(data=data, layout=layout)
    py.offline.plot(fig, filename='askScience.html')

    pass

if __name__ == '__main__':

    sys.exit(main())
