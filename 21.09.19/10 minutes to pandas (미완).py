#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 10 minutes to pandas


# In[1]:


import numpy as np

import pandas as pd


# In[ ]:


Object creation


# In[3]:


s = pd.Series([1, 3, 5, np.nan, 6, 8])


# In[4]:


s


# In[5]:


dates = pd.date_range("20130101", periods=6)


# In[6]:


dates


# In[7]:


df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))


# In[8]:


df


# In[9]:


df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)


# In[10]:


df2


# In[14]:


df2.<TAB>  # noqa: E225, E999
df2.A                  df2.bool
df2.abs                df2.boxplot
df2.add                df2.C
df2.add_prefix         df2.clip
df2.add_suffix         df2.columns
df2.align              df2.copy
df2.all                df2.count
df2.any                df2.combine
df2.append             df2.D
df2.apply              df2.describe
df2.applymap           df2.diff
df2.B                  df2.duplicated


# In[ ]:


Viewing data


# In[15]:


df.head()


# In[16]:


df.tail(3)


# In[17]:


df.index


# In[18]:


df.columns


# In[19]:


df.to_numpy()


# In[20]:


df2.to_numpy()


# In[ ]:


# DataFrame.to_numpy() does not include the index or column labels in the output.


# In[ ]:


# describe() shows a quick statistic summary of your data:


# In[21]:


df.describe()


# In[23]:


# Transposing your data:

df.T


# In[24]:


# Sorting by an axis:

df.sort_index(axis=1, ascending=False)


# In[25]:


# Sorting by values:

df.sort_values(by="B")


# In[ ]:


# Getting


# In[26]:


df["A"]


# In[27]:


# Selecting via [], which slices the rows.

df[0:3]


# In[28]:


df["20130102":"20130104"]


# In[ ]:


# Selection by label


# In[29]:


# For getting a cross section using a label:

df.loc[dates[0]]


# In[30]:


# Selecting on a multi-axis by label:

df.loc[:, ["A", "B"]]


# In[31]:


# Showing label slicing, both endpoints are included:

df.loc["20130102":"20130104", ["A", "B"]]


# In[32]:


# Reduction in the dimensions of the returned object:

df.loc["20130102", ["A", "B"]]


# In[33]:


# For getting a scalar value:

df.loc[dates[0], "A"]


# In[34]:


# For getting fast access to a scalar (equivalent to the prior method):

df.at[dates[0], "A"]


# In[ ]:


# Selection by position


# In[35]:


# Select via the position of the passed integers:

df.iloc[3]


# In[36]:


# By integer slices, acting similar to NumPy/Python:

df.iloc[3:5, 0:2]


# In[ ]:


# By lists of integer position locations, similar to the NumPy/Python style:


# In[37]:


# By lists of integer position locations, similar to the NumPy/Python style:

df.iloc[[1, 2, 4], [0, 2]]


# In[38]:


# For slicing rows explicitly:

df.iloc[1:3, :]


# In[39]:


# For slicing columns explicitly:

df.iloc[:, 1:3]


# In[ ]:


# For getting a value explicitly:


# In[40]:


df.iloc[1, 1]


# In[ ]:


# For getting fast access to a scalar (equivalent to the prior method):


# In[41]:


df.iat[1, 1]


# In[ ]:


# Boolean indexing


# In[42]:


# Using a single column’s values to select data.

df[df["A"] > 0]


# In[ ]:


# Selecting values from a DataFrame where a boolean condition is met.


# In[43]:


df[df > 0]


# In[44]:


# Using the isin() method for filtering:

df2 = df.copy()

df2["E"] = ["one", "one", "two", "three", "four", "three"]

df2


# In[45]:


df2[df2["E"].isin(["two", "four"])]


# In[ ]:


# Setting


# In[46]:


# Setting a new column automatically aligns the data by the indexes.

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))


# In[47]:


s1


# In[48]:


df["F"] = s1


# In[ ]:


# Setting values by label:


# In[49]:


df.at[dates[0], "A"] = 0


# In[ ]:


# Setting values by position:


# In[50]:


df.iat[0, 1] = 0


# In[ ]:


# Setting by assigning with a NumPy array:


# In[51]:


df.loc[:, "D"] = np.array([5] * len(df))


# In[ ]:


# The result of the prior setting operations.


# In[52]:


df


# In[ ]:


# A where operation with setting.


# In[53]:


df2 = df.copy()

df2[df2 > 0] = -df2

df2


# In[ ]:


# Missing data


# In[54]:


df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])


# In[55]:


df1.loc[dates[0] : dates[1], "E"] = 1

df1


# In[56]:


# To drop any rows that have missing data.

df1.dropna(how="any")


# In[57]:


# Filling missing data.

df1.fillna(value=5)


# In[58]:


# To get the boolean mask where values are nan.

pd.isna(df1)


# In[ ]:


추가 : https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html

