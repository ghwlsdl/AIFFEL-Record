#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
start = time.time()  # 시작 시간 저장

a = 1
for i in range(100):
	a += 1
 
# 작업 코드
print("time :", time.time() - start) # 결과는 '초' 단위 입니다.


# In[2]:


my_list = ['a', 'b', 'c', 'd']

for i in my_list:
    print("값 : ", i)


# In[3]:


my_list = ['a','b','c','d']

for i, value in enumerate(my_list):
    print("순번 : ", i, " , 값 : ", value)


# In[4]:


my_list = ['a','b','c','d']
result_list = []

for i in range(2):
    for j in my_list:
        result_list.append((i, j))
        
print(result_list)


# In[5]:


my_list = ['a','b','c','d']

result_list = [(i, j) for i in range(2) for j in my_list]

print(result_list)


# In[6]:


my_list = ['a','b','c','d']

# 인자로 받은 리스트를 가공해서 만든 데이터셋 리스트를 리턴하는 함수
def get_dataset_list(my_list):
    result_list = []
    for i in range(2):
        for j in my_list:
            result_list.append((i, j))
    print('>>  {} data loaded..'.format(len(result_list)))
    return result_list

for X, y in get_dataset_list(my_list):
    print(X, y)


# In[7]:


my_list = ['a','b','c','d']

# 인자로 받은 리스트로부터 데이터를 하나씩 가져오는 제너레이터를 리턴하는 함수
def get_dataset_generator(my_list):
    result_list = []
    for i in range(2):
        for j in my_list:
            yield (i, j)   # 이 줄이 이전의 append 코드를 대체했습니다
            print('>>  1 data loaded..')

dataset_generator = get_dataset_generator(my_list)
for X, y in dataset_generator:
    print(X, y)


# In[8]:


a = 10
b = 0
try:
    #실행 코드
    print(a/b)
		
except:
    #에러가 발생했을 때 처리하는 코드
    print('에러가 발생했습니다.')


# In[10]:


a = 10
b = 1

try:
    #실행 코드
    print(a/b)
		
except:
    #에러가 발생했을 때 처리하는 코드
    print('에러가 발생했습니다.')


# In[11]:


a = 10
b = 0 

try:
    #실행 코드
    print(a/b)
		
except:
    print('에러가 발생했습니다.')
    #에러가 발생했을 때 처리하는 코드
    b = b+1
    print("값 수정 : ", a/b)


# In[12]:


import time

num_list = ['p1','p2', 'p3', 'p4']
start = time.time()

def count(name):
    for i in range(0, 100000000):
        a = 1 + 2
        
    print("finish : ", name)

for num in num_list:
    count(num)

print("time :", time.time() - start)


# In[13]:


import multiprocessing
import time

num_list = ['p1','p2', 'p3', 'p4']
start = time.time()

def count(name):
    for i in range(0, 100000000):
        a = 1+2
    print("finish : ", name)
    

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes = 4)
    pool.map(count, num_list)
    pool.close()
    pool.join()

print("time :", time.time() - start)


# In[14]:


import multiprocessing

def count(name):
    for i in range(0, 100000000):
        a = 1 + 2
    print("finish : ",name)


# In[15]:


num_list = ['p1','p2', 'p3', 'p4']

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes = 4)
    pool.map(count, num_list)
    pool.close()
    pool.join()


# In[16]:


def function_f(input_x):
    output_x = input_x*input_x
    return ouput_x


# In[17]:


list_data = [10, 20, 30, 40]
list_data2 = [20, 30, 40, 50]

length = len(list_data)
max_result = list_data[0]
for i in range(length):
    if max_result < list_data[i]:
        max_result = list_data[i]
        
print("최댓값은 ", max_result)

length = len(list_data2)
max_result = list_data2[0]
for i in range(length):
    if max_result < list_data2[i]:
        max_result = list_data2[i]
        
print("최댓값은 ", max_result)


# In[18]:


