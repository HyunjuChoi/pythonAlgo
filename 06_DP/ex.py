#230731
# 피보나치 함수 재귀로 구현해보기

def fibo(x):
    if x ==1 or x == 2:
        return 1
    else:
        return fibo(x-1)+fibo(x-2) 

print(fibo(4))