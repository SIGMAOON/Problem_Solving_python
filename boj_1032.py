num = int(input()) - 1
str1 = list(input())
length = len(str1)

for i in range(num):
    str2 = list(input())
    for j in range(length):
        if str1[j] != str2[j]:
            str1[j] = '?'

print(''.join(str1))
