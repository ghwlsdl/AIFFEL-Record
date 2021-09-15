#!/usr/bin/env python
# coding: utf-8

# In[1]:


#평균 계산하기

total = 0
count = 0
numbers = input("Enter a number :  (<Enter Key> to quit)")
while numbers != "":
    try:
        x = float(numbers)
        count += 1
        total = total + x
    except ValueError:
        print('NOT a number! Ignored..')
    numbers = input("Enter a number :  (<Enter Key> to quit)")
avg = total / count
print("\n average is", avg)


# In[2]:


# 2개 이상의 숫자를 입력받아 리스트에 저장하는 함수
def numbers():
    X=[]    # X에 빈 리스트를 할당합니다.
    while True:
        number = input("Enter a number (<Enter key> to quit)") 
        while number !="":
            try:
                x = float(number)
                X.append(x)    # float형으로 변환한 숫자 입력을 리스트에 추가합니다.
            except ValueError:
                print('>>> NOT a number! Ignored..')
            number = input("Enter a number (<Enter key> to quit)")
        if len(X) > 1:  # 저장된 숫자가 2개 이상일 때만 리턴합니다.
            return X

X=numbers()

print('X :', X)


# In[3]:


import array as arr

mylist = [1, 2, 3]   # 이것은 파이썬 built-in list입니다. 
print(type(mylist))

mylist.append('4')  # mylist의 끝에 character '4'를 추가합니다. 
print(mylist)

mylist.insert(1, 5)  # mylist의 두번째 자리에 5를 끼워넣습니다.
print(mylist)

myarray = arr.array('i', [1, 2, 3])   # 이것은 array입니다. import array를 해야 쓸 수 있습니다.
print(type(myarray))

# 아래 라인의 주석을 풀고 실행하면 에러가 납니다.
#myarray.append('4')    # myarray의 끝에 character '4'를 추가합니다. 
print(myarray)

myarray.insert(1, 5)    # myarray의 두번째 자리에 5를 끼워넣습니다.
print(myarray)


# In[4]:


total = 0.0
for i in range(len(X)):
    total = total + X[i]
mean = total / len(X)

print('sum of X: ', total)


# In[5]:


def median(nums):  		# nums : 리스트를 지정하는 매개변수
    nums.sort()					# sort()로 리스트를 순서대로 정렬
    size = len(nums)
    p = size // 2
    if size % 2 == 0:		   # 리스트의 개수가 짝수일때 
        pr = p                         # 4번째 값
        pl = p-1                      # 3번째 값
        mid= float((nums[pl]+nums[pr])/2)    
    else:								# 리스트의 개수가 홀수일때
        mid = nums[p]
    return mid

print('X :', X)
median(X)						# 매개변수의 값으로 X를 사용함


# In[7]:


#avg = means(X)

def std_dev(nums, avg):
   texp = 0.0
   for i in range(len(nums)):
       texp = texp + (nums[i] - avg)**2    # 각 숫자와 평균값의 차이의 제곱을 계속 더한 후
   return (texp/(len(nums)-1)) ** 0.5    # 그 총합을 숫자개수-1로 나눈 값의 제곱근을 리턴합니다.

std_dev(X,avg)


# In[9]:


#avg = means(X)

def std_dev(nums, avg):
   texp = 0.0
   for i in range(len(nums)):
       texp = texp + (nums[i] - avg)**2    # 각 숫자와 평균값의 차이의 제곱을 계속 더한 후
   return (texp/(len(nums)-1)) ** 0.5    # 그 총합을 숫자개수-1로 나눈 값의 제곱근을 리턴합니다.

std_dev(X,avg)


# In[11]:


# med = median(X)
# avg = means(X)
std = std_dev(X, avg)
print("당신이 입력한 숫자{}의 ".format(X))
print("중앙값은{}, 평균은{}, 표준편차는{}입니다.".format(med, avg, std))


# In[12]:


def numbers():
    X=[]
    while True:
        number = input("Enter a number (<Enter key> to quit)") 
        while number !="":
            try:
                x = float(number)
                X.append(x)
            except ValueError:
                print('>>> NOT a number! Ignored..')
            number = input("Enter a number (<Enter key> to quit)")
        if len(X) > 1:
            return X

