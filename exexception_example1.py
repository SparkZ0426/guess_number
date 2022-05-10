#The try block will generate an error, because x is not defined:

num1 = input("Enter number one")
num2 = input("Enter number two")
try:
  num1 = int(num1)
  num2 = int(num2)

  result = num1/num2
  print("the result is " + str(result))

except ZeroDivisionError:
  print("You cannot divide a number by 0")
except ValueError:
  print("You need to enter number as age")
except:
  print("An exception has occured")
