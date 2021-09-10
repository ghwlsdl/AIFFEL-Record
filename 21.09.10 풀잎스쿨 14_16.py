#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 5
if x == 10:
    print('10입니다.')
else:
    print('10이 아닙니다')


# In[9]:


x = 5

if x == 10:
    y = x
else:
    y =0
    
    y


# In[7]:


x = 5
y = x if x == 10 else 0
y


# In[10]:


x = 5

if x == 10:
    print('10입니다.')
else:
print('x에 들어 있는 숫자는') #unexpected indent 에러발생
    print('10이 아닙니다.')


# In[15]:


x = 10


if x == 10:
    print('10입니다.')
else:
    print('x에 들어있는 숫자는')

print('10이 아닙니다.')


# In[17]:


if 0:
    print('참')
else: print('거짓')
    
if 1:
    print('참')
else:
    print('거짓')


# In[18]:


if 'Hello':    # 문자열
    print('참')    # 문자열은 참
else:
    print('거짓')
 
if '':    # 빈 문자열
    print('참')
else:
    print('거짓')    # 빈 문자열은 거짓


# In[19]:


if not 0:
    print('참')    # not 0은 참
 
if not None:
    print('참')    # None은 참
 
if not '':
    print('참')    # not 빈 문자열은 참


# In[20]:


x = 10
y = 20
 
if x == 10 and y == 20:     # x가 10이면서 y가 20일 때
    print('참')
else:
    print('거짓')


# In[21]:


if x > 0:
    if x < 20:
        print('20보다 작은 양수입니다.')


# In[22]:


if x > 0 and x < 20:
    print('20보다 작은 양수입니다.')


# In[23]:


if 0 < x < 20:
    print('20보다 작은 양수입니다.')


# In[24]:


x = 20
if x == 10:
     print('10입니다.')
elif x == 20:
    print('20입니다.')


# In[26]:


x = 30

if x == 10:
    print('10입니다.')
elif x == 20:
    print('20입니다.')
else:
    print('10도 20도 아닙니다.')
    
#순서는 if, elif, else 순으로 진행해야 합니다.


# In[1]:


button = int(input())

if button == 1:
    print('콜라')
elif button == 2:
    print('사이다')
elif buttion == 3:
    print('환타')
else:
    print('제공하지 않는 메뉴')


# In[2]:


x = int(input())

if 11 <= x <=20:
    print('11~20')
elif 21 <= x <=30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')


# In[3]:


price = int(input())
coupon = int(input())

if coupon == 3:
    price -= 3000
    
elif coupon == 5:
    proce -= 5000
    
else:
    price = ('잘 못 된 쿠폰 입니다.')
    
print(price)


# In[4]:


for i in range(100):
    print('Hello, world!')


# In[5]:


for i in range(100):
    print('Hello, world', i)


# In[6]:


for i in range(5, 12):
    print('Hello, world', i)


# In[7]:


for i in range(0,10,2):
    print('Hello, world', i)


# In[9]:


for i in range(10,0, -1):
    print('Hello, world', i)


# In[10]:


for i in reversed(range(10)):
    print('Hello, world', i)


# In[12]:


count = int(input('반복할 횟수를 입력하세요: '))

for i in range(count):
    print('Hello, world', i)


# In[13]:


a = [10, 20, 30, 40, 50]

for i in a:
    print(i)


# In[14]:


fruits = ('apple', 'orange', 'grape')

for fruit in fruits:
    print(fruit)


# In[16]:


for letter in 'Python':
    print(letter, end=' ')


# In[17]:


for letter in reversed('Python'):
    print(letter, end=' ')


# In[18]:


for i in range(10,0)


# In[19]:


# 1. 정수 입력
# 1-1. 몇 번 반복할 지 반복할 것인가
# 2. 출력 형식은 숫자 * 숫자 = 숫자
# 3. 숫자와 *, = 사이의 공백을 한 칸 띄웁니다.

number = int(input())

for i in range(1, 9+1):
    print(number, '*', i, '=', number * i)

print(list(range(1,9+1)))


# In[ ]:




