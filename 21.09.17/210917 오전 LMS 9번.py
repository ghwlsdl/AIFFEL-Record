# Preview

# Q. 데이터 전처리는 왜 해야할까요??

# 동현 : 결과값에 영향을 줄 수 있는 잘못된 데이터를 지워야 한다.

# 호진 : 데이터가 너무 많을 때 진짜로 필요한 데이터만 추출해야 한다.

# 태균 : 데이터에 결측값을 처리해주기 위해서 필요하다.

# 성연 : 분석의 결과에 신뢰도를 좌우하는게 데이터 전처리라고 생각한다.

# 머신러닝 : 기계를 학습시킨다는 것인데,

# 기계라는 것은 결국 확률 모델을 학습시킨다.

# 학습을 통해 얻은 확률모델을 새로운 데이터에 대해서도 계속 사용을 합니다.

# 결국은 모델의 정확도와 신뢰도에 직접적인 영향을 주는게 데이터 전처리입니다.


# In[ ]:


# 데이터 분석의 8할은 데이터 전처리이다. 라는 말이 있는데,

# 중요한 이유는, 데이터 분석의 질이 달라지기 때문입니다.


# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("👽 Hello.")


# In[2]:


import os

csv_file_path = os.getenv('HOME')+'/aiffel/data_preprocess/data/trade.csv'
trade = pd.read_csv(csv_file_path) 
trade.head()


# In[ ]:


#중복된 데이터를 찾아 제거할 수 있고, 결측치(missing data)를 제거하거나 채워 넣을 수 있다.

# 데이터를 정규화시킬 수 있다.

# 이상치(outlier)를 찾고, 이를 처리할 수 있다.

# 범주형 데이터를 원-핫 인코딩할 수 있다.

# 연속적인 데이터를 구간으로 나눠 범주형 데이터로 변환할 수 있다.


# In[ ]:


# 결측치(Missing Data)

# 중복된 데이터

# 이상치(Outlier)

# 정규화(Normalization)

# 원-핫 인코딩(One-Hot Encoding)

# 구간화(Binning)


# In[ ]:


# 9-2. 결측치


# In[3]:


print('전체 데이터 건수:', len(trade))


# In[4]:


print('컬럼별 결측치 개수')
len(trade) - trade.count()


# In[5]:


trade = trade.drop('기타사항', axis=1)
trade.head()


# In[ ]:


# DataFrame.isnull()은 데이터마다 결측치 여부를

# True, False로 반환합니다.

# DataFrame.any(axis=1)는 행마다 하나라도 True가 있으면 True,

# 그렇지 않으면 False를 반환합니다.


# In[ ]:


# DataFrame에 isnull()을 적용하고,

# 여기도 또 any(axis=1) 메서드를 적용합니다.

# 이 결과, '각 행이 결측치가 하나라도 있는지' 여부를

# 불리언 값으로 가진 Series가 출력됩니다.


# In[6]:


trade.isnull() # isnull 은 결측치의 여부를 측정 할 수 있습니다.


# In[7]:


trade.isnull().any(axis=1)


# In[8]:


trade[trade.isnull().any(axis=1)]


# In[ ]:


# DataFrame의 dropna는 결측치를 삭제해주는 메서드입니다.

# subset 옵션으로 특정 컬럼들을 선택했습니다.

# how 옵션으로 선택한 컬럼 전부가 결측치인

# 행을 삭제하겠다는 의미로 'all'을 선택합니다.

# ('any': 하나라도 결측치인 경우)

# * inplace 옵션으로 해당 DataFrame 내부에 바로 적용시켰습니다.


# In[9]:


trade.dropna(how='all', subset=['수출건수', '수출금액', '수입건수', '수입금액', '무역수지'], inplace=True)
print("👽 It's okay, no biggie.")


# In[10]:


trade[trade.isnull().any(axis=1)]


# In[11]:


trade.loc[[188, 191, 194]]


# In[12]:


trade.loc[191, '수출금액'] = (trade.loc[188, '수출금액'] + trade.loc[194, '수출금액'] )/2
trade.loc[[191]]


