# 1. Turn on -> add in an off switch (x)
# 2. Take in user input -> parse entire equation (x)
# 3. Give the result (x)
# 4. Perform another calculation? (x)
# 5. a. If no -> turn off (x)
# 5. b. If yes -> ask if they want to use last result (x)
# 6. a. If yes -> repeat 1-5 with last result (x)
# 6. b. If no -> repeat 1-5 with new numbers (x)

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


def tokenize(equation, lastResult="", useLastResult=False):
    eqTokens = []
    num = lastResult

    for char in equation:
        if char in ["+", "-", "*", "/"]:
            eqTokens.append(num)
            eqTokens.append(char)
            num = ""
        elif char.isdigit() or char == ".":
            num += char
        else:
            continue

    eqTokens.append(num)

    return eqTokens


def evaluate(rawEq):
    operations = {
        "*": multiply,
        "/": divide,
        "+": add,
        "-": subtract,
    }

    tokens = rawEq

    for operator in operations.keys():
        newTokens = [tokens[0]]
        for idx in range(1, len(tokens), 2):

            op = tokens[idx]
            right = tokens[idx + 1]

            if op == operator:
                left = newTokens.pop()
                result = operations[operator](left, right)
                newTokens.append(result)
            else:
                newTokens.append(op)
                newTokens.append(right)
        tokens = newTokens

    return newTokens[0]    


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN DEFINITION
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    calcOn = True
    useLastResult = False
    result = 0

    while calcOn:

        # Take in user equation
        print("")
        print("Enter an equation")
        rawEq = input(" --> ")

        # Parse equation into list
        if useLastResult:
            eqTokens = tokenize(rawEq, result)
        else:
            eqTokens = tokenize(rawEq)


        # Solve equation in order of operations
        result = evaluate(eqTokens)

        print(f" --> {result}")

        validChoice = False
        while not validChoice:
            print("")
            print("Would you like to perform another calculation? (y/n)")
            another = input(" --> ").lower()

            if another in ["y", "yes"]:
                validChoice = True

                validResultChoice = False
                while not validResultChoice:
                    print("")
                    print("Would you like to use last result? (y/n)")
                    resultChoice = input(" --> ").lower()

                    if resultChoice in ["y", "yes"]:
                        useLastResult = True
                        validResultChoice = True
                    elif resultChoice in ["n", "no"]:
                        useLastResult = False
                        validResultChoice = True
                    else:
                        print("Invalid choice!")

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
