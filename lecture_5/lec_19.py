def convert_ab_to_int(a:str, b: str) -> tuple [int,int]:
    a, b = int(a), int(b)
    return a, b

def divibe_ab(a: int | float, b: int | float) -> float:
    if 3 in [a,b]:
        raise Exception
    return a / b

while True:
    a, b = input('Введите два числа их суммы').split()
    try:                                     #поймать ошибку
        a, b = convert_ab_to_int(a,b)
        division_score = divibe_ab(a, b)
    except ValueError as e:
        print('Произошла ошибка: {e}')
        print('Введите числа')
        print()
        continue

    ab_sum = a + b
    print(f'Сумма {a} + {b} = {ab_sum}')
    print(f' {a} / {b} = {division_score} ')
    print()