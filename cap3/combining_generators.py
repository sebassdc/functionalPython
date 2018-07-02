
f = lambda x: x * x

# mode 1
g_f_x = (g(f(x)) for x in range())

#mode 2
g_f_x = (g(y) for y in (f(x) for x in range()))

#mode 3
f_x = (f(x) for x in range())
g_f_x = (g(y) for y in f_x)
