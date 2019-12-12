'''
문제 2.
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

numbers = int(input('숫자를 입력하세요: '))

i = 0
while i <= numbers:
    i = i+1 
    print(i)

#아래는 답안코드 
# for i in range(numbers):
#    print(i+1)