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

