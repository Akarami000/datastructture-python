m=int(input())
n=int(input())

if m<n:
    (m,n)=(n,m)

if m%n==0:
      print(n)

else :
      dif=m-n
      print (min(n,dif))



