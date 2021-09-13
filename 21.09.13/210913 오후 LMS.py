#!/usr/bin/env python
# coding: utf-8

# In[1]:


#class

#1. 생성자
#2. 인스터스
#3. 메소드
#4. self
#5. 멤버변수
#6. 멤버접근연산자


# In[2]:


x, y = 1, 2


# In[3]:


x = 3
y = 4

# 연산하기가 귀찮다!


# In[11]:


class Point2D:
    def __init__(self, x, y):
        #맴버변수의 속성 : 파이썬에서는 private, public이 존재합니다.
        #private : 맴버접근 연사자를 통해 맴버 변수나 애소드에 직접 전근이 불가합니다. __ (underbar) 2개를 붙여서 만듭니다.
        #public : 맴버접근 연산자를 통해 자유롭게 접근할 수 있습니다.
       
        self.___x = x
        self.___y = y
        
        #getter 메소드 : pravate 맴버변수를 가져오고 싶을 때 보통 구현을 합니다.
        def get_xy(self):
            return (self.__x, self.__y)
        
        def get_x(self):
            return self.__x
        
        def get_y(self):
            return self.__y
        
        #setter 메소드 : 맴버변수를 변경하고 싶을 떄 사용합니다.
        def set_xy(self, x, y):
            self.__x = x
            self.__y = y


# In[12]:


point = Point2D(1,1)
#print(point.__x)
point.__x = 3
#print(point.__x)
print(point.get_x())
print(point.get_xy())

#접근을 하지 못한 이유는 private 하기 떄문입니다.


# In[13]:


print("--- 변경후")
point.set_xy(2,2)
print(point.get_x())
print(point.get_xy())


# In[14]:


#클래스의 상속

get_ipython().set_next_input('많은 돈을 상속 받으면 삶이 편해지죠');get_ipython().run_line_magic('pinfo', '편해지죠')
많은 기능을 부모 클래스로부터  상속받으면 개발자의 삶이 매우 편해집니다.
즉, 동일한 기능을 또 구현할 필요가 없기 때문입니다.


# In[15]:


#상속을 받기 위해서는 괄호를 사용해서 부모 클래스의 이름을 적어줘야한다.
# Point3D 클래스를 Point2D 클래스의 자식클래스라고 한다.

class Point3D(Point2D):
    def __init__(self. x, y, z):
        # super()
        super().__init__(x,y)
        self.__x = super().get_x()
        # 자식클래스는 부모 클래스의 pravate 맴버변수에 접근하지 못한다!
        # 따라서 getter를 써야한다.
        self.__y = super().get_y()
        self.__z = 


# In[ ]:


#메소드 오버라이딩 : 부모클래스의 메소드를 자식클래스에서 재정의합니다.

daf get_cood(self):
    return (self.__x, self.__y, self.__z)

def set

#추가 사진 보고 복습 & 숙제 해결할 것!

