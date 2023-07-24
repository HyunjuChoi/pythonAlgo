x = int(input())

result = 0

while(x != 1):
    if(x%5 == 1):
        x -=1
        result+=1
    elif(x%5 == 0):
        x = x//5
        result += 1
    elif(x%3 == 0):
        x = x//3
        result += 1
    elif (x%2 == 0):
        x  = x//2
        result += 1
print(result)
