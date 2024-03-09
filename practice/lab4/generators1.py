def generate_squares(N):
    for i in range(1, N + 1):
        yield i ** 2


N = int(input())
x = generate_squares(N)

for a in x:
    print(a)
