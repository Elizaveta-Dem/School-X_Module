def personal(
        num: int
) -> int:
        for i in range(1,num):
            if num/i == i:
                otvet=num/i
                print(otvet)
                break
            else:
                print(f'{i} Не могу')

personal(196)
    

        