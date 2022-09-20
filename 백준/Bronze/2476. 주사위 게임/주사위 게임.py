plp = int(input())
lst=[]
for i in range(plp):
  a,b,c = map(int,input().split())
  if a==b==c:
    lst.append(10000+a*1000)
  elif a==b and a!=c and b!=c:
    lst.append(1000+a*100)
  elif b==c and a!=b and a!=c:
    lst.append(1000+b*100)
  elif a==c and b!=a and b!=c:
    lst.append(1000+a*100)
  elif a!=b and a!=c and b!=c:
    lst.append(max(a,b,c)*100)
print(max(lst))