try:
    num1 = input("\nEnter a number:")

    num2 = input("\nEnter a number:")

    num1int, num2int = int(num1), int(num2)
    result = num1int + num2int

except:
    print("sorry but we cant add them together")


else:
    print(f"addition of {num1int} and {num2int} is {result}")
