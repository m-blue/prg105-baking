# liter to fluid ounces
def convert(l):
    ounces = (float(l) * 34)
    return ounces

liters = raw_input("Type in the number of liters: ")
fl_ounces = convert(liters)
print (liters + " liters equals to " + str(fl_ounces) + " fluid ounces.")
