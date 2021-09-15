# Q. 표준 입력으로 게임 캐릭터 능력치(체력, 마나, AP)가 입력됩니다.

# 다음 소스 코드에서 애니(Annie) 클래스를 작성하여 티버(tibbers)

# 스킬의 피해량이 출력되게 만드세요. 티버의 피해량은 AP * 0.65 + 400이며

# AP(Ability Power, 주문력)는 마법 능력치를 뜻합니다.

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

a = Annie(511.68, 334.0, 298)

print(a.tibber())  #tibber 도 함수 이므로 ()가 들어가야합니다.

#print(a.tibber)   # ()가 없을 시, tibber 함수가 나옵니다.

b = Annie(100, 200, 300)

print(b.tibber())