def median(nums): 
    nums.sort()
    size = len(nums)
    p = size // 2
    if size % 2 == 0:
        pr = p
        pl = p-1
        mid = float((nums[pl]+nums[pr])/2)
    else:
        mid = nums[p]
    return mid

def means(nums):
    total = 0.0
    for i in range(len(nums)):
        total = total + nums[i]
    return total / len(nums)

def std_dev(nums, avg):
   texp = 0.0
   for i in range(len(nums)):
       texp = texp + (nums[i] - avg) ** 2
   return (texp/(len(nums)-1)) ** 0.5

def main():
    X = numbers()
    med = median(X)
    avg = means(X)
    std = std_dev(X, avg)
    print("당신이 입력한 숫자{}의 ".format(X))
    print("중앙값은{}, 평균은{}, 표준편차는{}입니다.".format(med, avg, std))

if __name__ == '__main__':
    main()


# In[13]:


import numpy as np

# 아래 A와 B는 결과적으로 같은 ndarray 객체를 생성합니다. 
A = np.arange(5)
B = np.array([0,1,2,3,4])  # 파이썬 리스트를 numpy ndarray로 변환

# 하지만 C는 좀 다를 것입니다. 
C = np.array([0,1,2,3,'4'])

# D도 A, B와 같은 결과를 내겠지만, B의 방법을 권합니다. 
D = np.ndarray((5,), np.int64, np.array([0,1,2,3,4]))

print(A)
print(type(A))
print(B)
print(type(B))
print(C)
print(type(C))
print(D)
print(type(D))


# In[14]:


A = np.arange(10).reshape(2,5)   # 길이 10의 1차원 행렬을 2X5 2차원 행렬로 바꿔봅니다.

print(A.shape)
print(A.ndim)
print(A.size)


# In[15]:


A = np.arange(10)
print('A: ', A)
B = np.arange(10).reshape(2,5)
print('B: ', B)
C = np.arange(10).reshape(3,3)  # 이 줄에서 에러가 날 것입니다.
print('C: ', C)


# In[16]:


A= np.arange(6).reshape(2,3)
print(A)
print(A.dtype)
print(type(A))

B = np.array([0,1,2,3,4,5])  
print(B)
print(B.dtype)
print(type(B))

C = np.array([0,1,2,3,'4',5])
print(C)
print(C.dtype)
print(type(C))

D = np.array([0,1,2,3,[4,5],6])  # 이런 ndarray도 만들어질까요?
print(D)
print(D.dtype)
print(type(D))


# In[17]:


C = np.array([0,1,2,3,'4',5])
print(C[0])
print(type(C[0]))
print(C[4])
print(type(C[4]))

D = np.array([0,1,2,3,[4,5],6])
print(D[0])
print(type(D[0]))
print(D[4])
print(type(D[4]))


# In[18]:


A = np.arange(10).reshape(2,5)   # 길이 10의 1차원 행렬을 2X5 2차원 행렬로 바꿔봅니다.

print(A.shape)
print(A.ndim)
print(A.size)


# In[19]:


A = np.arange(10)
print('A: ', A)
B = np.arange(10).reshape(2,5)
print('B: ', B)
C = np.arange(10).reshape(3,3)  # 이 줄에서 에러가 날 것입니다.
print('C: ', C)


# In[20]:


A= np.arange(6).reshape(2,3)
print(A)
print(A.dtype)
print(type(A))

B = np.array([0,1,2,3,4,5])  
print(B)
print(B.dtype)
print(type(B))

C = np.array([0,1,2,3,'4',5])
print(C)
print(C.dtype)
print(type(C))

D = np.array([0,1,2,3,[4,5],6])  # 이런 ndarray도 만들어질까요?
print(D)
print(D.dtype)
print(type(D))


# In[21]:


C = np.array([0,1,2,3,'4',5])
print(C[0])
print(type(C[0]))
print(C[4])
print(type(C[4]))

D = np.array([0,1,2,3,[4,5],6])
print(D[0])
print(type(D[0]))
print(D[4])
print(type(D[4]))


# In[22]:


# 단위행렬
np.eye(3)


