a: list[int] = [ 1, 2, 3, 3, 4, 5]
b: list[int] = [0, 0, 1, 0, 1]

# 1 вариант
answer_1 = [
    val * b[i]
    for i, val in enumerate(a)

] 
print(answer_1)

# 2 вариант
answer_2 = []
for i, val in enumerate(a):
    answer_2.append(val * b[i])
print(answer_2)