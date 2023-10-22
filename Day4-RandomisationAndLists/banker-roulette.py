#Trong bài toán này chúng ta sẽ đưa vào 1 chuỗi và chuyển chuỗi đó thành list
#Trong chuỗi là tên của các thành viên của 1 nhóm người sẽ đi ăn hôm nay
#Nhiệm vụ của bạn là random tên một người nào đó sẽ trả tiền cho bữa ăn ngày hôm nay bằng cách sử dụng list

#Đầu tiên chúng ta sẽ nhập tên cách thành viên trong nhóm, tên các thành viên ngăn cách nhau bởi dấu phẩy và 1 space
name_string = input("Input name (separated by comma and space): ")
#Chuyển string vừa input thành chuỗi bằng cách tách các phần tử trong chuỗi
name = name_string.split(", ")
import random
#Random index của list để lấy random tên người sẽ thanh toán bằng cách sử dụng module random mà ta đã học ở bài trước
num_items = len(name)
random_name = random.randint(0, num_items - 1)
person_who_pay = name[random_name]
#In ra kết quả
print(person_who_pay + " will pay the meal today!")