# In[23]:


# 0 행렬
np.zeros([2,3])


# In[24]:


# 1행렬
np.ones([3,3])


# In[25]:


A = np.arange(9).reshape(3,3)
A


# In[26]:


# ndarray A에 2를 상수배 했을 때,
A * 2


# In[27]:


# ndarray A에 2를 더했을 때,
A + 2


# In[28]:


# 3 X 3 행렬에 1 X 3 행렬을 더했을 때
A = np.arange(9).reshape(3,3)
B = np.array([1, 2, 3])
print(A)
print(B)
A+B


# In[29]:


# 3 X 3 행렬에 3 X 1 행렬을 더했을 때
A = np.arange(9).reshape(3,3)
C = np.array([[1], [2], [3]])
print(A)
print(C)
A+C


# In[30]:


# 3 X 3 행렬에 1 X 2 행렬을 더하는 것은 허용되지 않습니다. 
A = np.arange(9).reshape(3,3)
D = np.array([1, 2])
print(A)
print(D)
A+D


# In[31]:


print([1,2]+[3,4])
print([1,2]+3)


# In[32]:


import numpy as np
print(np.array([1,2])+np.array([3,4]))
print(np.array([1,2])+3)


# In[33]:


# 3 X 3 행렬의 첫번째 행을 구해 봅시다. 
A = np.arange(9).reshape(3,3)
print(A)
B = A[0]
print(B)


# In[34]:


# 0, 1을 인덱싱 하면 A의 첫번째 행에서 두번째 값을 참조합니다.
# 아래 두 결과는 정확히 같습니다.
print(A[0, 1])
print(B[1])


# In[35]:


# 슬라이싱도 비슷합니다.
A[:-1]


# In[36]:


# 이 슬라이싱의 결과는 
print(A[:,2:])
print(A[:,1:])
print(A[:,:])

# 이 슬라이싱의 결과와 동일합니다.
print(A[:,-1:])
print(A[:,-2:])
print(A[:,-3:])

# 위 그림과 비교해서 이해해 보세요.


# In[37]:


A[1,:2]


# In[38]:


A[:2, 1:]


# In[39]:


A[:,-1]


# In[41]:


# 의사 난수를 생성하는 예제입니다. 여러번 실행해 보세요.

print(np.random.random())   # 0에서 1사이의 실수형 난수 하나를 생성합니다. 

print(np.random.randint(0,10))   # 0~9 사이 1개 정수형 난수 하나를 생성합니다. 

print(np.random.choice([0,1,2,3,4,5,6,7,8,9]))   # 리스트에 주어진 값 중 하나를 랜덤하게 골라줍니다.


# In[44]:


# 아래 2가지는 기능면에서 동일합니다. 원소의 순서를 임의로 뒤바꾸어 줍니다. 

print(np.random.permutation(10))   
print(np.random.permutation([0,1,2,3,4,5,6,7,8,9]))


# In[45]:


# 아래 기능들은 어떤 분포를 따르는 변수를 임의로 표본추출해 줍니다. 

# 이것은 정규분포를 따릅니다.
print(np.random.normal(loc=0, scale=1, size=5))    # 평균(loc), 표준편차(scale), 추출개수(size)를 조절해 보세요.

# 이것은 균등분포를 따릅니다. 
print(np.random.uniform(low=-1, high=1, size=5))  # 최소(low), 최대(high), 추출개수(size)를 조절해 보세요.


# In[46]:


A = np.arange(24).reshape(2,3,4)
print(A)               # A는 (2,3,4)의 shape를 가진 행렬입니다. 
print(A.T)            # 이것은 A의 전치행렬입니다. 
print(A.T.shape) # A의 전치행렬은 (4,3,2)의 shape를 가진 행렬입니다.


# In[47]:


# np.transpose는 행렬의 축을 어떻게 변환해 줄지 임의로 지정해 줄 수 있는 일반적인 행렬 전치 함수입니다. 
# np.transpose(A, (2,1,0)) 은 A.T와 정확히 같습니다.

