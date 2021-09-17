# 백준 1978번 문제

# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성
# 첫 줄에 수의 개수 N (N <= 100)
# 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수

# 함수를 사용한 경우

# 입력 받기
n = int(input())
input_num = map(int, input().split())

# 소수인지 판별하는 함수
def check_prime(num):
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# 입력값이면서 소수인 값의 개수 구하기 (list comprehension 활용: LMS 06 참고)
print(sum([check_prime(x) for x in input_num]))
            
# 함수를 사용하지 않은 경우

n = int(input())
input_num = map(int, input().split())

nprime_num = [1]
output_num = []

# 소수가 아닌 수의 리스트 구하기 nprime_num
for i in range(1, 1000+1):
    j = 2
    while 1 < j < i:
        if i % j == 0:
            nprime_num.append(i)
            j += 1

        else:
            j += 1

for i in input_num:
    if i in nprime_num:
        continue
    else:
        output_num.append(i)


# 소수이면서 입력 받은 수의 리스트 output_num
for i in range(1, 1000+1):
    if i in nprime_num:
        continue
    else:
        if i in input_num:
            output_num.append(i)


print(output_num) # 출력값 (소수이면서 입력된 값들의 개수)

# 백준 1065번 문제

# 어떤 양의 정수N의 각 자릿수가 등차수열을 이룬다면 그 수를 한수라고 한다.
# N 이하의 자연수에서 한수의 개수를 구하여라.
# 입력 값 N <= 1000, 출력 값 : 한수의 개수

# 풀이과정
# 1. 한수를 구한다 → 1번 선택
# 2. 반대

# 예제: 입력 출력
# 110 >> 99 → 1 ~ 99 는 모두 한수이다. 100, 101, 102,
# 1 >> 1 103... 나머지는 당연히 한수가 아니다.
# 210 >> 105

N = int(input())

def checksh(num):
    if num < 100:
        return True
    else:
        if int(str(num)[0]) - int(str(num)[1]) == int(str(num)[1]) - int(str(num)[2]) :
            return True
        else:
            return False

count = 0
for i in range(1, N+1):
    if checksh(i) == True:
        count += 1

print(count)