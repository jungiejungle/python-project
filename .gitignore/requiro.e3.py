data = input("Enter a comma separated list of numbers:")

total = sum([float(k)**2 for k in data.split(",")])
print("Sum of squares: {:.2f}".format(total))


import sys 

real_numbers = sys.argv[1]
real_numbers = float(real_numbers)
squared_numbers = sys.argv[1]
squared_numbers = float(squared_numbers)

real_numbers = print("Enter a comma separated list of numbers:")
