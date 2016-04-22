# skyi first work

textfile = open("namelist.txt",'r')
names = textfile.readlines()
namelist = dict()
for line in names:
    line = line.strip()
    # strip by removing '\n'
    #pos = line.find('\n')
    #if pos>0 :
    #    line=line[:pos]
    if line not in namelist:
        namelist[line]=1
    else:
        namelist[line]=namelist[line]+1
for k in namelist.keys() :
    print(" %s : %d" % (k,namelist[k]))
textfile.close()

# Next Problem
print("*" * 50)

# Extra
categorylist = {}
with open('Training_01.txt','r') as openfile:
    lines = openfile.readlines()
    for line in lines:
        category = line.split('/')[2]
        if category not in categorylist:
            categorylist[category]=1
        else:
            categorylist[category]=categorylist[category]+1
    for k in categorylist.keys():
        print(" %s : %d" % (k,categorylist[k]))


