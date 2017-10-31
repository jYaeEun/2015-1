print("write n")
n = int(input())
#star tree
for i in range (1,n+1):
    for j in range(1,i+i):
        print('*',end='')
    print('');
