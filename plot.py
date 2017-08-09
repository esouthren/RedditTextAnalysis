from colourGen import *
import plotly as py
import plotly.graph_objs as go

def plot(sortedList, orientation, title):

    werds = []
    counts = []

    colours = colourGen(len(sortedList))

    # create separate arrays of words/counts to feed into Plotly
    for w in sortedList:
        werds.append(w)
        counts.append(sortedList.get(w))

    # flip to display graph in reverse order
    werds.reverse()
    counts.reverse()

    data = [go.Bar(
        x=counts,
        y=werds,
        orientation=orientation,
        marker=dict(
            color=colours,
        )
    )]

    layout = go.Layout(
        title=title,

    )

    fig = go.Figure(data=data, layout=layout)
    py.offline.plot(fig, filename='askScience.html')
