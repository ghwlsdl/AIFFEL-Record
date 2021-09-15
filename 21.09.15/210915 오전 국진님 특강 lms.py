#!/usr/bin/env python
# coding: utf-8

# In[1]:


#랜덤변수와 확률 이해하기


# In[2]:


import random


# In[8]:


# 주사위 던지기를 시행

throwing_number = 10

# 주사기 던지기 시행의 결과를 random_dise라는 리스트에 저장

random_dise = [random.randint(1, 6) for i in range(throwing_number)]
random_dise


# In[9]:


# 주사기 던지기 사건에 대한 랜덤 변수 생성
random_var_dict = {i:0 for i in range(1, 7)}
random_var_dict


# In[17]:


# 주사기의 랜덤변수에 대한 확률을 할당
# ramdo,_var_dict의 item레 들어가는 확률을 계산하고 할당.
# Mint : 리스트 객체는 .count(elem) 을 통해 element가 몇 개 있는지 셀 수 있다.


# 지현님
random_var_dict = {i:random_dise.count(i)/throwing_number for i in range(1,7)}
print(random_var_dict)

# 이후는 오늘 올려주시는 국진 님 자료 보고 하자구나


# In[22]:


# 국진님 자료 참고하기

import matplotib.pyplot as plt

x = random_var_dict.keys()
p = random_var_dict.values()
plt.okit(x,p)
plt.legnd()
plt. show()


# In[20]:


#기댓값 (평균)


# In[ ]:


# Himt : 기존의 random_var 딕셔너리 사용
# 주사위 랜덤 변수에 대한 기댓값을 계산합니다.

expectation = 0
for 


# In[23]:


# 준영님
exp = 0
for key, value in random_var_dict.items():
    exp += key*value
    print(exp)


# In[24]:


# 지현님
expectation = 0
for key, value in random_var_dict.items():
    expectation += key * value
print(expectation)


# In[26]:


# 태균님
expectation = 0
for i, j in enumerate(random_var_dict.values()):
    expectation += (i+1) * j
print(expectation)


# In[ ]:


# 분산 구하기


# In[28]:


var = 0
# hint : 계산한 expectation 값을 활용해야합니다.

x = [1, 2, 3, 4, 5, 6]
p = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
mean = 3.5
var = 0
for x_i, p_i in zip(x,p):
    var += (x_i - mean)**2 * p_i
print(var)


# In[29]:


exp = 0
exp_square = 0
for key, value in random_var_dict.items():
    exp += key*value
    exp_square += (key**2)*value
    
var = exp_square - exp**2
print(var)


# In[ ]:


# 번외) 주사위 기댓값, 분산 구하기

# from sympy.stats
# import E, Die, variance x = Die('x', 6)
# print(f"expectation: {float(E(x))}, variance: {float(variance(x))}")

