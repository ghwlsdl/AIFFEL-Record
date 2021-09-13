#!/usr/bin/env python
# coding: utf-8

# In[6]:


i = 1
while i <= 100:
    print('Hello, world!', i)
    i+= 1


# In[7]:


i = 100
while i > 0:
    print('Hello, world!', i)
    i -= 1


# In[9]:


count = int(input('반복할 횟수를 입력하세요: '))

i = 0
while i < count:
    print('Hello, world!', i)
    i += 1


# In[10]:


count = int(input('반복할 횟수를 입력하세요: '))
 
while count > 0:     # count가 0보다 클 때 반복
    print('Hello, world!', count)
    count -= 1       # count를 1씩 감소시킴


# In[18]:


import random


# In[20]:


random.randint(1, 6)


# In[21]:


random.randint(1, 6)


# In[22]:


random.randint(1, 6)


# In[23]:


import random    # random 모듈을 가져옴
 
i = 0
while i != 3:    # 3이 아닐 때 계속 반복
    i = random.randint(1, 6)    # randint를 사용하여 1과 6 사이의 난수를 생성
    print(i)


# In[24]:


dice = [1, 2, 3, 4, 5, 6]


# In[25]:


random.choice(dice)


# In[26]:


random.choice(dice)


# In[27]:


random.choice(dice)


# In[ ]:


#while True:
    print('Hello, world!')


# In[ ]:


i = 2
j = 5

while i <= 32 or j >=1:
    print(i, j)
    i *=2
    j -=1


# In[29]:


# 1회당 요금은 1,350원

count = int(input('반복할 횟수를 입력하세요: '))

while count > 0:
    print(i, count)
    i -=1350


# In[58]:


fee = 1350


# In[59]:


cash = int(input())


# In[60]:


while cash >= fee:
    cash = cash - fee
    print(cash)


# In[61]:


i = 0
while True:    # 무한 루프
    print(i)
    i += 1          # i를 1씩 증가시킴
    if i == 100:    # i가 100일 때
        break       # 반복문을 끝냄. while의 제어흐름을 벗어남


# In[62]:


for i in range(10000):
    print(i)
    if i == 100:
        break


# In[64]:


for i in range(100):
    if i % 2 == 0:
        continue
    print(i)


# In[66]:


i = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        continue
    print(i)


# In[68]:


count = int(input('반복할 횟수를 입력하세요: '))

i = 0
while True:
    print(i)
    i += 1
    if i == count:
        break


# In[69]:


count = int(input('반복할 횟수를 입력하세요: '))

for i in range(count +1):
    if i % 2 ==0:
        continue
    print(i)


# In[71]:


i = 0
while True:
    if i % 10 !=3:
        i += 1
        continue
    if i > 73:
        break
    print(i, end=' ')
    i +=1


# In[78]:


start, stop = map(int, input().split())

i = start

for i in range(start, stop+1): #for문 해답
    if 1%10==3:
        continue
    print(i)


# In[86]:


start, stop = map(int, input().split())

i = start

while start <= stop:
    a = str(start)
    start += 1
    if a.endswith('3'): continue
    print(a)
    


# In[80]:


a = 3
print(str(a).endswith('3')) #endsith는 앞 뒤로 str 해야 연산이 가능


# In[ ]:




