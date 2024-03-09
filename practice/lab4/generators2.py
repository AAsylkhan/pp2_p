def generate(N):
    for i in range(1, N):
        if i%2==0:
            yield i
        else:
            continue

N = int(input())
x = generate(N)
S=[]
for a in x:
    if a == N-1:
        S.append(a)
        break
    S.append(str(a) + ",")
print(*S)