B = np.transpose(A, (2,0,1))
print(A)             # A는 (2,3,4)의 shape를 가진 행렬입니다. 
print(B)             # B는 A의 3, 1, 2번째 축을 자신의 1, 2, 3번째 축으로 가진 행렬입니다.
print(B.shape)  # B는 (4,2,3)의 shape를 가진 행렬입니다.


# In[48]:


import numpy as np

# 6-3 스텝에서 사용하였던 함수입니다. 
def numbers():
    X = []
    number = input("Enter a number (<Enter key> to quit)") 
    # 하지만 2개 이상의 숫자를 받아야 한다는 제약조건을 제외하였습니다.
    while number != "":
        try:
            x = float(number)
            X.append(x)
        except ValueError:
            print('>>> NOT a number! Ignored..')
        number = input("Enter a number (<Enter key> to quit)")
    return X

def main():
    nums = numbers()       # 이것은 파이썬 리스트입니다. 
    num = np.array(nums)   # 리스트를 Numpy ndarray로 변환합니다.
    print("합", num.sum())
    print("평균값",num.mean())
    print("표준편차",num.std())
    print("중앙값",np.median(num))   # num.median() 이 아님에 유의해 주세요.

main()


# In[49]:


import PIL
PIL.__version__


# In[50]:


from PIL import Image, ImageColor
import os
img_path = os.getenv("HOME") + "/aiffel/data_represent/image/newyork.jpg"
img = Image.open(img_path)
print(img_path)
print(type(img))
img


# In[51]:


img.size


# In[52]:


W, H = img.size
print((W, H))


# In[53]:


print(img.format)
print(img.size)
print(img.mode)


# In[54]:


img.crop((30,30,100,100))


# In[55]:


# 새로운 이미지 파일명
cropped_img_path = os.getenv("HOME") + "/aiffel/data_represent/image/cropped_img.jpg"
img.crop((30,30,100,100)).save(cropped_img_path)
print("저장 완료!")


# In[56]:


get_ipython().system('ls ~/aiffel/data_represent/image/cropped_img.jpg')


# In[57]:


import numpy as np
img_arr = np.array(img)
print(type(img))
print(type(img_arr))
print(img_arr.shape)
print(img_arr.ndim)


# In[58]:


img_arr


# In[59]:


img_g = Image.open(img_path).convert('L')
img_g


# In[60]:


img_g_arr = np.array(img_g)
print(type(img_g_arr))
print(img_g_arr.shape)
print(img_g_arr.ndim)


# In[61]:


img_g_arr


# In[62]:


red = ImageColor.getcolor('RED','RGB')
reda = ImageColor.getcolor('red','RGBA')
yellow = ImageColor.getcolor('yellow','RGB')
print(red)
print(reda)
print(yellow)


# In[63]:


# 파이썬 dict 로 표현한 전화번호부입니다. 
Country_PhoneNumber = {'Korea': 82, 'America': 1, 'Swiss': 41, 'Italy': 39, 'Japan': 81, 'China': 86, 'Rusia': 7}
Country_PhoneNumber['Korea']  # 키를 가지고 값을 조회할 수 있습니다.


# In[64]:


#물품을 보여주는 함수

treasure_box = {'rope':2, 
                'apple':10, 
                'torch': 6, 
                'gold coin': 50, 
                'knife': 1, 
                'arrow': 30}

def display_stuff(treasure_box):
    print("Congraturation!! you got a treasure box")
    for k, v in treasure_box.items():
        print("you have {} {}pcs".format(k, v))
display_stuff(treasure_box)


# In[65]:


#물품을 통해 얻을 은화를 보여주는 함수

coin_per_treasure = {'rope':1,
        'apple':2,
        'torch': 2,
        'gold coin': 5, 
        'knife': 30,
        'arrow': 1}

def total_silver(treasure_box, coin_per_treasure):
    total_coin = 0
    for treasure in treasure_box:
        coin = coin_per_treasure[treasure] * treasure_box[treasure]
        print("{} : {}coins/pcs * {}pcs = {} coins".format(
          treasure, coin_per_treasure[treasure], treasure_box[treasure], coin))
        total_coin += coin
    print('total_coin : ', total_coin)
total_silver(treasure_box, coin_per_treasure)


# In[66]:


