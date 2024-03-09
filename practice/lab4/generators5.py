def generate_nums(n):
    for i in range(n):
        yield i

n = int(input())

z = generate_nums(n)
S=[]
for a in z:
    S.append(a)
S= S[::-1]
print(*S)