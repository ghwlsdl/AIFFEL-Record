#!/usr/bin/env python
# coding: utf-8

# In[1]:


def hello():
    print('Hello, world!')


# In[2]:


hello()


# In[3]:


def hello():
    pass


# In[4]:


def add(a, b):
    print(a + b)


# In[5]:


add(10 , 20)


# In[6]:


def 함수이름(매개변수):
    """독스트링"""
    코드
    
def 함수이름(매개변수):
    """
    여러 줄로 된
    독스르일
    """
    코드


# In[7]:


def add(a, b):
    """이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수입니다."""
    return a + b
 
x = add(10, 20)       # 함수를 호출해도 독스트링은 출력되지 않음
print(x)
 
print(add.__doc__)    # 함수의 __doc__로 독스트링 출력


# In[8]:


help(add)


# In[12]:


def add(a, b):
    return a + b

x = add(10, 20)


# In[13]:


x


# In[19]:


print(add(10, 20))


# In[20]:


def add_sub(a, b):
    return a + b, a - b


# In[21]:


x, y = add_sub(10, 20)


# In[22]:


x


# In[23]:


y


# In[24]:


x = add_sub(10, 20)


# In[25]:


x


# In[26]:


x, y = (30, -10)


# In[27]:


x


# In[28]:


y


# In[31]:


def one_two():
    return (1, 2)


# In[30]:


1, 2


# In[32]:


def one_two():
    return 1, 2


# In[33]:


def one_two():
    return [1, 2]


# In[34]:


x, y = one_two()


# In[35]:


print(x, y)


# In[36]:


def mul(a, b):
    c = a * b
    return c

def add(a, b):
    c = a + b
    print(c)
    d= mul(a, b)
    print(d)
    
x = 10
y = 20
add(x,y)


# In[37]:


# 29.5 함수의 호출 과정 알아보기 어렵다 ㅠㅠ


# In[ ]:


표준 입력으로 숫자 두 개가 입력됩니다.
다음 소스 코드를 완성하여 두 숫자의 덧셈, 뺄셈, 곱셈,
나눗셈의 결과가 출력되게 만드세요.
이때 나눗셈의 결과는 실수라야 합니다.

# input = x, y
# out = 각각의 사칙연산의 결과물


# In[38]:


x, y = map(int, input().split())


# In[40]:


add = x + y


# In[41]:


print(add)


# In[42]:


sub = x - y


# In[43]:


print(sub)


# In[44]:


mul = x * y


# In[45]:


print(mul)


# In[46]:


div = x / y


# In[47]:


print(div)


# In[ ]:


x, y = map(int, input().split()) # function 화의 이유


# In[53]:


def calculater(x, y):
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
    
    return add, sub, mul, div #return 의 이유? 함수 안에서 돌출 될 수 있기 때문? 값을 반환하려고?


# In[51]:


x, y = map(int, input().split())


# In[52]:


print(calculater(x, y))


# In[54]:


print(10, 20, 30)


# In[60]:


def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)


# In[61]:


print_numbers(10, 20, 30)


# In[62]:


x = [10, 20, 30]


# In[63]:


print_numbers(*x)


# In[68]:


def paint_numbers(*args):
    for arg in args:
        print(arg)


# In[70]:


print_numbers(10)


# In[71]:


print_numbers(10, 20, 30, 40)


# In[72]:


def print_numbers(a, *args):
    print(a)
    print(args)


# In[73]:


print_numbers(1)


# In[74]:


print_numbers(1, 10, 20)


# In[75]:


print_numbers(*[10, 20, 30])


# In[76]:


def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)


# In[77]:


personal_info('홍길동', 30, '서울시 용산구 이촌동')


# In[78]:


personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')


# In[79]:


def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)


# In[80]:


x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}


# In[81]:


personal_info(**x)


# In[82]:


personal_info(*x)


# In[83]:


def personal_info(**kwargs):
     for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')


# In[84]:


personal_info(name='홍길동')


# In[85]:


personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')


# In[86]:


x ={'name' : '홍길동'}


# In[87]:


personal_info(**x)


# In[88]:


y = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}


# In[90]:


personal_info(**y)


# In[91]:


def personal_info(**kwargs):
    if 'name' in kwargs:    # in으로 딕셔너리 안에 특정 키가 있는지 확인
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])


# In[92]:


def personal_info(name, **kwargs):
    print(name)
    print(kwargs)


# In[93]:


personal_info('홍길동')


# In[95]:


personal_info('홍길동', age=30, address='서울시 용산구 이촌동')


# In[96]:


personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})


# In[97]:


def custom_print(*args, **kwargs):
    print(*args, **kwargs)


# In[99]:


custom_print(1, 2, 3, sep=':', end='')


# In[100]:


def personal_info(name, age, address='비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)


# In[102]:


personal_info('홍길동', 30)


# In[103]:


personal_info('홍길동', 30, '서울시 용산구 이촌동')


# In[107]:


# 어렵다 ㅠㅠ
def personal_info(name, address='비공개', age):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)


# In[109]:


#표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
#다음 소스 코드를 완성하여 가장 높은 점수, 가장 낮은 점수,
#평균 점수가 출력되게 만드세요.
#평균 점수는 실수로 출력되어야 합니다.

# input = 국어, 영어, 수학, 과학 점수
# output = 가장 높은 점수와 낮은 점수, 평균 점수가 출력 되게 만드세요.

korean, english, mathematics, science = map(int, input().split())

def cal(kor=0, eng=0, mat=0, sci=0):
        maxi = max([kor,eng,mat,sci])
        mini = min([kor,eng,mat,sci])
        
        return maxi, mini

print(cal(korean, english, mathematics, science))


# In[ ]:





# In[ ]:




