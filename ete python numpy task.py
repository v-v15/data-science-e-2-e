#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Create a 1D array of numbers from 0 to 9.
import numpy as np
v = np.arange(10)
v


# In[3]:


#2. Create a 3×3 numpy array of all True’s
v1=np.ones((3, 3), dtype=bool)
v1


# In[29]:


#3. Given an array as input, print only odd numbers as output
import math
for a in v:
    if (a%2)==1:
        print(a)


# In[28]:


#4. Replace all odd numbers in arr with -2
for a in v:
    if (a%2)==0:
        print(-2)
    else:
        print(a)


# In[30]:


#5. How to reshape an array?


# In[35]:


#6. Convert a 1D array to a 2D array with 2 rows
v2=np.reshape(v, (2, -1))
v2


# In[36]:


#7.Given an array  a  = [1,2,3,4,5,6,7,8,9] , create  new array b from a such that b includes all odd numbers and 4 multiples. 
a  = [1,2,3,4,5,6,7,8,9]
b = []
for a in a:
    if a%2 == 1 or a/4==0:
        b.append(a)
b


# In[23]:


#8. Given array, check if there are any null values and print them out.
va = pd.Series([1, np.nan, 'hello', None])
va[va.isnull()]


# In[34]:


#9.How to replace all missing values with 0 in a numpy array?
va.fillna(0)


# In[38]:


#10.How to find the count of each unique number in a NumPy array
vu = np.array([1,11,1,1,11])
uniqueValues, occurCount = np.unique(vu, return_counts=True)
uniqueValues, occurCount


# In[7]:


#11.How to convert a numeric to a categorical (text) array?
import pandas as pd
import numpy as np
a=np.array([10,11])
a.astype(str)


# In[65]:


#12. Write a program to print all numbers between 99 and 299 which are either divisible by 5 or 7. Exclude the elements which are divisible by both.
for a in range(99,299,1):
    if (a%7==0 or a%5==0) and a%35!=0:
            print(a)


# In[44]:


#13. Write a program to reverse an array and print (Don’t use inbuilt reverse functions)
a  = [1,2,3,4,5,6,7,8,9]
b = []
for a in range(len(a),0,-1):
    b.append(a)
b


# In[ ]:




