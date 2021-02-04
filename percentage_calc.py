percentage = input("Input Percentage in decimals: ")
number     = input("Input Number: ")

p = float(percentage)
n = float(number)

percent = (p * n) - n 
positive = percent * -1.0
print(f"Your percentage of the input number is {positive}")


