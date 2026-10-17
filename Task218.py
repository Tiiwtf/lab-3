
#enter the value of a natural number
number = int(input("Введіть натуральне число: "))

#count the number of digits in the number
digits_count = 0

#repeat the process of dividing the number by 10 until it becomes 0
while True:
    number //= 10
    digits_count += 1
    if number == 0:
       break

    #print result
print(digits_count)