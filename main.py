# 1. Turn on -> add in an off switch (x)
# 2. Take in user input -> parse entire equation
# 3. Give the result
# 4. Perform another calculation?
# 5. a. If no -> turn off (x)
# 5. b. If yes -> ask if they want to use last result
# 6. a. If yes -> repeat 1-5 with last result
# 6. b. If no -> repeat 1-5 with new numbers

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# HELPER FUNCTIONS AND IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add(numOne, numTwo):
    return str(float(numOne) + float(numTwo))


def subtract(numOne, numTwo):
    return str(float(numOne) - float(numTwo))


def multiply(numOne, numTwo):
    return str(float(numOne) * float(numTwo))


def divide(numOne, numTwo):
    try:
        return str(float(numOne) / float(numTwo))
    except ZeroDivisionError:
        return "0"
        # return "You can't divide by zero!"




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN DEFINITION
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    calcOn = True
    useLastResult = False
    result = 0

    operations = {"*": multiply, "/": divide, "+": add, "-": subtract}

    while calcOn:

        # Take in user equation
        print("")
        print("Enter an equation")
        rawEq = input(" --> ")



        # Parse equation into list
        eqTokens = []
        num = ""
        
        for idx in range(len(rawEq)):
            if rawEq[idx] in ["+", "-", "*", "/"]:
                eqTokens.append(num)
                eqTokens.append(rawEq[idx])
                num = ""
            elif rawEq[idx].isdigit() or rawEq[idx] == ".":
                num += rawEq[idx]
            else:
                continue
        
        if num:
            eqTokens.append(num)

        print(f"eqTokens is first: {eqTokens}")
        
        # Solve equation in order of operations
        for key in operations.keys():
            for idx in range(len(eqTokens)):
                if eqTokens[idx] == key:
                    numOne = eqTokens[idx-1]
                    numTwo = eqTokens[idx+1]
                    result = operations[key](numOne, numTwo)
                    eqTokens[idx-1:idx+1] = result
                    print("")
                    print(f"After passing for {key} eqTokens is: {eqTokens}")



        print(f"After all keys eqTokens is: {eqTokens}")

        validChoice = False
        while not validChoice:
            print("")
            print("Would you like to perform another calculation? (y/n)")
            another = input(" --> ").lower()

            if another in ["y", "yes"]:
                validChoice = True
            elif another in ["n", "no", "exit", "quit"]:
                validChoice = True
                calcOn = False
            else:
                print("Invalid choice!")





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN CALL
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    main()
