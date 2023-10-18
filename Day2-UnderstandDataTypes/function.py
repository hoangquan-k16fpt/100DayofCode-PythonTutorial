name_char = len(input("What's your name?\n"))
#Để có thể biết được kiểu dữ liệu của một biến, ta sử dụng hàm type()
print("Type of name_char: ", type(name_char))
#Ta không thể nối chuỗi giữa string và integer nên bắt buộc phải ép kiểu integer trở thành string
new_name_char = str(name_char)
#Sau đó ta có thể in ra số lượng ký tự trong chuỗi string mà người dùng đã nhập vào 
print("Your name has " + new_name_char + " characters.")

#Tương tự ta sẽ kiểm tra kiểu của casd biến
a = str(123)
print(type(a))
b = float(3.14)
print(type(b))

#Một số ví dụ về ép kiểu
print(70 + float("100.5"))
print(str(50) + str(70))