# In[13]:


trade.loc[191, '무역수지'] = trade.loc[191, '수출금액'] - trade.loc[191, '수입금액'] 
trade.loc[[191]]


# In[ ]:


# 9-3. 중복된 데이터


# In[14]:


#DataFrame.duplicated()는 중복된 데이터 여부를 불리언 값으로반환

trade.duplicated()


# In[15]:


trade[trade.duplicated()]


# In[16]:


trade[(trade['기간']=='2020년 03월')&(trade['국가명']=='중국')]


# In[17]:


trade.drop_duplicates(inplace=True)
print("👽 It's okay, no biggie.")


# In[18]:


df = pd.DataFrame({'id':['001', '002', '003', '004', '002'], 
                   'name':['Park Yun', 'Kim Sung', 'Park Jin', 'Lee Han', 'Kim Min']})
df


# In[19]:


df.drop_duplicates(subset=['id'], keep='last')


# In[ ]:


# pandas.DataFrame.drop_duplicates'

# subset : 열 레이블 또는 레이블 시퀀스, 선택 사항

# 중복을 식별하기 위해 특정 열만 고려하고 기본적으로 모든 열을 사용합니다.

# keep : 첫 번째'{ '첫 번째' '마지막', 거짓}, 기본

# 유지할 복제본(있는 경우)을 결정합니다.

# - first: 첫 번째 항목을 제외하고 중복 항목을 삭제합니다.

# - last: 마지막 항목을 제외하고 중복 항목을 삭제합니다.

# - False : 모든 중복을 삭제합니다.

# inplace : bool, 기본값 False

# 복제본을 제자리에 삭제할지 또는 복사본을 반환할지 여부입니다.

# ignore_index : bool, 기본값은 False

# True이면 결과 축에 0, 1, ..., n - 1이라는 레이블이 지정됩니다.

# 중복이 제거된 DataFrame 또는 None 경우 inplace=True.


# In[20]:


df = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 5]
})
df


# In[21]:


# 기본적으로 모든 열을 기반으로 중복 행을 제거합니다.

df.drop_duplicates()


# In[22]:


# 특정 열에서 중복을 제거하려면 subset 을 사용합니다.

df.drop_duplicates(subset=['brand'])


# In[23]:


# 중복을 제거하고 마지막 항목을 유지하려면 를 사용하십시오

df.drop_duplicates(subset=['brand', 'style'], keep='last') 


# In[ ]:


# 9.4. 이상치(Outier) :

# 대부분 값의 범위에서 벗어나 극단적으로 크거나 작은 겂을 의미

# Min-Max Scaling 해보면 대부분의 값은 0에 가깝고 이상치만 1에 가까운 값을 가지게 될 것입니다.

# 평균과 표준편차를 이용하는 z score

# 평균을 빼주고 표준편차로 나눠 z score({\frac {X-\mu }{\sigma }})( )를 계산


# In[24]:


def outlier(df, col, z):
    return df[abs(df[col] - np.mean(df[col]))/np.std(df[col])>z].index
print("👽 It's okay, no biggie.")


# In[ ]:


# z-score method

# abs(df[col] - np.mean(df[col])) :
# 데이터에서 평균을 빼준 것에 절대값을 취합니다.
# abs(df[col] - np.mean(df[col]))/np.std(df[col]) :
# 위에 한 작업에 표준편차로 나눠줍니다.
# df[abs(df[col] - np.mean(df[col]))/np.std(df[col])>z].index:
# 값이 z보다 큰 데이터의 인덱스를 추출합니다.


# In[25]:


trade.loc[outlier(trade, '무역수지', 1.5)]


# In[27]:


trade.loc[outlier(trade, '무역수지', 2)]


# In[28]:


trade.loc[outlier(trade, '무역수지', 3)]


# In[29]:


def not_outlier(df, col, z):
    return df[abs(df[col] - np.mean(df[col]))/np.std(df[col]) <= z].index
print("👽 It's okay, no biggie.")


# In[30]:


