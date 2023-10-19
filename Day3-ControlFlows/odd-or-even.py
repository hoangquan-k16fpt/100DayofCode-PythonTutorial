print("Odd or even auto checker")
#Nhập vào một số nguyên để kiểm tra đó là số chẵn hay lẻ
number = int(input("Input your number:"))
#Nếu là số chẵn thì input number phải chia hết cho 2, còn số lẻ thì sẽ không chia hết cho 2
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")


    