treasure_box = {'rope': {'coin': 1, 'pcs': 2},
                'apple': {'coin': 2, 'pcs': 10},
                'torch': {'coin': 2, 'pcs': 6},
                'gold coin': {'coin': 5, 'pcs': 50},
                'knife': {'coin': 30, 'pcs': 1},
               	'arrow': {'coin': 1, 'pcs': 30}
               }
treasure_box['rope']


# In[76]:


def display_stuff(treasure_box):
    print("Congreaturation!! you got a treasure boox")
    for k, v in treasure_box.items():
        print("you have {} {}pcs".format(k,v))

display_stuff(treasure_box)


# In[80]:


def total_silver(treasure_box, coin_per_treasure):
    total_coin = 0
    for treasure in treasure_box:
        coin = coin_per_treasure[treasure] * treasure_box[treasure]
        print("{} : {}coins/pcs * {}pcs = {} coins".format(
          treasure, coin_per_treasure[treasure], treasure_box[treasure], coin))
        total_coin += coin
    print('total_coin : ', total_coin)
total_silver(treasure_box, coin_per_treasure)


# In[81]:


import pandas as pd
ser = pd.Series(['a','b','c',3])
ser


# In[82]:


ser.values


# In[83]:


ser.index


# In[85]:


# 인덱스 설정 : Series의 인자로 넣어주는 방법

ser2 = pd.Series(['a', 'b', 'c', 3], index=['i','j','k','h'])
ser2


# In[86]:


# 인덱스 설정: 할당 연산자

ser2.index = ['Jhon', 'Steve', 'Jack', 'Bob']
ser2


# In[87]:


ser2.index


# In[88]:


Country_PhoneNumber = {'Korea': 82, 'America': 1, 'Swiss': 41, 'Italy': 39, 'Japan': 81, 'China': 86, 'Rusia': 7}
ser3 = pd.Series(Country_PhoneNumber)
ser3


# In[89]:


ser3['Korea']


# In[90]:


ser3['Italy':]


# In[92]:


#Series의 Name

ser3.name = 'Country_PhoneNumber'
ser3.index.name = 'Country_Name'
ser3


# In[93]:


# Series로 변환

data = {'Region' : ['Korea', 'America', 'Chaina', 'Canada', 'Italy'],
        'Sales' : [300, 200, 500, 150, 50],
        'Amount' : [90, 80, 100, 30, 10],
        'Employee' : [20, 10, 30, 5, 3]
        }
s = pd.Series(data)
s


# In[94]:


# DataFrame 으로 변환

s = pd.DataFrame(data)
s


# In[95]:


s.columns


# In[96]:


s.index


# In[97]:


s.index=['one','two','three','four','five']
s.columns = ['a','b','c','d']
s


# In[98]:


import pandas as pd
import os

csv_path = os.getenv("HOME") + "/aiffel/data_represent/data/covid19_italy_region.csv"
data = pd.read_csv(csv_path)
type(data)


# In[99]:


data


# In[100]:


data.head()


# In[101]:


data.tail()


# In[102]:


data.head(3)


# In[103]:


data.columns


# In[104]:


data.info()


# In[105]:


data.describe()


# In[106]:


data.isnull().sum()


# In[107]:


data['RegionName'].value_counts()


# In[108]:


data['Country'].value_counts()


# In[109]:


data['RegionName'].value_counts().sum()


# In[110]:


data['Country'].value_counts().sum()


# In[111]:


print(data['TotalPositiveCases'].sum())
print(data['TestsPerformed'].sum())
print(data['Deaths'].sum())
print(data['Recovered'].sum())


# In[112]:


data.sum()


# In[113]:


print(data['TestsPerformed'].corr(data['TotalPositiveCases']))
print(data['TestsPerformed'].corr(data['Deaths']))
print(data['TotalPositiveCases'].corr(data['Deaths']))

data.corr()


# In[114]:


data.drop(['Latitude','Longitude','Country','Date','HospitalizedPatients',  'IntensiveCarePatients', 'TotalHospitalizedPatients','HomeConfinement','RegionCode','SNo'], axis=1, inplace=True)

data.corr()


# In[115]:


import numpy as np


# In[116]:


np.arange(36).reshape(3,4,3)


# In[ ]:




