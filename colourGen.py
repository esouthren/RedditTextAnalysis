def colourGen(length):
    colours = []
    for i in range (0, length):
        if i % 2 == 0:
            colours.append("rgba(0,109,205,1)")
        else:
            colours.append("rgba(76,153,255,1)")
    return colours
