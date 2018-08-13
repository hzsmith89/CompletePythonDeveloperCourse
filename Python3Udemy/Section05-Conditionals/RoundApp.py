def Rounding(x):
    XRound = int(x)

    if x - XRound < 0.5:
        return XRound
    else:
        return XRound + 1


number = 3.49

print(Rounding(number))

