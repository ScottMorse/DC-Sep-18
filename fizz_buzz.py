
def fizz_buzzer(num):
    #error handle
    if not isinstance(num,int):
        raise ValueError("Invalid argument. Please use integer.")
    
    #bools
    fizzer = num % 3 == 0
    buzzer = num % 5 == 0

    #results
    if fizzer:
        result = "Fizz"
        if buzzer:
            result += " Buzz"
        return result
    if buzzer:
        return "Buzz"
    return

if __name__ == "__main__":

    print(fizz_buzzer(int(input("Enter a number(int): ").strip())))