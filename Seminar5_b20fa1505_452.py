#!/usr/bin/env python
# coding: utf-8

# In[9]:


x = 6
for i in range(x):
    for j in range(i+1):
        print('*', end='')
    print()


# In[21]:


x = 6
for i in range(x):
    for j in range(i,x):
        print('*', end='')
    print()


# In[14]:


dict = {'Bat':18,'Oyu':22, 'Dulam':21, 'Suren':21}
maxkey = max(dict, key=dict.get)
minkey = min(dict, key=dict.get)
print(maxkey, minkey)


# In[22]:


for i in range(1, 1000):
    if((i%3==0) | (i%7==0)):
      print(i)


# In[ ]:





# In[ ]:





# In[ ]:




