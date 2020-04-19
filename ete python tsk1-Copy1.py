#!/usr/bin/env python
# coding: utf-8

# In[1]:


#finding length of the string
import re
a=(" I am very keen in building up my career in Data Science, but not sure from where to start. If I search the web it throws me thousands of articles, few are relevant others make me confused, again I come around to the same page. Supervised has provided me a good platform to remove all such qualms which were wrangling in my mind")
b= len(a)
b


# In[3]:


#1.Consider the above text as a string, figure out the average length of the string.
c= a.split( )
d=sum(len(word) for word in c)/len(c)
d


# In[5]:


#2.Lower the text in the string.
e=a.lower()
e


# In[19]:


#3.Try to get the clean text removing the punctuation from the string.
#defining punctuation
punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
f=""
for char in a:
    if char not in punct:
        f=f+char
f


# In[ ]:





# In[86]:


#5.frequency of words in a string
g=c
h=[]
i=0
for word in c:
    i=0
    for word1 in g:
        if word==word1:
            i+=1
    if word not in h:
        h.append(word)
        print(word,i)


# In[89]:


#7.Find all the words which occurred more than once in the string.
h=[]
for word in c:
    i=0
    for word1 in g:
        if word==word1:
            i+=1
    if word not in h:
        h.append(word)
        if i>1:
            print(word,i)


# In[100]:


#8 Can you change the word "Supervised" to "Unsupervised" in the string
j=a
k=j.replace("Supervised","Unsupervised")
k


# In[107]:


#9 Splitting of the string with a dot operator(.)
l=j.split('.')
l


# In[172]:


#Find the words from the string which ends with "e"
j=a
revword=[]
    revword=words.reverse()
    if revword[0] in 'e':
        print(words)


# In[161]:


# Figure out number of a's used in the string.
p=a
count=0
i=0
for i in p:
    if i in'a':
        count+=1
count            


# In[2]:


#Questions on Dictionary
#In the weekend , I purchased 250g of apple, 500g of sugar, 2.5 kg of rice, 2.5 litres of milk and finally 1 dozen of egg.


# In[38]:


#Can you help me frame the above purchase in the form of dictionary with commodities as keys to it.
v_dict={".25":"apple",".5":"sugar","2.5":"rice","3.5":"milk","1":"egg"}
v_dict


# In[39]:


#I forgot to mention another item, 1kg of atta packet. Can you also add it ?
v_dict.update({"1":"potato"})
v_dict


# In[40]:


#Instead of 2kg of rice, I bought only 1kg of rice. Can you change the corresponding value ?
v_dict.pop("2.5")
v_dict.update({"1":"rice"})
v_dict


# In[41]:


#Can you list out all these items using a loop.
#for key in v_dict:
#    print v_dict[key]
#    
for key, value  in v_dict.items():
    print(key + " : " + str(value))


# In[42]:


#However, the cost of 1 kg apple is Rs.220, 1 kg of sugar is Rs.43, 1 Kg of rice is Rs. 45, 1 litre of milk is Rs.30 and 1 dozen of egg is Rs. 60.
v_pricing={"apple":"220","sugar":"43","rice":"43","milk":"30","egg":"60"}
v_pricing


# In[44]:


for key, value  in v_dict.items():
    for key, value  in v_pricing.items():
        if v_dict.value() == v_pricing.key[]
            sum+=v_pricing.value()*v_dict.key()


# In[8]:


#Sort the list in ascending order
AI_companies= ['Amazon','Facebook','Hisilicon','Google','Apple','Microsoft','Sensetime']
AI_companies


# In[9]:


#Sort the list in ascending order
AI_companies.sort()
AI_companies


# In[10]:


#Add multiple companies at once 'Nvidia', 'OpenAI' , 'Qualcomm' and 'Reliance' to the list
AI_companies.extend([ 'Nvidia', 'OpenAI' , 'Qualcomm' , 'Reliance'])
AI_companies


# In[27]:


#lower the list using List comprehension
AI_comp=[a for a in AI_companies]
AI_comp


# In[11]:


#Elimiate 'Reliance' from the list
AI_companies.remove('Reliance')
AI_companies


# In[25]:


#Extract 'Facebook', 'Google' and 'Microsoft' using a single command
AI_companies[2:6:1]


# # Questions on Tuple
# #(a)Consider the above standard price problem statement and place the prices in the form of the tuple.
# 

# In[36]:


tup1=(220,43,44,30,60)
tup1


# In[37]:


max(tup1)


# In[38]:


min(tup1)


# In[49]:


AI_companies2= ['Amazon','Facebook','Hisilicon','Google','Apple','Microsoft','Sensetime']
tup2=(AI_companies2)
tup2


# In[54]:


tup3 = tup1 + tup1
tup3


# In[61]:


len(tup2)


# In[62]:


len(tup3)


# In[ ]:




