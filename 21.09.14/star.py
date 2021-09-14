# input 별의 층수
# output 별 곱하기

# umber = int(input())
# for i in range(1, number + 1):
#    print("*" * i)


# number = int(input())
# for i in range(number + 1):
#     print("*" * (i+1))

number = int(input())
i = 1

# i와 number 랑 비교할 수 있는 것을 적어야 합니다.
5
while i <= number:
    print(" " * (number-i) + "#" * i)
    i +=1
