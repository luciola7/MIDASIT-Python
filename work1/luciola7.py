"""luciola7 work1"""
import os
py_path = os.path.dirname(os.path.abspath(__file__))

input_file = py_path + "/nameslist.txt"

with open(input_file) as f:
    NAME_LIST = f.readlines()
    NAME_COUNT = {}
    for name in NAME_LIST:
        if name[:-1] in NAME_COUNT:
            NAME_COUNT[name[:-1]] += 1
        else:
            NAME_COUNT[name[:-1]] = 1
    print(NAME_COUNT)