trade.loc[not_outlier(trade, '무역수지', 1.5)]


# In[31]:


# IQR method

np.random.seed(2020)
data = np.random.randn(100)  # 평균 0, 표준편차 1의 분포에서 100개의 숫자를 샘플링한 데이터 생성
data = np.concatenate((data, np.array([8, 10, -3, -5])))      # [8, 10, -3, -5])를 데이터 뒤에 추가함
data


# In[32]:


fig,ax = plt.subplots()
ax.boxplot(data)
plt.show()


# In[33]:


Q3,Q1 = np.percentile(data, [75,25])
IQR = Q3 - Q1
IQR


# In[34]:


data[(Q1-1.5*IQR > data)|(Q3+1.5*IQR < data)]


# In[35]:


# Z-score method

import numpy as np

def outliers_z_score(ys):
    threshold = 3

    mean_y = np.mean(ys)
    stdev_y = np.std(ys)
    z_scores = [(y - mean_y) / stdev_y for y in ys]
    return np.where(np.abs(z_scores) > threshold)


# In[36]:


import numpy as np

def outliers_modified_z_score(ys):
    threshold = 3.5

    median_y = np.median(ys)
    median_absolute_deviation_y = np.median([np.abs(y - median_y) for y in ys])
    modified_z_scores = [0.6745 * (y - median_y) / median_absolute_deviation_y
                         for y in ys]
    return np.where(np.abs(modified_z_scores) > threshold)


# In[37]:


import numpy as np

def outliers_iqr(ys):
    quartile_1, quartile_3 = np.percentile(ys, [25, 75])
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * 1.5)
    upper_bound = quartile_3 + (iqr * 1.5)
    return np.where((ys > upper_bound) | (ys < lower_bound))


# In[42]:


def outlier2(df, col):
    # [[YOUR CODE]]

outlier2(trade, '무역수지') pass


# In[43]:


# 정규분포를 따라 랜덤하게 데이터 x를 생성합니다.

np.random.seed(2020)
x = pd.DataFrame({'A': np.random.randn(100)*4+4,
                 'B': np.random.randn(100)-1})
x


# In[44]:


# 데이터 x를 Standardization 기법으로 정규화합니다. 

x_standardization = (x - x.mean())/x.std()
x_standardization


# In[45]:


# 데이터 x를 min-max scaling 기법으로 정규화합니다. 

x_min_max = (x-x.min())/(x.max()-x.min())
x_min_max


# In[46]:


fig, axs = plt.subplots(1,2, figsize=(12, 4),
                        gridspec_kw={'width_ratios': [2, 1]})

axs[0].scatter(x['A'], x['B'])
axs[0].set_xlim(-5, 15)
axs[0].set_ylim(-5, 5)
axs[0].axvline(c='grey', lw=1)
axs[0].axhline(c='grey', lw=1)
axs[0].set_title('Original Data')

axs[1].scatter(x_standardization['A'], x_standardization['B'])
axs[1].set_xlim(-5, 5)
axs[1].set_ylim(-5, 5)
axs[1].axvline(c='grey', lw=1)
axs[1].axhline(c='grey', lw=1)
axs[1].set_title('Data after standardization')

plt.show()


# In[47]:


fig, axs = plt.subplots(1,2, figsize=(12, 4),
                        gridspec_kw={'width_ratios': [2, 1]})

axs[0].scatter(x['A'], x['B'])
axs[0].set_xlim(-5, 15)
axs[0].set_ylim(-5, 5)
axs[0].axvline(c='grey', lw=1)
axs[0].axhline(c='grey', lw=1)
axs[0].set_title('Original Data')

axs[1].scatter(x_min_max['A'], x_min_max['B'])
axs[1].set_xlim(-5, 5)
axs[1].set_ylim(-5, 5)
axs[1].axvline(c='grey', lw=1)
axs[1].axhline(c='grey', lw=1)
axs[1].set_title('Data after min-max scaling')

plt.show()


# In[48]:


# Standardization


# In[49]:


