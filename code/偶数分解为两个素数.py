import math


def IsPrime(n):
    flag = True
    # 判断是否为质数
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            flag = False
            break
    return flag

def testing(n):
    if n > 0 and n % 2 == 0:
        for i in range(3,int(n/2)+1):
            if IsPrime(i) and IsPrime(n-i):
                print(n,'=',i,'+',n-i)

if __name__ == '__main__':
    testing(10)