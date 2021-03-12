# people = {
#     ('이호준', '01050442903'),
#     ('이호상', '01051442904'),
#     ('이준호', '01050342904'),
#     ('이호준', '01050442903'),
#     ('이준', '01050412904'),
#     ('이호', '01050443904'),
#     ('이호준', '01050442903')
# }

# len(set(people))

###################################################

# a = input('알파벳을 입력 하세요: ')
# for i in a:
#     if i.isupper():
#         print(i.lower(),end="")
#     elif i.islower():
#         print(i.upper(),end="")

########################################################

# num = list(map(int,input().split()))
# print(max(n))

# n = list(map(int,input().split()))

# a = sorted(list(map(int,input().split())))
# print(a[-1])

# num = list(map(int,input().split()))
# a = 0 
# for i in range(len(n)):
#     if num[i] > a:
#         a = num[i]
# print(num[i])

#######################################################

# student = ['강은지','김유정','박현서','최성훈','홍유진','박지호','권윤일','김채리','한지호','김진이','김민호','강채연']
# # student.sort()
# # for i in range(len(student)):
# #     print('번호: {0}, 이름: {1}'.format(i+1,student[i]))

# student.sort()
# for p in enumerate(student):
#     print(p)
# for i, v in enumerate(student):
#     print("번호: {0}, 이름: {i}".format(i+1,name))

#######################################################

# 20190923

# print(ord('U')-ord('A'),ord('U')-ord('B'),ord('A')-ord('A'),ord('O')-ord('F'),ord('X')-ord('A'))

#######################################################

# n = list(input().split()) # 입력한 값을 리스트로 정렬
# i = 0 
# for i in range(len(n)): # 입력한 값의 리스트 수 만큰 for 문으로 돌림
#     print(n[i][0],end='') # 리스트의 i 번째 의 첫번째 글만 출력

# # a = input().split('')
# out = ''

# for i in a:
#     out = out + i[0]
#     print(out)
# print(out)

#######################################################

# 양의 정수만 입력으로 받고 그 수의 자릿수를 출력해보자.

# print("{}의 자리수".format((len(input())))) # 입력을 받아 그 자리수를 출력

a = input().split(' ') # 값을 입력
result = 0
for i in a: # for문을 이용하여 숫자를 센다.
    result += len(i) # 입력한 값의 수를 하나식 더해 준다.
print(result) # 더한 값을출력 한다.