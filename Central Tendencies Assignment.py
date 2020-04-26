#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy
#1. Find the mean of the following data using hand and compare with numpy.mean()
#a) 9, 7, 11, 13, 2, 4, 5, 5
a=[9, 7, 11, 13, 2, 4, 5, 5]
print(numpy.mean(a))


# In[9]:


#b) 2.2, 10.2, 14.7, 5.9, 4.9, 11.1, 10.5
print(numpy.mean([2.2, 10.2, 14.7, 5.9, 4.9, 11.1, 10.5]))


# In[10]:


#c) 11/4, 21/2, 51/2, 31/4, 21/2
print(numpy.mean([11/4, 21/2, 51/2, 31/4, 21/2]))


# In[20]:


#2. Find the mean of first 10 Fibonacci numbers (Use a for loop to create 10 Fibonacci series)
a=0
b=1
c=0
d=[]
for i in range(2,10): 
        c = a + b 
        a = b 
        b = c 
        d.append(c)
print(d)
print(numpy.mean(d))


# In[47]:


#3. Find the mean and median of first 5 prime numbers.
import statistics as st
c=[2,3,5,7,11]
print ("mean=",numpy.mean(c))
print ("median=",st.median(c))


# 4. The mean of 8, 11, 6, 14, x and 13 is 66. Find the value of the observation x.
# 
# formula => total/num = avg
# 
# (8+11+6+14+x+13)/6=66
# 
# x=396-(8+11+6+14+13)=344

# 5. The mean of 6, 8, x + 2, 10, 2x - 1, and 2 is 9. Find the value of x in the data.
# 
# (6+8+(x+2)+10+(2x-1)+2)/6=9
# 
# 2x+25=36
# 
# x=8

# 6. Find the mean of the following distribution.
# 
# a) The age of 20 boys in a locality is given below
# 
# ans>> (12*5+10*3+15*2+14*6+8*4)/20=11.8
# 
# b) Marks obtained by 40 students in an exam are given below
# 
# ans>> (25*8+30*12+15*10+20*6+24*4)/40=23.15

# 7. Find the mode of the following data
# 
# a) 12, 8, 4, 8, 1, 8, 9, 11, 9, 10, 12, 8
# 
# b) 15, 22, 17, 19, 22, 17, 29, 24, 17, 15
# 
# c) 0, 3, 2, 1, 3, 5, 4, 3, 42, 1, 2, 0
# 
# d) 1, 7, 2, 4, 5, 9, 8, 3
# 
# ans >> a= 8.5
# 
# b= 18
# 
# c= 2.5
# 
# d= 4.5

# 8. The following observations are arranged in ascending order. The median of the data is 25 . Find the value of x.
# 
# 17, x, 24, x+7, 35, 36, 46
# 
# ans >> x= 18

# 9. In the above problem, how would you approach the problem if the numbers are not in ascending order ? What are possible values of X then?
# 
# ans>> Median in case of odd no. of number is the middle value when arranzed in ascending order. Since this sequence is of odd number. So middle number is 25 and middle is x+7
#  x+7=25 ==> x=18

# 10. In which of these situations would you use the mode to measure the central tendency of the data.
# 
# a) Justin records the temperature at noon every day for two weeks and wants to know the temperature of a 'typical' day.
# 
# b) Would you use the mean in all of these situations?
# 
# c) Juliana measures the height of all the girls on her soccer team and wants to know the typical height of a soccer player.
# 
# d) Sam asks the students in her class to identify their favourite colour and wants to know which colour is the most common.
# 
# ans >> d
