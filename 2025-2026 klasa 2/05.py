<<<<<<< HEAD
def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print("fib(n)", 50, fib(50))

def fib2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = a + b
    return a

a = 5
b = 8

a, b = b, a
print("fib2(n)", 400, fib2(400))
=======
def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print("fib(n)", 50, fib(50))

def fib2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = a + b
    return a

a = 5
b = 8

a, b = b, a
print("fib2(n)", 400, fib2(400))
>>>>>>> 1dd45523b45d5652d47db15093e62f50f2550991
