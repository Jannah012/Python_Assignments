fn=0
sn=1
n=int(input('nmbr'))
sum=fn+sn
for i in range(0,n+1):
    print(sum)
    sum=fn+sn
    fn=sn
    sn=sum