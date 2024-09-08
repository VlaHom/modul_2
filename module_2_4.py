# Khomutov Vladimir

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []
for i in range(2, len(numbers)):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        primes.append(i)
    else:
        not_primes.append(i)
print("простые:", primes)
print("не простые:", not_primes)