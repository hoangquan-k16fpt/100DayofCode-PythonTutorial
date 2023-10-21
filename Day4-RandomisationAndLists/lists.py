#Trong bài học này chúng ta sẽ tìm hiểu về một khái niệm quan trọng trong Python, đó chính là cấu trúc list
#Cấu trúc list đơn giản chỉ là một trong số những cách tổ chức và lưu trữ dữ liệu trong Python
#Thay vì phải lưu trữ riêng lẻ từng biến có cấu trúc và tính chất giống nhau, chúng ta có thể lưu trữ chúng trong cùng 1 biến
#Ví dụ: chúng ta có thể lưu trữ tên các bang của Hoa Kỳ trong cùng 1 biến State_of_US
state_of_us = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", 
               "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", 
               "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", 
               "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", 
               "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", 
               "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", 
               "Wyoming", "Washington, D.C."]
#Mỗi phần tử trong list sẽ được đánh index, index sẽ được bắt đầu từ 0 ứng với phần tử đầu tiên trong list
#Ví dụ như bài toán trên state_of_us[0] sẽ tương ứng với Alabama
print(state_of_us[0])

#Ngoài đánh chỉ mục xuôi, trong Python ta cũng có thể thêm dấu trừ - vào trước index, khi này, list sẽ đếm ngược từ cuối list lên, tức là phần tử cuối cùng tương ứng với list tại index -1
print(state_of_us[-1])

#Ta có thể thay thế một phần tử trong list đơn giản là ghi đè lên phần tử đã có
#Ví dụ ta thay phần tử có index 1 bằng một giá trị khác
state_of_us[1] = "Pennsylvania"
print(state_of_us)
print("\n")
#Sau khi in ra ta thấy phần tử đã được thay đổi

#Tiếp theo, ta có thể nối thêm vào list 1 phần tử nữa ở cuối cùng của list bằng cách sử dụng phương thức append
state_of_us.append("Hanoi Capital City")
print(state_of_us)
print("\n")

#Tương tự như append, để thêm nhiều phần tử vào cuối list, ta sử dụng phương thức extend
state_of_us.extend(["Da Nang", "Hoi An", "Quang Nam", "Khanh Hoa", "Ho Chi Minh City"])
print(state_of_us)

#Chúng ta có thể lưu trữ các loại trái cây trong 1 biến list
fruit = ["Apple","Pear","Cherry"]
print(fruit[2])

