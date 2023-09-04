a=list(map(int,input().split()))
c=0
for i in range(0,len(a)):
    if i==a[i]:
        print(i)
        c=1
if c==0:
    print("No Fixed Point")
