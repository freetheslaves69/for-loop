colorlist = []
repeat = "Y"
while repeat == "Y":
    color = input("enter a color: ")
    colorlist.append(color)
    repeat = input ("do you want to add another color?(Y/N)")
print(colorlist)