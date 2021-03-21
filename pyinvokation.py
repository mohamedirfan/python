import pyapplication
import sys
#online jupyter notebook
#https://hub.gke2.mybinder.org/user/apache-spark-idn3bvbz/notebooks/python/docs/source/getting_started/Untitled.ipynb?kernel_name=python3
def main():
    calc = pyapplication.Calculator()
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    # Take input from the user
    choice = input("Enter choice(1/2/3/4):")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if choice == '1':
        print(num1,"+",num2,"=", calc.add(num1,num2))
    elif choice == '2':
        print(num1,"-",num2,"=", calc.subtract(num1,num2))
    elif choice == '3':
        print(num1,"*",num2,"=", calc.multiply(num1,num2))
    elif choice == '4':
        print(num1,"/",num2,"=", calc.divide(num1,num2))
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()

print("Main Method Name:",__name__)

# Exception Hanldling in python

a = [1, 2, 3]
try:
    print("Second element = " + str((a[1])))

    # Throws error since there are only 3 elements in array
    print("Fourth element = "  + str((a[3])))

except IndexError:
    print("An error occurred in the index handling")

(x, y) = (5, 0)

try:

    z = x / y

except IOError:
    print("An error occurred trying to read the file.")

except ValueError:
    print("Non-numeric data found ")

except ImportError:
    print("NO module found")

except(ZeroDivisionError, NameError):
    print("Divide by zero error occured")
except:
    print(" some error occured")
else:
    print("No Error")
finally:
    print("I will be running at any cost")
