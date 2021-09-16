#!/usr/bin/env python
# coding: utf-8

# In[1]:


# LMS 8번 노드


# In[2]:


# 간단한 막대 그래프 그리는 전체 코드

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# 그래프 데이터 
subject = ['English', 'Math', 'Korean', 'Science', 'Computer']
points = [40, 90, 50, 60, 100]

# 축 그리기
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

# 그래프 그리기
ax1.bar(subject, points)

# 라벨, 타이틀 달기
plt.xlabel('Subject')
plt.ylabel('Points')
plt.title("Yuna's Test Result")

# 보여주기
plt.savefig('./barplot.png')  # 그래프를 이미지로 출력
plt.show()                    # 그래프를 화면으로 출력


# In[4]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# 그래프 데이터 
subject = ['English', 'Math', 'Korean', 'Science', 'Computer']
points = [40, 90, 50, 60, 100]


# In[5]:


# 축 그리기
fig = plt.figure() #도화지(그래프) 객체 생성
ax1 = fig.add_subplot(1,1,1) #figure()객체에 add_subplot 메소드를 이용해 축을 그려준다.


# In[6]:


fig = plt.figure()


# In[7]:


fig =  plt.figure(figsize=(5,2))
ax1 = fig.add_subplot(1,1,1)


# In[8]:


fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,4)


# In[11]:


# 그래프 데이터 
subject = ['English', 'Math', 'Korean', 'Science', 'Computer']
points = [40, 90, 50, 60, 100]

# 축 그리기
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

# 그래프 그리기
ax1.bar(subject,points)


# In[12]:


# 그래프 데이터 
subject = ['English', 'Math', 'Korean', 'Science', 'Computer']
points = [40, 90, 50, 60, 100]

# 축 그리기
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

# 그래프 그리기
ax1.bar(subject, points)

# 라벨, 타이틀 달기
plt.xlabel('Subject')
plt.ylabel('Points')
plt.title("Yuna's Test Result")


# In[13]:


from datetime import datetime
import pandas as pd
import os

# 그래프 데이터 
csv_path = os.getenv("HOME") + "/aiffel/data_visualization/data/AMZN.csv"
data = pd.read_csv(csv_path ,index_col=0, parse_dates=True)
price = data['Close']

# 축 그리기 및 좌표축 설정
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
price.plot(ax=ax, style='black')
plt.ylim([1600,2200])
plt.xlim(['2019-05-01','2020-03-01'])

# 주석달기
important_data = [(datetime(2019, 6, 3), "Low Price"),(datetime(2020, 2, 19), "Peak Price")]
for d, label in important_data:
    ax.annotate(label, xy=(d, price.asof(d)+10), # 주석을 달 좌표(x,y)
                xytext=(d,price.asof(d)+100), # 주석 텍스트가 위차할 좌표(x,y)
                arrowprops=dict(facecolor='red')) # 화살표 추가 및 색 설정

# 그리드, 타이틀 달기
plt.grid()
ax.set_title('StockPrice')

# 보여주기
plt.show()


# In[14]:


# plt.plot()로 그래프 그리기

import numpy as np
x = np.linspace(0, 10, 100) #0에서 10까지 균등한 간격으로  100개의 숫자를 만들라는 뜻입니다.
plt.plot(x, np.sin(x),'o')
plt.plot(x, np.cos(x),'--', color='black') 
plt.show()


# In[15]:


x = np.linspace(0, 10, 100) 

plt.subplot(2,1,1)
plt.plot(x, np.sin(x),'orange','o')

plt.subplot(2,1,2)
plt.plot(x, np.cos(x), 'orange') 
plt.show()


# In[16]:


#linestyle, marker옵션

x = np.linspace(0, 10, 100) 

plt.plot(x, x + 0, linestyle='solid') 
plt.plot(x, x + 1, linestyle='dashed') 
plt.plot(x, x + 2, linestyle='dashdot') 
plt.plot(x, x + 3, linestyle='dotted')
plt.plot(x, x + 0, '-g') # solid green 
plt.plot(x, x + 1, '--c') # dashed cyan 
plt.plot(x, x + 2, '-.k') # dashdot black 
plt.plot(x, x + 3, ':r'); # dotted red
plt.plot(x, x + 4, linestyle='-') # solid 
plt.plot(x, x + 5, linestyle='--') # dashed 
plt.plot(x, x + 6, linestyle='-.') # dashdot 
plt.plot(x, x + 7, linestyle=':'); # dotted


# In[17]:


fig, axes = plt.subplots(2, 1)
data = pd.Series(np.random.rand(5), index=list('abcde'))
data.plot(kind='bar', ax=axes[0], color='blue', alpha=1)
data.plot(kind='barh', ax=axes[1], color='red', alpha=0.3)


# In[18]:


df = pd.DataFrame(np.random.rand(6,4), columns=pd.Index(['A','B','C','D']))
df.plot(kind='line')


# In[19]:


# 정리

# 1. fig = plt.figure():
# figure 객체를 선언해 '도화지를 펼쳐' 줍니다.

# 2. ax1 = fig.add_subplot(1,1,1) :
    # 축을 그립니다.

# 3. ax1.bar(x, y): 
# 축안에 어떤 그래프를 그릴지 메소드를 선택한 다음,
    # 인자로 데이터를 넣어줍니다.

# 4. 그래프 타이틀 축의 레이블 등을 plt의 여러 메소드
    # grid, xlabel, ylabel 을 이용해서 추가해주고
# 5. plt.savefig 메소드를 이용해 저장해 줍니다.


