#!/usr/bin/env python
# coding: utf-8

# In[1]:


클래스


# In[2]:


클래스? -> 인스턴스를 만드는 틀.

클래스 : 붕어빵틀
인스턴스 : 붕어빵
    
클래스를 통해 여러 개의 변수를 관리하고자 함.


# In[ ]:


variabl31 = 3
variable = "사과"
variable = [1, 2, 3]


# In[3]:


class FishBread:
    pric = 500
    category = "슈프림"


# In[5]:


#클래스를 통해 생성된 객체는 인스턴스라고 부른다.
fb = FishBread()
fb2 = FishBread()

# fb, fb2 는 FishBread 클래스의 인스턴스들이다.


# In[16]:


class MakeFishBread:
    #맴버변수 : 클래스 내부에 속한 변수.
    price = None
    caregory = None
    __passward =None #__가 붙으면 private 맴버변수를 의미합니다.
    
    #생성자 : 인스턴스를 생성할 때 가장 먼저 호출하는 함수
    #self 키워드 : 변수나 함수가 이 클래스 내부에 속하는 것을 말합니다.
    def __init__(self, price, category):
        self.price = price
        self.category = category
        self.__password = password
        
    #매소드 : 클래스 내부의 맴버함수를 의미한다.
    # 맴버변수를 새로 할당한 매소드를 setter라고 한다.
    # 맴버변수를 반환하는 매소드를 getter라고 한다.
        
    def set_price_and_category(self, price, category):
        self.price = price
        self.category = category
        
    def get_password(self, password):
        if password == self.__password:
            
           return self.password
    
    ------------- 야발 하나도 못 따라가겠다... 저녁에 다시 보자구나
        
    def get_price_and_category(self):
        return (self.pric, self.catrgory)
    
        
bread1 = MakeFishBread(500, "팥")

# . 맴버접근연산자
print(bread1.price)
print(bread1.category)

print(isinstance(bread1, MakeFishBread))
print(isinstance(bread1,int)
      
# 결국 bread1이라는 인스턴스는 MakeFishBread라는 자료형으로 생각할 수 있다.      
print(type(bread1))
      
bread1.set_price(700)
print(bread1.price)


# In[7]:


bread2 = MakeFishBread(700, "슈프림", 1234)
#bread2.__password
bread2.get


# In[ ]:


class Student:
#     __id = None
#     __pw = None #private
#     name = None
    
    def __init__(self, __id, pw, name):
        self.__id = __id
        self.__pw = pw
        self.name = name
        
    def get_id(self):
        pass
    
    def get_pw(self):
        pass
    
    def set_id(self, __id):
        pass
    
    def set_pw(self, __pw):
        pass
    
    #1 클래스 완성하기
    #2 인스턴스 만들기
    #3 매소드 이용해 id, pw를 변경해보기.
        

