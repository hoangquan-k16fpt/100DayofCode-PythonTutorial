#Trong phần này, chúng ta sẽ xây dựng một chương trình máy tính đơn giản bằng Python
#Chúng ta sẽ sử dụng các hàm để định nghĩa các phép toán

def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def divide(number1, number2):
    return number1 / number2

def multiply(number1, number2):
    return number1 * number2

def power(number1, number2):
    return number1 ** number2

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
    "^": power,
}

#Để chương trình có thể chạy tiếp sau khi tính toán, ta sử dụng vòng lặp while
isNotCont1 = False
while not isNotCont1:
    number1 = float(input("Enter the first number: "))

    isNotCont2 = False
    while not isNotCont2:
        for symbol in operations:
            print(symbol)

        symbol = input("Pick an operation in the line above: ")

        calculation = operations[symbol]

        number2 = float(input("Enter the second number: "))

        calculation = calculation(number1= number1, number2=number2)
        print(f"The calculation: {number1} {symbol} {number2} = {calculation}")

        continue_calc = input(f"Do you want to continue calculate the current result {calculation}? Type 'yes' to continue,'no' to cancel or 'quit' to logout the program.\n")

        if continue_calc == 'yes':
            number1 = calculation
        else:
            if continue_calc == 'quit':
                isNotCont1 = True
                print("Good bye!")
            isNotCont2 = True