list_data = [10, 20, 30, 40]
list_data2 = [20, 30, 40, 50]

def max_function(x):
    length = len(x)
    max_result = x[0]
    for i in range(length):
        if max_result < x[i]:
            max_result = x[i]
    return max_result

print("최댓값은 ", max_function(list_data))
print("최댓값은 ", max_function(list_data2))


# In[19]:


def empty_function():


# In[20]:


def empty_function():
    pass


# In[21]:


def say_something(txt):
    return txt

def send(function, count):
    for i in range(count):  
        print(function)
    
send(say_something("안녕!"), 2)


# In[22]:


list_data = [30, 20, 30, 40]

def minmax_function(x_list):
    
    def inner_min_function(x):
        length = len(x)
        min_result = x[0]
        for i in range(length):
            if min_result > x[i]:
                min_result = x[i]
        return min_result
    
    def inner_max_function(x):
        length = len(x)
        max_result = x[0]
        for i in range(length):
            if max_result < x[i]:
                max_result = x[i]
        return max_result
        
    x_min = inner_min_function(x_list)
    x_max = inner_max_function(x_list)
    
    minmax_list = [x_min, x_max]

    return minmax_list

print("최솟값, 최댓값은 : ", minmax_function(list_data))
print("최솟값은 : ", minmax_function(list_data)[0])
print("최댓값은 : ", minmax_function(list_data)[1])


# In[25]:


list_data = [30, 20, 30, 40]

def minmax_function(x_list):
    
    def inner_min_function(x):
        length = len(x)
        min_result = x[0]
        for i in range(length):
            if min_result > x[i]:
                min_result = x[i]
        return min_result
    
    def inner_max_function(x):
        length = len(x)
        max_result = x[0]
        for i in range(length):
            if max_result < x[i]:
                max_result = x[i]
        return max_result
        
    x_min = inner_min_function(x_list)
    x_max = inner_max_function(x_list)
    
    minmax_list = [x_min, x_max]

    return minmax_list

print("최솟값, 최댓값은 : ", minmax_function(list_data)[0]) # 변경
print("최솟값은 : ", minmax_function(list_data)[0])
print("최댓값은 : ", minmax_function(list_data)[1])


# In[26]:


list_data = [30, 20, 30, 40]

def minmax_function(x_list):
        
    def inner_min_function(x):
        length = len(x)
        min_result = x[0]
        for i in range(length):
            if min_result > x[i]:
                min_result = x[i]
        return min_result
    
    def inner_max_function(x):
        length = len(x)
        max_result = x[0]
        for i in range(length):
            if max_result < x[i]:
                max_result = x[i]
        return max_result
        
    x_min = inner_min_function(x_list)
    x_max = inner_max_function(x_list)
    
    return x_min, x_max

min_value, max_value = minmax_function(list_data)

print("최솟값은 : ", min_value)
print("최댓값은 : ", max_value)


# In[27]:


print( (lambda x,y: x + y)(10, 20) )


# In[28]:


def list_mul(x):
     return x * 2

result = list(map(list_mul, [1, 2, 3]))
print(result)

# 각 함수를 실행할 때마다 어떤 결과가 나오는지 궁금하다면 아래 주석을 풀고 실행해보세요! 
map_res = map(list_mul, [1, 2, 3])
print(map_res)
list_map_res = list(map_res)
print(list_map_res)


# In[29]:


result = list(map(lambda i: i * 2 , [1, 2, 3]))
print(result)


# In[30]:


(lambda x,y: x + y)(10, 20)


# In[31]:


# mycalculator.py

test = "you can use this module."

def add(a, b):
    return a + b
 
def mul(a, b):
    return a * b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b


class all_calc():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
 
    def mul(self):
        return self.a * self.b

    def sub(self):
        return self.a - self.b

    def div(self):
        return self.a / self.b


# In[32]:


