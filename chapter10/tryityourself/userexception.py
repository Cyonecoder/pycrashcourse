result = 0
while True:
    try:

        num1 = input("\nEnter a number:")
        if num1 == "q":
            break
        num1int = int(num1)

    except:
        # print("sorry but we cant add them together")
        pass

    else:
        resultbefore = result
        result += num1int
        print(f"addition of {resultbefore} and {num1} is {result}")
