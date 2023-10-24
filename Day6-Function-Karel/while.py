#Trong phần này chúng ta sẽ tìm hiểu về vòng lặp while, vòng lặp while là nâng cao của vòng lặp for
#Với for, ta có thể lặp qua các phần tử trong 1 list, hay có thể định rõ số lần lặp cho vòng lặp bằng cách sử dụng in range
#Ở vòng lặp while, nó sẽ lặp nếu điều kiện vẫn đúng, cho đến khi điều kiện sai thì nó mới thoát vòng lặp

#Định nghĩa number = 1
number = 1
#Vòng lặp sẽ hoạt động cho đến khi number = 10 thì dừng
while number < 10:
    print(number)
    #Sau mỗi lần lặp, tăng number lên 1 đơn vị
    #Vậy vòng lặp sẽ in number đến 9, khi number = 10 thì điều kiện sai, vòng lặp sẽ dừng
    number += 1

isRun = True
num = 1
while isRun == True:
    print(f"Vòng lặp thứ {num}")
    num += 1
    if num == 20:
        isRun = False

