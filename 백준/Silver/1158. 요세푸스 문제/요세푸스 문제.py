N,K = map(int, input().split())
ppl=[i for i in range(1, N+1)]
rmv=[]
idx=0

for j in range(N):
  idx = idx + K-1
  if idx >= len(ppl):
    idx = idx%len(ppl)
  rmv.append(str(ppl.pop(idx)))
print("<",", ".join(rmv)[:],">", sep='')