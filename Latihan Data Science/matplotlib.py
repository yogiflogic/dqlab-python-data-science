def Linear_search(arr, n, key):
 
    for i in range(0, n):
        if (arr[i] == key):
            return i
    else:
        return -1
  
arr = [12, 3, 24, 10, 4, 5, 7]
key = 10
n = len(arr)

result = Linear_search(arr, n, key)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)

a = 45
while True :
     if a > 56:
         print(a+3)
         break
     else:
         a += 2

def func1(a):
    b = a + 2
    return b + 10

def fun2(b):
    d = b + 10
    print(func1(d))


fun2(20)

x = "2 4 6 8 10"
b = x.split(" ")
for i in b:
    if x is 6:
        print(x,"sudah di temukan")
        break
    x += i
    

print(x)