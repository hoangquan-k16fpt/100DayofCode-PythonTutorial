#Trong phần trước chúng ta đã tìm hiểu về function trong Python, bao gồm hàm có tham số trả về và không có tham số trả về
#Ở phần tiếp theo, chúng ta sẽ làm quen với một kiểu hàm mới, đó là hàm có tham số đầu vào
#Hàm có tham số đầu vào là một hàm thông thường, tuy nhiên ta có thể truyền các tham số từ bên ngoài hàm vào trong hàm để có thể dễ dàng xử lý các tác vụ trong hàm
#Hàm có tham số đầu vào được sử dụng rất nhiều trong quá trình bạn viết mã

#Xem lại về phần hàm không có tham số đầu vào
def greeting():
    print("Hello")
    print("How are you today?")
    print("Isn't the weather nice today?")
greeting()
#Trên đây là một ví dụ về một hàm điển hình, không có tham số đầu vào
#Tiếp theo chúng ta sẽ đến với hàm có tham số đầu vào
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Where are you from, {name}?")
#Chúng ta có thể truyền tham số trực tiếp hoặc gián tiếp vào hàm
greet_with_name("Angela")
name = "Quan"
#Trong phần khai báo trên, người ta thường gọi "name" là parameter, còn "Quan" là argument
#Bạn cần phải nhớ những thuật ngữ thông dụng trong lập trình để sau này có thể làm việc dễ dàng hơn với chúng
greet_with_name(name)
#Trong Python, chúng ta có thể truyền mọi kiểu tham số vào hàm mà không cần phân biệt hoặc định nghĩa đó là kiểu dữ liệu gì, đây chính là điểm khác biệt của Python so với các ngôn ngữ lập trình khác
greet_with_name(123)

