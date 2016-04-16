
# coding: utf-8

# In[1]:

ls


# In[20]:

dict = {}
with open("nameslist.txt", "r") as f:
    names = f.readlines()
    
    for name in names:
        name = name.replace('\n', '')
        
        if dict.get(name, 0) == 0:
            dict[name] = 1
        else:
            dict[name] += 1


# In[21]:

dict


# In[22]:

ls


# In[28]:

# Extra Work
category_dict = {}
with open("Training_01.txt", "r") as f:
    filenames = f.readlines()
    
    for filename in filenames:
        category = filename.split('/')[2]
        
        if category_dict.get(category) is None:
            category_dict[category] = 1
        else:
            category_dict[category] += 1


# In[ ]:



