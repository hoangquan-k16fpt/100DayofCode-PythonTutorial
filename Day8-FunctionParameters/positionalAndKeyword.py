#Trong bài tập này, chúng ta sẽ làm quen với khái niệm posisional và keywords argument
#Ở bài tập trước, ta đã làm quen với khái niệm hàm có tham số đầu vào
#Hàm trong ngôn ngữ lập trình Python giới hạn số lượng tham số đầu vào tối đa
#Hàm là công cụ để có thể sử dụng lại code nhanh mà không cần phải lặp đi lặp lại các đoạn code giống nhau
#Lưu ý khi viết hàm, mỗi hàm chỉ nên xử lý 1 tác vụ cụ thể, để có thể tối ưu và dễ dàng sử dụng lại hàm

def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"Your location is {location}.")

#Truyền tham số vào trong hàm thông qua biến toàn cục
name = "Ngo Ba Hoang Quan"
location = "Dong Da, Ha Noi, Viet Nam"
greet_with(name,location)
#Khi định nghĩa như trên, ta đang định nghĩa argument "name" của hàm là biến name toàn cục, argument "location" của hàm là biến location toàn cục
#Ta không nhất thiết phải đặt tên arguments và biến toàn cục giống nhau
a = "Tim Bulchaka"
b = "New South Wales, Australia"
greet_with(a,b)

#Truyền tham số trực tiếp trong hàm mà không thông qua biến toàn cục
greet_with("Angela","Beijing, China")

#Ngoài ra trong Python còn có thể đổi chỗ của các arguments
#Tuy nhiên khi sử dụng cách này chúng ta phải định nghĩa cụ thể từng argument
greet_with(location = "Yen Phong, Bac Ninh", name="Ngo Ba Hoang Bach")
#Khi này, chương trình vẫn hiểu và biên dịch chính xác và không có lỗi gì