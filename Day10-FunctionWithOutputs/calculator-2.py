#Trong phần này chúng ta sẽ tìm hiểu về đệ quy (recursion) trong Python
#Chúng ta sẽ sử dụng chính bài tập ở file calculator.py để thực hiện đệ quy trong bài toán này
#Đệ quy có thể định nghĩa đơn giản rằng đó là trong một hàm sẽ gọi lại chính nó để tiếp tục tính toán cho đến khi có một điều kiện nào đó để nó có thể dừng lại


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

#Thay vì sử dụng vòng lặp while ở đây, chúng ta sẽ sử dụng đệ quy (recursion)
def calculator():
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

        continue_calc = input(f"Do you want to continue calculate the current result {calculation}? Type 'yes' to continue,'no' to create new calculator or 'quit' to logout the program.\n")

        if continue_calc == 'yes':
            number1 = calculation
        elif continue_calc == 'no':
            #Gọi đệ quy hàm calculator nếu người dùng muốn tạo một phép tính mới mà không sử dụng kết quả của phép tính cũ nữa
            calculator()
        elif continue_calc == 'quit':
            print("Goodbye")
            isNotCont2 = True


if __name__ == "__main__":
    calculator()