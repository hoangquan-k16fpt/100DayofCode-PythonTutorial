#0
#Input(nhập vào từ bàn phím) trong Python
input("What is your name?\n")
#Input và chương trình sẽ in ra Hello + tên
print("Hello " + input("What is your name?\n"))

#1
#Input nhập tên và chương trình sẽ in ra length (độ dài của chuỗi) mà bạn đã input
print(len(input("What is your name?\n")))

#2
#Gán biến cho input và in ra output là tên mà bạn vừa nhập vào từ bàn phím
#gọi name là một variable (biến)
name = input("What is your name?\n")
print(name)

#3
#Ví dụ đơn giản hơn
name = "Jack"
print(name)
#Sau này ta có thể gán cho biến name một giá trị khác
name = "Angela"
print(name) #Lúc này biến name đã thay đổi theo giá trị được gán cuối cùng

#4
#Ngoài ra ta cũng có thể tách thành nhiều biến khác nhau để code được tường minh và rõ ràng
name = input("What is your name?")
length = len(name)
print(length) # Đoạn code này sẽ in ra độ dài của biến name mà ta vừa input vào từ bàn phím

#NOTICE:
#Khi sử dụng đoạn code nào (0,1,2,3,4) thì comment các đoạn code khác lại để output tường minh và dễ hiểu


