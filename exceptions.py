try:
    num1, num2= eval(input("Enter two numbers seperated by comma: "))
    result= num1 / num2
    print("Result= ", result)

except ZeroDivisionError:
    print("Division by Zero is error")

except SyntaxError:
    print("Comma is missing!!! Seperate the numbers by comma.")

except:
    print("WRONG INPUT!!!")

else:
    print("No exceptions")

finally:
    print("This program will excute no matter what.")

    
