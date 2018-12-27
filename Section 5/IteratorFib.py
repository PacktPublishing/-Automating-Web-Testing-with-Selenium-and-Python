def fib():
   a, b = 0, 1
   while True:
      yield b
      a, b = b, a + b

f = fib()
print(type(f))
for i in range(20):
    print(next(f), end=' ')
print()