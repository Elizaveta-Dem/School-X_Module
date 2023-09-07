n = int(input('Введите число '))
sum1 = 0
#sum2 = 0
for i in range(0, n+1):
    if i % 3 == 0 or i % 5 == 0:
         sum1 += i
         
  #  if i % 5 == 0:
    #    sum2 += i
         
print(sum1)