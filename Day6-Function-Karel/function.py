#Trong bài này chúng ta sẽ tìm hiểu về hàm/function trong Python, dưới đây là cách để khai báo một hàm đơn thuần
#Hàm sẽ bao gồm 2 loại chính, đó là hàm có tham số trả về, tức là khi gọi hàm đó, ta sẽ return lại một cái gì đó, có thể là một số, kí tự,...
#Loại thứ hai đó là hàm không có tham số trả về. Loại này thì thường sẽ thực hiện 1 chức năng và sẽ có lệnh print ngay trong hàm, và không có lệnh return

#Ví dụ về hàm không có tham số trả về, không có lệnh return
def SayHello():
    name = input("Input your name: ")
    print(f"Hello {name}")
#Sau khi định nghĩa và tạo xong hàm, để gọi hàm cần chú ý tab về đầu lề
SayHello()

#Ví dụ về hàm có tham số trả về
def userName():
    name = input("Input your name: ")
    return name
#Để sử dụng được hàm có tham số trả về, ta cần gán biến cho tham số trả về của hàm đó
username = userName()
print(f"Bonjour {username}")
