#!/usr/bin/env python
# coding: utf-8

# In[2]:


#y=f(x)


# In[3]:


print("안녕하세요")


# In[4]:


def print2(input1, input2):
    print(input1)
    print(input2)
    return input1, input2


# In[5]:


# 호출 (둘의 차이는 무엇인가? ()가 있으면, 함수입니다.)
print
print("호출")


# In[9]:


#ingredient는 텍스트
def frying_pan(ingredient1, ingredient2):
    cooked = ingredient1 + ingredient2
    return cooked

#출력
print(frying_pan("김치", "볶음밥")


# In[8]:





# In[10]:


say_hi_nice()


# In[15]:


def say_hi():
    print('안녕')

def say_hi_nice():
    print('안녕!')
    print('반가워.')
    
say_hi_nice()


# In[16]:


def say_hi_somebody(name):
    print(name + ', 안녕!')
    
say_hi_somebody('준이')


# In[18]:


def say_hi_default(name='somebody'):
    print('안녕, ' + name + '!')
    
say_hi_default('준이')


# In[19]:


say_hi_default()


# In[24]:


def say_hi_couple(name1, name2):
    print(name1 + ', ' + name2 + ' 안녕!')
    
say_hi_couple(name1='그리', name2='단테')


# In[25]:


def add(number1, number2):
    print(number1 + number2)
    
add(1,2)


# In[26]:


def add_and_return(number1, number2):
    print(number1 + number2)
    return number1 + number2

print(add_and_return(1,2) + 3)


# In[27]:


def print_two(word1, word2):
    print(word1)
    print(word2)

def print_and_return(word1, word2, word3):
    print_two(word3, word2)
    return word1

print_two('1', print_and_return("2", "3", "4"))


# In[28]:


def print_if_positive(number):
    if number >= 0:
        print(number)
#- 숫자가 0보다 크거나 같을(>=) 경우 즉, 0 이상일 경우에만 숫자를 출력합니다.

print_if_positive(1)
print_if_positive(-1)


# In[29]:


def print_whether_positive_or_negative(number):
    if number >=0:
        print('+')
    else:
        print('-')
        
print_whether_positive_or_negative(1)
print_whether_positive_or_negative(-1)


# In[30]:


def print_whether_positive_or_negative_or_zero(number):
    if number > 0:
        print('+')
    elif number == 0:
        print('0')
    else:
        print('-')
#- 숫자가 양수이면 +를, 음수이면 -를, 양수도 음수도 아닌 0일 경우 그대로 0을 출력합니다.

print_whether_positive_or_negative_or_zero(1)
print_whether_positive_or_negative_or_zero(0)
print_whether_positive_or_negative_or_zero(-1)


# In[32]:


def print_if_positive_and_even(number):
    if (number > 0) and (number % 2 == 0):
        print(number)

#- 숫자가 양수이고(and) 짝수일 때 해당 숫자를 출력합니다.
#-- 양수 : number > 0
#-- 짝수 : number % 2 == 0 즉, 숫자를 2로 나눈 나머지가 0인 경우

print_if_positive_and_even(6)
print_if_positive_and_even(4)
print_if_positive_and_even(2)
print_if_positive_and_even(8)


# In[33]:


print(type(1))


# In[34]:


print(type(True))
print(type(False))


# In[35]:


conductor = {'first_name': '단테', 'last_name': '안'}
conductor['gender'] = 'male'
print(conductor)


# In[36]:


conductor = {'first_name': '단테', 'last_name': '안'}
for key, value in conductor.items():
    print(key + ' : ' + value)


# In[41]:


def fibonacci(n):
    if n <= 2:
        number = 1
    else:
       number = fibonacci(n-1) + fibonacci(n-2)
    return number

print(fibonacci(20))


# In[43]:


memory = {1: 1, 2: 1}

def fibonacci(n):
    if n in memory:
        number = memory[n]
    else:
       number = fibonacci(n-1) + fibonacci(n-2)
       memory[n] = number
    return number

print(fibonacci(100))

print(memory)


# In[52]:


import numpy as np

MU = 0
SIGMA = 1
PI = np.pi

#힌트 : 루트는 np.sqrt() 사용, 자연상수는 np.exp() 사용

def gaussian(x, MU, SIGMA):
    
#     gaussian(x, MU, SIGMA) = 1 % {SIGMA * np, sqrt(2 * np, pi)} * e ** {-1 * (x-MU) ** 2 % 2 * SIGMA ** 2}
    
    out = (1/np.squrt(2*PI)/SIGMA)*np.exp(-1*((x-MU)**2/(2*SIGMA**2)))
    
    return out
    


# In[56]:


#a는 nrlfdldml qprxjfh fltmxmfmf xhdgo vygus
# ex  a = [0.1, 0.2, 0.7]
# 소프트맥스의 반환값 또한 벡터로 구현

def softmax(a):
    sum = 0
    for item in a:
        sum += np.exp(item)
    
    y = []
    for item in a:
        y.append(np.exp(item)/sum)
    return y


# In[57]:


a = [0.1, 0.2, 0.7]
print(softmax(a))


# In[ ]:




