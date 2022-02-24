#!/usr/bin/env python
# coding: utf-8

# In[6]:


#1
x = input()

w = ""
for i in x:
	w = i + w

if (x == w):
	print("Yes,palindrome mun")
else:
	print("No,palendrome bish")


# In[28]:


#2
x = input()
lower_count = sum(map(str.islower, x))
upper_count = sum(map(str.isupper, x))
print("Jijig useg:",lower_count, "Tom useg:",upper_count)


# In[37]:


#3
def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x
    return result
list1 = [1, 2, 3]
print("Urjweriin utga",multiplyList(list1))


# In[50]:


#4
x = int(input())+1
t=1
for j in range(1,x):
    t = t * j
print('Bacterial utga',t)


# In[45]:


#5
systems = ['Bold', 'Bat', 'Ganaa']
print('Anhnii utga:', systems)

systems.reverse()

print('Esreg utga:', systems)


# In[43]:


#6
total = 0
list1 = [11, 5, 17, 18, 23]

for ele in range(0, len(list1)):
    total = total + list1[ele]
 
print("Buh elementiin niilber: ", total)


# In[39]:


#7
mylist = ["a", "b", "a", "c", "c","1","2","1"]
mylist = list(dict.fromkeys(mylist))
print(mylist)


# In[46]:


#8
list = [1,2,3,100,4,5]

biggest = max(list)

print(biggest)

