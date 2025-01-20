def cm_to_feet(cm,meters):
    inches = (cm/2.54)
    feet = meters /(2.54*12)
    return inches + feet



x=cm_to_feet(75,100)
print(x)