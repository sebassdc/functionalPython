#  {1}
# writing pure functions

def some_function(a, b, t): #! bad design
    return a + b * t + global_adjustment


def open(iname, oname): #! bad design
    global ifile, ofile
    ifile = open(iname, "r")
    ofile = open(oname, "w")
