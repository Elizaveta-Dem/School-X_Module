def personal(
        num: int
) -> int:
        for i in range(1,num+1):
            if num/i == i:
                otvet=num/i
                print(otvet)
                break
            else:
                print(f'{i} Не могу')

personal(1)
    

        