# trade 데이터를 Standardization 기법으로 정규화합니다.

cols = ['수출건수', '수출금액', '수입건수', '수입금액', '무역수지']
trade_Standardization= (trade[cols]-trade[cols].mean())/trade[cols].std()
trade_Standardization.head()


# In[50]:


trade_Standardization.describe()


# In[51]:


# trade 데이터를 min-max scaling 기법으로 정규화합니다. 

trade[cols] = (trade[cols]-trade[cols].min())/(trade[cols].max()-trade[cols].min())
trade.head()


# In[52]:


trade.describe()


# In[53]:


train = pd.DataFrame([[10, -10], [30, 10], [50, 0]])
test = pd.DataFrame([[0, 1], [10, 10]])
print("👽 It's okay, no biggie.")


# In[54]:


train_min = train.min()
train_max = train.max()

train_min_max = (train - train_min)/(train_max - train_min)
test_min_max =  (test - train_min)/(train_max - train_min)    # test를 min-max scaling할 때도 train 정규화 기준으로 수행
print("💫 It's okay, no biggie...")


# In[55]:


train_min_max


# In[56]:


test_min_max


# In[57]:


from sklearn.preprocessing import MinMaxScaler
train = [[10, -10], [30, 10], [50, 0]]
test = [[0, 1]]
scaler = MinMaxScaler()
print("👽 It's okay, no biggie.")


# In[58]:


scaler.fit_transform(train)


# In[59]:


scaler.transform(test)


# In[ ]:


# 9-6. 원-핫 인코딩(One-Hot Encoding)


# In[60]:


#trade 데이터의 국가명 컬럼 원본
print(trade['국가명'].head())  

# get_dummies를 통해 국가명 원-핫 인코딩
country = pd.get_dummies(trade['국가명'])
country.head()


# In[61]:


#trade 데이터의 국가명 컬럼 원본
print(trade['국가명'].head())  

# get_dummies를 통해 국가명 원-핫 인코딩
country = pd.get_dummies(trade['국가명'])
country.head()


# In[62]:


trade.drop(['국가명'], axis=1, inplace=True)
trade.head()


# In[ ]:


# 9-7. 구간화(Binning)


# In[63]:


salary = pd.Series([4300, 8370, 1750, 3830, 1840, 4220, 3020, 2290, 4740, 4600, 
                    2860, 3400, 4800, 4470, 2440, 4530, 4850, 4850, 4760, 4500, 
                    4640, 3000, 1880, 4880, 2240, 4750, 2750, 2810, 3100, 4290, 
                    1540, 2870, 1780, 4670, 4150, 2010, 3580, 1610, 2930, 4300, 
                    2740, 1680, 3490, 4350, 1680, 6420, 8740, 8980, 9080, 3990, 
                    4960, 3700, 9600, 9330, 5600, 4100, 1770, 8280, 3120, 1950, 
                    4210, 2020, 3820, 3170, 6330, 2570, 6940, 8610, 5060, 6370,
                    9080, 3760, 8060, 2500, 4660, 1770, 9220, 3380, 2490, 3450, 
                    1960, 7210, 5810, 9450, 8910, 3470, 7350, 8410, 7520, 9610, 
                    5150, 2630, 5610, 2750, 7050, 3350, 9450, 7140, 4170, 3090])
print("👽 Almost there..")


# In[64]:


salary.hist()


# In[65]:


bins = [0, 2000, 4000, 6000, 8000, 10000]
print("👽 Almost there..")


# In[66]:


ctg = pd.cut(salary, bins=bins)
ctg


# In[67]:


print('salary[0]:', salary[0])
print('salary[0]가 속한 카테고리:', ctg[0])


# In[68]:


ctg.value_counts().sort_index()


# In[69]:


ctg = pd.cut(salary, bins=6)
ctg


# In[70]:


ctg.value_counts().sort_index()


# In[73]:


ctg = pd.qcut(salary, q=5)
ctg


# In[74]:


print(ctg.value_counts().sort_index())
print(".\n.\n🛸 Well done!")


# In[ ]:




