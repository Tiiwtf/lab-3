
#enter the value of the number
number = int(input("Введіть число (0 - кінець вводу): "))

#Initial values ​​of variables
best_length = 0
best_value = 0
current_length = 0
previous = 0

#repeat until the user enters 0 
while number != 0:

    #check if the current number is equal to the previous one
    if number == previous:
        current_length += 1
    else:

        #reset the current length and update the previous number
        current_length = 1
        previous = number

        #check if the current length is greater than the best length
    if current_length > best_length:
        best_length = current_length
        best_value = number

        #enter second number
    number = int(input("Введіть число (0 - кінець вводу): "))

    #print the results
print("Найдовший ряд однакових чисел:", best_length)
print("Повторюваний елемент:", best_value)
