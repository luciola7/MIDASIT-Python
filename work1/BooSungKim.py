
# coding: utf-8

# In[1]:

# ls


# In[20]:

import os
py_path = os.path.dirname(os.path.abspath(__file__))

input_file = py_path + "/nameslist.txt"

dict = {}
with open(input_file, "r") as f:
    names = f.readlines()
    
    for name in names:
        name = name.replace('\n', '')
        
        if dict.get(name, 0) == 0:
            dict[name] = 1
        else:
            dict[name] += 1


# In[21]:

dict
print(dict)


# In[22]:

# ls


# In[28]:

# Extra Work
input_file = py_path + "/Training_01.txt"
category_dict = {}
with open(input_file, "r") as f:
    filenames = f.readlines()
    
    for filename in filenames:
        category = filename.split('/')[2]
        
        if category_dict.get(category) is None:
            category_dict[category] = 1
        else:
            category_dict[category] += 1

category_dict
print(category_dict)

# In[ ]:



