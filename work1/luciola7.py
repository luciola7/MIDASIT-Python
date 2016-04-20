"""luciola7 work1"""

READ_FILE_NAME = "nameslist.txt"

with open(READ_FILE_NAME) as f:
    NAME_LIST = f.readlines()
    NAME_COUNT = {}
    for name in NAME_LIST:
        if name[:-1] in NAME_COUNT:
            NAME_COUNT[name[:-1]] += 1
        else:
            NAME_COUNT[name[:-1]] = 1
    print(NAME_COUNT)
