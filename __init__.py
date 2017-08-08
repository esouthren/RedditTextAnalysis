
import csv 
from collections import Counter, OrderedDict
import operator
import plotly as py
import plotly.graph_objs as go
from colourGen import *



count = 0
words = ''
VALUES = 20
text = csv.reader(open('csvData/askScienceSmall.csv', 'r'))

for row in text:    
    words += row[1]
    count+=1
    
words = words.split(' ') 
wordsStripped = []

for w in words:
    if len(w) > 5 and len(w) < 20:
        wordsStripped.append(w)
    
# create dictionary of counted values
wordCount = Counter(wordsStripped)

# new dictionary of top 10 most common values
wordCountTop = dict(wordCount.most_common(VALUES))
# sorted Dictionary
sortedList = OrderedDict(sorted(wordCountTop.items(), key=lambda t: t[1]))

#print sortedList
werds = []
counts = []

colours = colourGen(VALUES)        

for w in sortedList:
    werds.append(w)
    counts.append(sortedList.get(w))
    
werds.reverse()
counts.reverse()
    
#print wordCountTop, "\n\n"    
#print sortedWords

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


'''
# matplotlib (import matplotlib.pyplot as plt)

plt.rcdefaults()
fig, ax = plt.subplots()
y_pos = np.arange(len(werds))
ax.barh(y_pos, counts, align='center',
        color='blue', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(werds)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Count')
ax.set_ylabel('Word')
ax.set_title('/r/AskScience: Word Occurences in Comments')

plt.show()
'''
