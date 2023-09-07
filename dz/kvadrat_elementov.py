def squares(N):
    l: list = []
    for i in range(-N, N+1): #положительные и отрицательные числа на вход
        l.append(i**2)
    return l
print(squares(2))
