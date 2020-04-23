#!/usr/bin/env python
# coding: utf-8

# In[69]:


#Assignment on Pandas
import pandas as pd
import sqlite3


# In[70]:


#1. Create a Datatime index containing all the weekdays days of year 2019 and assign a random number to each of them in a dataframe. 
v = pd.date_range('2020-01-31', '2020-02-08', freq='D').to_series()
v.dt.dayofweek


# In[71]:


#2. Given Pandas series , height = [23,42,55] and weight = [71,32,48] . Create a dataframe with height and weight as column names. 
height = [23,42,55]
weight = [71,32,48] 
v_scale = pd.DataFrame({'height': height,'weight':weight })
v_scale


# In[72]:


#3. How to get the items of series A not present in series B .From ser1 remove items present in ser2.
ser1=pd.Series([2,3,4,5])
ser2=pd.Series([5,6,7,8])
ser1[~ser1.isin(ser2)]


# In[97]:


#Questions on Titanic Dataset :-
#4. Compute the minimum, 25th percentile, median, 75th, and maximum of age in titanic dataset
import numpy as np
ttnc_ds=pd.read_csv(r'C:\Users\vaibh\Downloads\ete spreadsheet\titanic_test (1).csv')
print(np.percentile(ttnc_ds.Age.head(), q=[0, 25, 50, 75, 100]))
ttnc_sl_age_ds=ttnc_ds[['Age']]
print(np.percentile(ttnc_sl_age_ds, q=[0, 25, 50, 75, 100]))
print(np.percentile(ttnc_sl_age_ds.fillna(0), q=[0, 25, 50, 75, 100]))
#print(ttnc_sl_age_ds.fillna(0))
#ttnc_sl_age_ds


# In[106]:


#5. How to get frequency counts of unique items of a series? Calculate the frequency counts of ‘SibSp’ column in titanic Dataset
#ttnc_ds.SibSp.head().value_counts()
ttnc_ds['SibSp'].value_counts()


# In[153]:


#6. Keep only top 2 most frequent values as it is and replace everything else as ‘Other’ in ‘Embarked’ column of titanic dataset
#ttnc_ds['Embarked'].value_counts()
a=ttnc_ds['Embarked']
a[~a.isin(a.value_counts().index[2:])] = 'Other'
a.value_counts()


# In[133]:


#7.Bin the price column in titanic data set into 5 equal groups and get counts of each bin
ttnc_ds.head()
Fmax=max(ttnc_ds.Fare)
Fmax
f1=Fmax*0.2;f2=f1+f1;f3=f2+f1;f4=f3+f1;f5=Fmax
f1,f2,f3,f4,f5
ttnc_ds['Fare_bins'] = pd.cut(ttnc_ds.Fare,bins=[f1,f2,f3,f4,f5],labels=['0.2f','0.4f','0.6f','0.8f'])
ttnc_ds.head()


# In[134]:


#8.Count the number of missing values in each column?
ttnc_ds.isnull().sum()


# In[141]:


#9. Get the row number of the 5th largest value in the Age column of titanic dataset?
ttnc_ds.nlargest(5, ['Age']).iloc[[-1]]


# In[186]:


#10.Normalize all columns in a dataframe?
normalized_ttnc_ds=(ttnc_ds-ttnc_ds.mean())/ttnc_ds.std()


# In[185]:


#11.Get the indices of items of ser2 in ser1 as a list.
ser1 = pd.Series([10,9,6,5,3,1,12,8,13])
ser2 = pd.Series([1,3,10,13])
for index in ser2:
    #print(ser1.values[index])
    print(ser1.values[ser2.index[index]])


# # 12. How to convert a series of date-strings to a timeseries?
# (['01 jan 2010','02-02-2011'.'2013/04/04','2014-05-05','2015-05-06T12:20'])
# 

# In[48]:


v_dts=pd.Series(['01 jan 2010','02-02-2011','2013/04/04','2014-05-05','2015-05-06T12:20'])
v_dts1=pd.to_datetime(v_dts)
v_dts1


# In[52]:


#13. Get the day of month, week number, day of year and day of week from ser.
ser=pd.Series(['01 jan 2010','01-01-2011','20120303','2013/04/04','2014-05-05','2015-06-06T12:20'])
ser1=pd.to_datetime(ser)
print(ser1)
print("Day of month:")
print(ser1.dt.day.tolist())
print("Week number:")
print(ser1.dt.weekofyear.tolist())
print("Day of year:")
print(ser1.dt.dayofyear.tolist())
print("Day of week:")
print(ser1.dt.weekday_name.tolist())


# In[41]:


#14. Compute the euclidean distance between series (points) p and q, without using a packaged formula.
import numpy as np
import pandas as pd
p = pd.Series([1,2,3,4,5,6,7,8,9,10])
q = pd.Series([10,9,8,7,6,5,4,3,2,1])
a=np.linalg.norm(p-q)
a


# In[40]:


import numpy as np
import pandas as pd
import math
p = pd.Series([1,2,3,4,5,6,7,8,9,10])
q = pd.Series([10,9,8,7,6,5,4,3,2,1])
a1=distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(p, q)]))
a1


# In[61]:


#15. How to create a TimeSeries starting ‘2000-01-01’ and 10 weekends (saturdays/sundays)
v_dti = pd.date_range('2000-01-01', periods=10, freq='w')
v_dti


# In[62]:


#16. Import every 50th row of BostonHousing dataset as a dataframe.
bstn_ds=pd.read_csv(r'C:\Users\vaibh\Downloads\ete spreadsheet\boston_house_price.csv')
bstn_ds[::50]


# In[ ]:




