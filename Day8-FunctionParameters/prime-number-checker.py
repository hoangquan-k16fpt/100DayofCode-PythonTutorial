#Trong bài tập này chúng ta sẽ viết một hàm để kiểm tra số nhập vào có phải số nguyên tố hay không
#Số nguyên tố là số mà chỉ có ước là 1 và chính nó
#Chúng ta sẽ sử dụng kiến thức về hàm và vòng lặp trong bài này

def prime_checker(number):
    check = 0
    for num in range(1, number + 1):
        if number % num == 0:
            check += 1
    if check == 2:
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")

n = int(input("Input your number: "))
prime_checker(number = n)

#Cách 2: 
#Ở cách này, chúng ta có thể thấy chương trình sẽ chạy nhanh hơn cách 1 bởi giảm thiểu số vòng lặp
def prime(number_2):
    isPrime = True
    if number_2 <= 1:
        isPrime = False
    else:
        for num in range(2, number_2):
            if number_2 % num == 0:
                isPrime = False
                break
    if isPrime:
        print(f"{number_2} is prime.")
    else:
        print(f"{number_2} is not prime.")

n_2 = int(input("Input your number: "))
prime(number_2 = n_2)