
#enter the value of n
limit = int(input("Введіть n: "))

#Loop through numbers from 1 to n
for number in range(1, limit + 1):
    divisors = 0

    #Check all possible divisors of the number
    for d in range(1, number + 1):

        #Check if d is a divisor of number
        if number % d == 0:
            divisors += 1

            #print the number and the number of divisors
    print(str(number) + "+" * divisors)
