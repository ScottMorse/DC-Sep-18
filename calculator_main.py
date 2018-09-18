import calculator

def user_input():
    #takes input and catches errors
    try:
        value_1 = float(input("First value: ").strip())

        operator = input("Operator: ").strip()
        assert operator in calculator.operations

        value_2 = float(input("Second value: ").strip())
    except:
        raise ValueError("Invalid input.")

    return (value_1,operator,value_2)

def calculate(value_1,operator,value_2):

    #runs a function from calculator on the two values
    result = calculator.operations[operator](value_1,value_2)

    #doesn't return float on whole numbers
    if result.is_integer():
        result = int(result)

    return result

if __name__ == "__main__":

    print(f"Result: {calculate(*user_input())}")