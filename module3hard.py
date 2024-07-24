def calculate_structure_sum(*args):
	summ_ = 0
	for i in args:
		if isinstance(i, int):
			summ_ = summ_ + i
		elif isinstance(i, str):
			summ_ = summ_ + len(i)
		elif isinstance(i, list):
			summ_ = summ_ + calculate_structure_sum(*i)
		elif isinstance(i, tuple):
			summ_ = summ_ + calculate_structure_sum(*i)
		elif isinstance(i, dict):
			for key, value in i.items():
				summ_ = summ_ + len(key)
				summ_ = summ_ + calculate_structure_sum(value)
		elif isinstance(i, set):
			summ_ = summ_ + calculate_structure_sum(*i)
	return summ_


data_structure = [
	[1, 2, 3],
	{'a': 4, 'b': 5},
	(6, {'cube': 7, 'drum': 8}),
	"Hello",
	((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
