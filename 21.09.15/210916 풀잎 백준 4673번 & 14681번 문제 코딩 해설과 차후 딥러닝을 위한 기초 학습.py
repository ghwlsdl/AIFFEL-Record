# 백준 4673번 문제

# n = 양의 정수

# d(n) = n + n의 1 번째 자리 숫자 + n의 2번째 자리 숫자 + n의 3번째 자리 숫자 + ... + n 번째 자리 숫자

# d(d(n)), d(d(d(n))), ...

# 위 식에서 n 이 되지 못하는 숫자를 셀프 숫자라고 한다.

# 예로는 1, 3, 5, 6, 9, 20, 31, ... 일 수 있는데, 이 때, 10000보다 작거나

# 같은 셀프 넘버 숫자를 한 줄에 하나 씩 출력하는 프로그램을 작성하시오.

# 4673번 문제 풀이

def self_number():   # self_number 정의
    arrange=list()   # list 정의
    result=None      # return 정의
    
    for i in range(1, 10001):
        
        if i < 10:
            result = i+i
            arrange.append(result)
            
        elif i < 100:
            result = i+(i//10)+(i%10)
            arrange.append(result)
            
        elif i < 1000:
            result = i+(i//100)+((i%100)//10)+((i%100)%10)
            arrange.append(result)
            
        elif i < 10000:
            result = i+(i//1000)+((i%1000)//100)+(((i%1000)%100)//10)+(((i%1000)%100)%10)
            if result <= 10000:
                arrange.append(result)
                
    arrange.sort() # 오름차순 정렬이 진행
    
    arrange1 = [i for i in range(1,10001)]
    
    notSelf = [item for item in arrange1 if item not in arrange]
    
    for each in notSelf:
        print(each)
 
self_number()

# 노가다 과정 보다는 최적화 작업을 하는 것이 용이하다.

# 4673번 해창님 최적화 코딩

numset = []

for i in range(1, 10001):
    numset.append(i + sum(map(int, list(str(i)))))
    if i in numset:
        continue
    print(i)

# 백준 14681번 상연님 코딩 풀이

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0  and y > 0:
    print(2)
elif x <0 and y <0:
    print(3)
else:
    print(4)

# 딥러닝을 하기 위해서 필요한 것으로는 다양한 것이 있습니다.

# 그리고 딥러닝을 하기 위한 다양한 것 (텐서플로 1 vs 2 혹은 keras 혹은 파이토치 등)이 있습니다. 그러므로 그 차이를 알아야겠죠??

# 추가적으로 논문 학습을 위한 팁