code = '# mycalculator.py\ntest = "you can use this module."\n\ndef add(a, b):\n    return a + b\n \ndef mul(a, b):\n    return a * b\n\ndef sub(a, b):\n    return a - b\n\ndef div(a, b):\n    return a / b\n\n\nclass all_calc():\n\n    def __init__(self, a, b):\n        self.a = a\n        self.b = b\n\n    def add(self):\n        return self.a + self.b\n \n    def mul(self):\n        return self.a * self.b\n\n    def sub(self):\n        return self.a - self.b\n\n    def div(self):\n        return self.a / self.b'

f = open("mycalculator.py", "w")
f.write(code)
f.close()


# In[33]:


# import 모듈이름
import mycalculator


# In[34]:


# 모듈이름.함수이름()
print(mycalculator.add(4, 2))


# In[35]:


import mycalculator as mc

# 모듈이름.함수이름()
print(mc.add(4, 2))


# In[36]:


import mycalculator as mc

# 모듈이름.함수이름()
print(mc.sub(4, 2))


# In[37]:


import mycalculator as mc

# 모듈이름.함수이름()
print(mc.div(4, 2))


# In[38]:


import mycalculator as mc

# 모듈이름.함수이름()
print(mc.mul(4, 2))


# In[39]:


A = 5

def impure_mul(b):
    return b * A

print(impure_mul(6))


# In[40]:


def pure_mul(a, b):
    return a * b

print(pure_mul(4, 6))


# In[42]:


#generator.py

def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result

my_nums = square_numbers([1, 2, 3, 4, 5])

print(my_nums)


# In[45]:


def square_numbers(nums):
    for i in nums:
        yield i * i

my_nums = square_numbers([1, 2, 3, 4, 5])

print(next(my_nums))


# In[46]:


def square_numbers(nums):
    for i in nums:
        yield i * i

my_nums = square_numbers([1, 2, 3, 4, 5])

print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))


# In[48]:


def square_numbers(nums):
    for i in nums:
        yield i * i

my_nums = square_numbers([1, 2, 3, 4, 5])

print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))


# In[49]:


def square_numbers(nums):
    for i in nums:
        yield i * i

my_nums = square_numbers([1, 2, 3, 4, 5])

for num in my_nums:
    print(num)


# In[50]:


my_nums = [x*x for x in [1, 2, 3, 4, 5]]

print my_nums

for num in my_nums:
    print(num)


# In[51]:


# 제너레이터 : 이터레이터를 생성해주는 함수
# iterable(이터러블) :리스트, 튜플, 딕셔너리 같은 여러개의 원소들을 가지는 컨테이너 객체
# 이터레이터 : 이터러블에서 원소를 하.나.씩 꺼내오는 객체
# 프로그래밍을 할 떄는 극단적으로 생각하는 게 중요합니다.

def square(num_list):
    new_list = []
    for item in num_lisst:
        new_list.append(item * item)
    return new_list


# In[60]:


# num_list = []
# for i in range(100):
#    num_list_append(i)

num_list = []
for i in range(100):
    num_list.append(i)
    
num_list = [i for i in range(10)]
num_list = square(num_list)
for item in square(num_list):
    print(item)


# In[58]:


# iterable : 리스트, 튜플, 딕셔너리 등등
# iterator : iterable 객에에서 next를 통해 값을 하나씩 접근하게 해주는 객체

#iter() : 이터러블 객체를 이터레이터로 만들어준다.
num_list = [i for i in range(10)]
num_iterator = iter(num_list)

print(next(num_iterator))
print(next(num_iterator))

print()
print()
for item in num_iterator:
    print(item)

# 이터레이터는 내부 원소들을 하나씩 소모를 합니다.
# 메모리를 비우게 됩니다.


# In[61]:


# 제너레이터 : 이터레이터를 생성해주는 함수

def generate_sqaure(num_list):
    for item in num_list:
        yield item * item


# In[63]:


num_list = [i for i in range(10)]
num_iterator = generate_sqaure(num_list)
print(next(num_iterator))
print(next(num_iterator))

print()
print()

for item in num_iterator:
    print(item)


# In[ ]:




