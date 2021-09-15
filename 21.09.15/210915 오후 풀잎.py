#!/usr/bin/env python
# coding: utf-8

# In[1]:


#unit 34


# In[3]:


class Person:
     def greeting(self):
            print('Hello')


# In[4]:


# 인스턴스 = 클래스 ()

james = Person()


# In[5]:


james.greeting()


# In[6]:


a = int(10)


# In[7]:


a


# In[8]:


b = list(range(10))


# In[9]:


b


# In[11]:


c = dict(x=10, y=20)


# In[12]:


c


# In[13]:


b = list(range(10))


# In[14]:


b.append(20)


# In[15]:


b


# In[17]:


a = 10


# In[18]:


type(a)


# In[19]:


a = list(range(10))


# In[21]:


b = list(range(10))


# In[22]:


# 빈 클래스 만들기
class Person:
    pass


# In[26]:


# 메서드 안에서 메서드 호출하기

class Person:
    def greeting(self):
        print('Hello')
 
    def hello(self):
        self.greeting()    # self.메서드() 형식으로 클래스 안의 메서드를 호출
 
james = Person()
james.hello()    # Hello


# In[27]:


# 특정 클래스의 인스턴스인지 확인하기


# In[28]:


class Person:
    pass

james = Person()
isinstance(james, Person)


# In[29]:


def factorial(n):
    if not isinstance(n, int) or n < 0:    # n이 정수가 아니거나 음수이면 함수를 끝냄
        return None
    if n == 1:
        return 1
    return n * factorial(n - 1)


# In[30]:


class Person:
    def __init__(self): #__init__ 는 클래스에서 인스턴스를 만들 때 호출하는 메서드 입니다.
        self.hello = '안녕하세요.'
 
    def greeting(self):
        print(self.hello)
 
james = Person()
james.greeting()    # 안녕하세요.


# In[32]:


def greeting(self):
    print(self.hello)


# In[33]:


james = Person()
james.greeting()    # 안녕하세요.


# In[34]:


# 인스턴스를 만들 때 값 받기

class 클래스이름:
    def __init__(self, 매개변수1, 매개변수2):
        self.속성1 = 매개변수1
        self.속성2 = 매개변수2


# In[35]:


class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address
 
    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))
 
maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()    # 안녕하세요. 저는 마리아입니다.
 
print('이름:', maria.name)       # 마리아
print('나이:', maria.age)        # 20
print('주소:', maria.address)    # 서울시 서초구 반포동


# In[36]:


def __init__(self, name, age, address):
    self.hello = '안녕하세요.'
    self.name = name
    self.age = age
    self.address = address


# In[37]:


def greeting(self):
    print('{0} 저는 {1}입니다.'.format(self.hello, self.name))


# In[38]:


maria = Person('마리아', 20, '서울시 서초구 반포동')


# In[40]:


maria.greeting()


# In[41]:


class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]
 
maria = Person(*['마리아', 20, '서울시 서초구 반포동'])


# In[42]:


class Person:
    def __init__(self, **kwargs):    # 키워드 인수
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']
 
hojin1 = Person(name='이호진', age=29, address='서울시 관악구 대학동')
hojin2 = Person(**{'name': '이호진', 'age': 29, 'address': '서울시 관악구 대학동'})


# In[43]:


class Person:
    pass

hojin = Person()
hojin.name = '이호진'
hojin.name


# In[45]:


james = Person()    # james 인스턴스 생성
james.name    # maria 인스턴스에만 name 속성을 추가했으므로 james 인스턴스에는 name 속성이 없음
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    james.name
AttributeError: 'Person' object has no attribute 'name'


# In[47]:


class Person:
    def greeting(self):
        self.hello = '안녕하세요'    # greeting 메서드에서 hello 속성 추가

maria = Person()
maria.hello    # 아직 hello 속성이 없음

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    maria.hello
AttributeError: 'Person' object has no attribute 'hello'

maria.greeting()    # greeting 메서드를 호출해야

maria.hello         # hello 속성이 생성됨
'안녕하세요'


# In[48]:


class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address


# In[49]:


hojin = Person('이호진', 29, '서울시 관악구 대학동')


# In[51]:


hojin.name


# In[52]:


hojin.age


# In[53]:


hojin.address


# In[54]:


class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet    # 변수 앞에 __를 붙여서 비공개 속성으로 만듦
 
hojin = Person('이호진', 20, '서울시 관악구 대학동', 10000)
hojin.__wallet -= 10000    # 클래스 바깥에서 비공개 속성에 접근하면 에러가 발생함


# In[59]:


class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet    # 변수 앞에 __를 붙여서 비공개 속성으로 만듦
 
    def pay(self, amount):
        self.__wallet -= amount   # 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
        print('이제 {0}원 남았네요.'.format(self.__wallet))
 
hojin = Person('이호진', 20, '서울시 관악구 대학동', 10000)
hojin.pay(3000)


# In[60]:


def pay(self, amount):
        if amount > self.__wallet:    # 사용하려고 하는 금액보다 지갑에 든 돈이 적을 때
            print('돈이 모자라네...')
            return
        self.__wallet -= amount


# In[61]:


class Person:
    def __greeting(self):
        print('Hello')
 
    def hello(self):
        self.__greeting()    # 클래스 안에서는 비공개 메서드를 호출할 수 있음
 
hojin = Person()
hojin.__greeting()    # 에러: 클래스 바깥에서는 비공개 메서드를 호출할 수 없음


# In[62]:


class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
 
    def slash(self):
        print('베기')

x = Knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()


# In[ ]:


Q. 표준 입력으로 게임 캐릭터 능력치(체력, 마나, AP)가 입력됩니다.

다음 소스 코드에서 애니(Annie) 클래스를 작성하여 티버(tibbers)

스킬의 피해량이 출력되게 만드세요. 티버의 피해량은 AP * 0.65 + 400이며

AP(Ability Power, 주문력)는 마법 능력치를 뜻합니다.

--------------------------------------------------------

health, mana, ability_power = map(float, input().split())
 
x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()


# In[78]:


class Annie:
    # 인자를 사용한 이유? 애니의 능력치를 받기 위해서???
    # 클래스는 개념일뿐 실행하려면 인스턴스를 정의해야하기 때문입니다.
    # 클래스 Annie는 붕어빵틀 일 뿐, 붕어빵 속을 채우기 위해서 인자를 사용합니다.
    
    def __init__(self, health, mana, AP):
        self.health = health
        self.mana = mana
        self.AP = AP
        
        #self 사용이유? 인스턴스 본인의 변수임을 알려주기 위해서.
        
    def tibber(self):    #self 만 들어가도 되는 이유? 위에서 인자를 지정 받아서??
        damage = self.AP * 0.65 + 400    #self 사용 이유? 인스터스에서 받은 AP를 대입 받아야 하기 떄문
        return damage  


# In[80]:


a = Annie(511.68, 334.0, 298)


# In[81]:


print(a.tibber())  #tibber 도 함수 이므로 ()가 들어가야합니다.


# In[82]:


a.health


# In[83]:


a.mana


# In[84]:


a.AP


# In[85]:


a.damage


# In[87]:


print(a.tibber)   # ()가 없을 시, tibber 함수가 나옵니다.


# In[ ]:


# 비공개 속성의 사용이유? 엄밀하게 하기 위해 사용할 수 있으나, 필수는 아님


# In[88]:


b = Annie(100, 200, 300)


# In[89]:


print(b.tibber())


# In[90]:


class Person:
    def greeting(self):
        print('안녕하세요.')
 
class Student(Person):
    def study(self):
        print('공부하기')
 
james = Student()
james.greeting()    # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.study()       # 공부하기: 파생 클래스 Student에 추가한 study 메서드


# In[91]:


class Person:
    def greeting(self):
        print('안녕하세요.')
 
class PersonList:
    def __init__(self):
        self.person_list = []    # 리스트 속성에 Person 인스턴스를 넣어서 관리
 
    def append_person(self, person):    # 리스트 속성에 Person 인스턴스를 추가하는 함수
        self.person_list.append(person)


# In[92]:


class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
 
class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school = '파이썬 코딩 도장'
 
james = Student()
print(james.school)
print(james.hello)    # 기반 클래스의 속성을 출력하려고 하면 에러가 발생함


# In[93]:


class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
 
class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()                # super()로 기반 클래스의 __init__ 메서드 호출
        self.school = '파이썬 코딩 도장'
 
james = Student()
print(james.school)
print(james.hello)


# In[95]:


# 기반 클래스를 초기화하지 않아도 되는 경우

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
 
class Student(Person):
    pass
 
james = Student()
print(james.hello)


# In[96]:


# 좀 더 명확하게 super 사용하기

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super(Student, self).__init__()     # super(파생클래스, self)로 기반 클래스의 메서드 호출
        self.school = '파이썬 코딩 도장'


# In[97]:


class Person:
    def greeting(self):
        print('안녕하세요.')
 
class Student(Person):
    def greeting(self):
        print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')
 
james = Student()
james.greeting()


# In[98]:


# 오버라이딩 사용 이유? 
# 보통 프로그램에서 어떤 기능이 같은 메서드 이름으로 계속 사용되어야 할 때,
# 메서드 오버라이딩을 활용합니다.


# In[99]:


class Person:
    def greeting(self):
        print('안녕하세요.')
 
class Student(Person):
    def greeting(self):
        super().greeting()    # 기반 클래스의 메서드 호출하여 중복을 줄임
        print('저는 파이썬 코딩 도장 학생입니다.')
 
james = Student()
james.greeting()


# In[100]:


class Person:
    def greeting(self):
        print('안녕하세요.')
 
class University:
    def manage_credit(self):
        print('학점 관리')
 
class Undergraduate(Person, University):
    def study(self):
        print('공부하기')
 
james = Undergraduate()
james.greeting()         # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.manage_credit()    # 학점 관리: 기반 클래스 University의 메서드 호출
james.study()            # 공부하기: 파생 클래스 Undergraduate에 추가한 study 메서드


# In[101]:


james = Undergraduate()
james.greeting()         # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.manage_credit()    # 학점 관리: 기반 클래스 University의 메서드 호출
james.study()            # 공부하기: 파생 클래스 Undergraduate에 추가한 study 메서드


# In[102]:


class A:
    def greeting(self):
        print('안녕하세요. A입니다.')
 
class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')
 
class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')
 
class D(B, C):
    pass
 
x = D()
x.greeting()    # 안녕하세요. B입니다.


# In[103]:


int.mro()


# In[ ]:


# 다음 소스 코드에서 동물 클래스 Animal 과 조류 클래스 Wing 를 상속 받아 새 클라스
# Bird 를 작성하여 '먹다', '파닥거리다', '날다'
# 파충류, 양서류, 어류, 조류


# In[104]:


class Animal:
    
    
    def __init__(self.breathe, eat):
        self.breathe = breathe
        self.eat = eat
        
class Wing(Animal):
    
    def __init__(self.breathe, eat, fly):
        super().__init__(breathe, eat) # __init__도 함수 이기 때문에 괄호가 필요합니다.
        self.fly = fly
        
lion = Animal('air', 'meet')
sparrrow = Wing('air', 'banban', 'True')

print(lion.eat)
print(sparrow.eat)

# 너무 어렵다 ㅠㅜ


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




