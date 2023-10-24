#Trong bài tập này chúng ta sẽ tạo một dự án tạo password random
#Người dùng sẽ nhập số lượng chữ cái, số và ký tự đặc biệt mà họ muốn có trong password của mình
#Chương trình sẽ tự động random các chữ cái, số và ký tự để in ra một password random
#Chúng ta cần sử dụng module random
#Hint: cần sử dụng hàm shuffle trong module random để trộn các ký tự, chữ cái và số lại với nhau
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5','6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '?']

print("Welcome to the Password Generator.")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_number = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

password_list = []
for i in range(0, nr_letters):
    random_char = random.choice(letters)
    password_list.append(random_char)

for i in range(0, nr_number):
    random_num = random.choice(numbers)
    password_list.append(random_num)

for i in range(0, nr_symbols):
    random_symbols = random.choice(symbols)
    password_list.append(random_symbols)

#Sau khi có một list các ký tự, chữ cái và số trong password, ta thực hiện trộn shuffle chúng lại với nhau
random.shuffle(password_list)
#Sau khi shuffle ta có một password mà chữ cái, số và ký tự được trộn xen kẽ
password = ""
for char in password_list:
    password += char

print(f"Your password: {password}")
