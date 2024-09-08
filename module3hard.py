data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
    structure_sum = 0

    def extract(tap):
        nonlocal structure_sum
        if (isinstance(tap, list) or isinstance(tap, tuple)
                or isinstance(tap, set)):
            for i in tap:
                extract(i)
        elif isinstance(tap, dict):
            for value in tap.values():
                extract(value)
            for key in tap.keys():
                extract(key)
        elif isinstance(tap, int):
            structure_sum += tap
        elif isinstance(tap, str):
            structure_sum += len(tap)

    extract(args)
    return structure_sum

print(calculate_structure_sum(data_structure))






