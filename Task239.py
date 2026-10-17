
#enter the value of steps
steps = int(input("Введіть кількість сходинок: "))

#Building stairs using a loop
for i in range(1, steps + 1):

    #print spaces and characters to create a step
    print(" " * (steps - i) + "#" * i)
