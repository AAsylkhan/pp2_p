def generate(N):
    for i in range(1, N):
        if i%3==0 and i%4==0:
            yield i
        else:
            continue

N = int(input())
x = generate(N)
S=[]
for a in x:
    S.append(a)
print(*S)