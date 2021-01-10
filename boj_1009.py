T = int(input())

for i in range(T):
    a, b = map(int,input().split()) # 한 줄에 공백으로 분리된 여러개의 입력 받기
    a = a % 10
    
    if a == 0:
        print(10)
        
    elif a == 1 or a == 5 or a == 6:
        print(a)
    
    elif a == 4 or a == 9:
        if b % 2 == 0:
            print((a*a) % 10)
        else:
            print(a)
    
    elif a == 3 or a == 7 or a == 2 or a == 8 :
        b = b % 4
        
        if b == 1:
            print(a)
        elif b == 0:
            if a % 2 == 0:
                print(6)
            else:
                print(1)
            
        elif b == 2:
            if a % 2 == 0:
                print(4)
            else:
                print(9)
        else:
            print((a**3) % 10)
