
def tip_calculator(total,percent):
    try:
        total = float(total)
        percent = float(percent)
    except:
        raise ValueError("Invalid argument. Total and perecent must be numbers.")

    return total * (percent/100)

if __name__ == "__main__":
    #catch user error
    try:
        total = float(input("Total: $").strip())
        tip = float(input("Tip? (in %): ").strip())
    except:
        raise ValueError("Invalid input. Please enter numbers only.")

    #calculate total due
    due = round(total + tip_calculator(total,tip),2)

    print(f"Total due: ${due}")
    
