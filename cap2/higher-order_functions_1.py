#  {1}
year_cheese = [
    (2000, 29.87), (2001, 30.12), (2002, 30.6), (2003,30.66),
    (2004, 31.33), (2005, 32.62), (2006, 32.73), (2007, 33.5),
    (2008, 32.84), (2009, 33.02), (2010, 32.92),
]

snd = lambda x: x[1]
maximun = snd(max(map(lambda yc: (yc[1], yc), year_cheese)))

print(maximun)
# inmutable data
