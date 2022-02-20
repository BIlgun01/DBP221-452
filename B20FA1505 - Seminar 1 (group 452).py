#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1
list1=['python', 'php', 'java']
print(list1[0])
print(list1[1])
print(list1[2])


# In[3]:


# 2
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
e=0
t=0
while(e<len(list)):
    t=t+list[e]
    e+=1
print(t) 


# In[4]:


#3
def multiplyList(list) :
    t=1
    for x in list:
         t = t * x
    return t
list=[1, 2, 3, 4, 5]
print(multiplyList(list))


# In[5]:


#4
list=[1, 2, 3, 4, 5]
print(list[2]*list[-1])


# In[6]:


#6
def match_words(words):
  
  c = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      c += 1
  return c
 
print(match_words(['abca', 'ss','dgaga','a', 'aba', '1221']))


# In[12]:


#7
list3 = ['abdba', 'abcd', '121', '121', 'abcd']
x = set(list3)
y = list(x)
print(y)


# In[13]:


#8
list = []
if len(list):
	print('The list is not empty')
else:
	print('The list is empty')


# In[14]:


#9
list4=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
del list4[3]
del list4[4]
del list4[5]
print(list4)


# In[15]:


#10
mytuple = (12, 34, 56, 78, 56)
print ("anhnii tuple:",mytuple)
#11
x = list(mytuple)
q= int(input("Toogoo oruulana uu:= "))
x.append(q)
mytuple=tuple(x)
print("Shine tuple:",mytuple)
#12
second_element = mytuple[1]
isecon_element = mytuple[-2]
print("2doh bolon suuleesee 2 dah element:",second_element, isecon_element)
#13
a = int(input("Tuple-s haih toogoo oruulna uu:= "))
for y in mytuple:
    if a in mytuple:
        print("Garaas ogson too baina")
        break
    else:
        print("Bhq bna")
        break


# In[16]:


#14
e=0
tuple1=(1,2,3,4,5,6,7,8,9,10)
for e in tuple1:
    print(e)


# In[17]:


#15
set1={'1','2','3','4','5'}
set2={'6','7','8','9','10'}
set3=set.union(set1, set2)
print(set3)


# In[18]:


#16
set1={'1','2','3','4','5'}
set2={'6','7','3','2','1'}
k = set(set1)
i = k.intersection(set2)
t = set(i)
print(t)


# In[19]:


#17
set1={'1','2','3','4','5'}
print(len(set1))


# In[20]:


#18
set1 = {1,2,3,4,5,6,7,8,9,0}
set2 = {2,4,6,8,0}
set1 = set1.difference(set2)
print(set1)


# In[28]:


#19
set1={'1','2','3','4','5'}
set1.clear()
print(set1)
#20
del set1


# In[37]:




#22
d = {"key1": 10, "key2": 23}

if "key2" in d:
    print("yes")
else:
    print("no")



#23
dict1={'1':'10','2':'20','3':'30'}
if '20' in dict1.values():
    print('20 is in dictionary')
else:
    print("No")

# 24
dict1={'1':'10','2':'20','3':'30'}
for x in dict1:
  print(x, dict1[x])


#25
def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res
dict1={'1':'10','2':'20','3':'30'}
dict2={'a':'11','b':'22','c':'33'}
dict3 = Merge(dict1, dict2)
print(dict3)


#26

dict1 ={'1':10,'2':20,'3':30}
v = dict1.values()
t = sum(v)
print(t)
 


# In[ ]:




