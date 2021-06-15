# Write a program which returns the largest value between two user input numbers 
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

num3 = max(num1, num2)

print('The highest number between ' + str(num1) + ' and ' + str(num2) + ' is', num3)