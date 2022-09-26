n = int(input())
st, an, find = [],[],True

now=1
for i in range(n):
  num = int(input())
  while now <= num:
    st.append(now)
    an.append('+')
    now += 1
  if st[-1] == num:
    st.pop()
    an.append('-')
  else:
    find = False

if not find:
  print("NO")
else:
  for i in an:
    print(i)