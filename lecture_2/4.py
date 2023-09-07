n: int =int(input('N:'))

array: list = range(n)

i = 0
while True:
    if array[i] % 123 ==0:
        print(array[i], 'делится')
    i += 1

# while n>0:
#     print(n)
#     n=n-1