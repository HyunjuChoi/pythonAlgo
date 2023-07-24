
n = int(input())

A = list(input().split())

x = 1
y = 1

for i in range(len(A)):
    if (x == 1 and A[i] == 'U'): 
        continue
    elif (x == 5 and A[i] == 'D'):
        continue
    elif (y == 1 and A[i] == 'L'):
        continue
    elif (y == 5 and A[i] == 'R'):
        continue
    else:
        if (A[i] == 'U'): x -= -1
        elif (A[i] == 'D'): x += 1
        elif (A[i] == 'R'): y +=1
        elif (A[i] == 'L'): y -= 1

print(x, y)
