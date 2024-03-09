def generate_squares(x,y):
    for i in range(x,y):
        yield i ** 2

x = int(input())
y = int(input())
z = generate_squares(x,y)
S=[]
for a in z:
    S.append(a)
print(*S)