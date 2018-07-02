
#s = 0
#for n in range(1, 10):
#    if n % 3 == 0 or n % 5 == 0:
#        s += n
#print(s)

#m = list()
#for n in range(1, 10):
#    if n % 3 == 0 or n % 5 == 0:
#        m.append(n)
#print(sum(m))

class SummableList(list):

    def sum(self):
        s = 0
        for v in self.__iter__():
            s += v
        return s