# In[20]:


import pandas as pd
import seaborn as sns

tips = sns.load_dataset("tips")


# In[21]:


df = pd.DataFrame(tips)
df.head()


# In[22]:


df = pd.DataFrame(tips)
df.head()


# In[23]:


df.shape


# In[24]:


df.describe()


# In[25]:


df.info()


# In[26]:


print(df['sex'].value_counts())
print("===========================")


print(df['time'].value_counts())
print("===========================")


print(df['smoker'].value_counts())
print("===========================")


print(df['day'].value_counts())
print("===========================")


print(df['size'].value_counts())
print("===========================")


# In[27]:


#df의 첫 5행을 확인해봅시다. 
df.head()


# In[28]:


grouped = df['tip'].groupby(df['sex'])


# In[29]:


grouped.mean() # 성별에 따른 팁의 평균


# In[30]:


grouped.size() # 성별에 따른 데이터 량(팁 횟수)


# In[31]:


import numpy as np
sex = dict(grouped.mean()) #평균 데이터를 딕셔너리 형태로 바꿔줍니다.
sex


# In[32]:


x = list(sex.keys())  
x


# In[33]:


y = list(sex.values())
y


# In[34]:


import matplotlib.pyplot as plt

plt.bar(x = x, height = y)
plt.ylabel('tip[$]')
plt.title('Tip by Sex')


# In[35]:


sns.barplot(data=df, x='sex', y='tip')


# In[36]:


plt.figure(figsize=(10,6)) # 도화지 사이즈를 정합니다.
sns.barplot(data=df, x='sex', y='tip')
plt.ylim(0, 4) # y값의 범위를 정합니다.
plt.title('Tip by sex') # 그래프 제목을 정합니다.


# In[37]:


plt.figure(figsize=(10,6))
sns.barplot(data=df, x='day', y='tip')
plt.ylim(0, 4)
plt.title('Tip by day')


# In[38]:


fig = plt.figure(figsize=(10,7))

ax1 = fig.add_subplot(2,2,1)
sns.barplot(data=df, x='day', y='tip',palette="ch:.25")

ax2 = fig.add_subplot(2,2,2)
sns.barplot(data=df, x='sex', y='tip')

ax3 = fig.add_subplot(2,2,4)
sns.violinplot(data=df, x='sex', y='tip')

ax4 = fig.add_subplot(2,2,3)
sns.violinplot(data=df, x='day', y='tip',palette="ch:.25")


# In[39]:


sns.catplot(x="day", y="tip", jitter=False, data=tips)


# In[40]:


sns.scatterplot(data=df , x='total_bill', y='tip', palette="ch:r=-.2,d=.3_r")


# In[41]:


sns.scatterplot(data=df , x='total_bill', y='tip', hue='day')


# In[42]:


#np.random.randn 함수는 표준 정규분포에서 난수를 생성하는 함수입니다. 
#cumsum()은 누적합을 구하는 함수입니다.
plt.plot(np.random.randn(50).cumsum())


# In[43]:


x = np.linspace(0, 10, 100) 
plt.plot(x, np.sin(x), 'o')
plt.plot(x, np.cos(x)) 
plt.show()


# In[44]:


sns.lineplot(x, np.sin(x))
sns.lineplot(x, np.cos(x))


# In[45]:


#그래프 데이터 
mu1, mu2, sigma = 100, 130, 15
x1 = mu1 + sigma*np.random.randn(10000)
x2 = mu2 + sigma*np.random.randn(10000)

# 축 그리기
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

# 그래프 그리기
patches = ax1.hist(x1, bins=50, density=False) #bins는 x값을 총 50개 구간으로 나눈다는 뜻입니다.
patches = ax1.hist(x2, bins=50, density=False, alpha=0.5)
ax1.xaxis.set_ticks_position('bottom') # x축의 눈금을 아래 표시 
ax1.yaxis.set_ticks_position('left') #y축의 눈금을 왼쪽에 표시

# 라벨, 타이틀 달기
plt.xlabel('Bins')
plt.ylabel('Number of Values in Bin')
ax1.set_title('Two Frequency Distributions')

# 보여주기
plt.show()


# In[46]:


sns.distplot(df['total_bill'], label = "total_bill")
sns.distplot(df['tip'], label = "tip").legend()# legend()를 이용하여 label을 표시해 줍니다.


# In[47]:


df['tip_pct'] = df['tip'] / df['total_bill']
df['tip_pct'].hist(bins=50)


# In[48]:


df['tip_pct'].plot(kind='kde')


# In[49]:


csv_path = os.getenv("HOME") + "/aiffel/data_visualization/data/flights.csv"
data = pd.read_csv(csv_path)
flights = pd.DataFrame(data)
flights


# In[50]:


sns.barplot(data=flights, x='year', y='passengers')


# In[51]:


sns.pointplot(data=flights, x='year', y='passengers')


# In[52]:


sns.lineplot(data=flights, x='year', y='passengers')


# In[53]:


sns.lineplot(data=flights, x='year', y='passengers', hue='month', palette='ch:.50')
plt.legend(bbox_to_anchor=(1.03, 1), loc=2) #legend 그래프 밖에 추가하기


# In[54]:


sns.distplot(flights['passengers'])


# In[55]:


pivot = flights.pivot(index='year', columns='month', values='passengers')
pivot


# In[56]:


sns.heatmap(pivot)


# In[58]:


sns.heatmap(pivot, linewidths=.2, annot=True, fmt="d")


# In[59]:


sns.heatmap(pivot, cmap="YlGnBu")


# In[ ]:




