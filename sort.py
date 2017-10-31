import time

a=[]
b=[]

print("you must write 10 n(number)")
#a,b value input
for k in range(10):
    n=int(input())
    a.append(n)
    b.append(n)
#time measurement    
start = time.time()
a.sort()
end = time.time()
print("use sort function.")
print(end-start)
print(a)

start = time.time()
for i in range(0,len(a)-1):
    for j in range(0,len(a)-i-1):
        if b[j]>b[j+1]:
            temp=b[j]
            b[j]=b[j+1]
            b[j+1]=temp
end = time.time()
print("use bubble sort.")
print(end-start)
print(b)
