# generate alternating colours for bars

def colourGen(length):
    colours = []
    for i in range (0, length):
        if i % 2 == 0:
            colours.append("rgba(255,69,0,1)")
        else:
            colours.append("rgba(206,227,248,1)")
    return colours
