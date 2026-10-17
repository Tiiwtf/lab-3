
#enter the value 
divisor = int(input("Введіть число n: "))

#Variable to for storage sum of numbers 
total = 0

#Overalling all three-digit numbers from 100 to 999 
for number in range(100, 1000):

    #checking if the number is divisible without residue 
    if number % divisor == 0:

        #add number to the total sum
        total += number

        #print the result
print(total)
