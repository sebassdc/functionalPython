import csv
from collections import namedtuple

def row_iter(source):
	return csv.reader(source, delimiter="\t")


def head_split_fixed(row_iter):
	title = next(row_iter)
	assert len(title) == 1 and title[0] == "Anscombe's quartet"
	heading = next(row_iter)
	assert len(heading) == 4 and heading == ['I', 'II', 'III', 'IV']
	columns = next(row_iter)
	assert len(columns) == 8 and columns == ['x', 'y', 'x', 'y', 'x', 'y', 'x', 'y']
	return row_iter


Pair = namedtuple("Pair", ("x", "y"))
def series(n, row_iter):
	for row in row_iter:
		yield Pair(*row[n*2:n*2+2])


with open("Anscombe.txt") as source:
	data = head_split_fixed(row_iter(source))
	sample_I = tuple(series(0, data))
	sample_II = tuple(series(1, data))
	sample_III = tuple(series(2, data))
	sample_IV = tuple(series(3, data))


mean = sum(float(pair.y) for pair in sample_I) / len(sample_I)

for subset in sample_I, sample_II, sample_III, sample_IV:
	mean = sum(float(pair.y) for pair in sample_I) / len(sample_I)
	print(mean)
