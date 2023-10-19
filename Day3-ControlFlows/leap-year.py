#Trong bài toán này ta sẽ đi kiểm tra xem số năm mà người dùng nhập vào có phải năm nhuận hay không
print("Welcome to the leap year checker program.")
year = int(input("Enter the year you want to check: "))
if year % 4 == 0:
    if year % 100 == 0:
        if(year % 400 == 0):
            print(f"{year} is a leap year")
        else: 
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")