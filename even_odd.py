
def parity_check(num):
    #user input with error catcher
    if not isinstance(num,int):
        raise ValueError("Invalid argument.  Use integer only.")
    
    #checks parity
    if num % 2 == 0:
        parity = "even"
    else:
        parity = "odd"

    return parity

if __name__ == "__main__":

    user_input = int(input("Enter a number(int): ").strip())
    
    print(f"Number({user_input}) is {parity_check(user_input)}.")