from aocd import data, submit
from functools import reduce


subject_number = 7
public_keys = list(map(int, data.split("\n")))


transfrom_number = lambda input_num, subject_num: (input_num * subject_num) % 20201227


def loop_size (subject_number, public_key):
    key = loop_size = value = 1

    while True:
        value = transfrom_number(value, subject_number)
        if value == public_key: return loop_size
        loop_size += 1


loop_sizes = [loop_size(subject_number, key) for key in public_keys]
i = loop_sizes.index(min(loop_sizes))
value = 1

result = reduce(lambda n, _: transfrom_number(n, public_keys[not i]), range(loop_sizes[i]), 1)
print(result)
submit(result)

