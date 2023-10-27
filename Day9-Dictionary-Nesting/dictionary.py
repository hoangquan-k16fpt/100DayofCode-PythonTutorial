#Trong bài này chúng ta sẽ tìm hiểu về một cấu trúc dữ liệu đặc biệt trong Python, đó là Dictionary (từ điển)
#Từ điển trong Python cũng hoạt động và có cấu trúc tương tự như từ điển ngoài đời thực
#Khi bạn tra từ, sẽ có một định nghĩa kèm theo, đó là cấu trúc của từ điển
#Mỗi từ điển thông thường sẽ có 2 phần: từ khóa và giá trị (định nghĩa)

programming_dictionary = {
    "Bug":"An error in a program that prevents the program from running as expected.",
    "Fuction":"A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}
#Truy xuất giá trị từ trong dictionary
print(programming_dictionary["Bug"])

#Add thêm giá trị vào trong dictionary
programming_dictionary["Dictionary"] = "A dictionary containing the following properties of the programming dictionary"
print(programming_dictionary)

#Để khởi tạo một từ điển trống, ta sử dụng dấu ngoặc nhọn
empty_dictionary = {}

#Để chỉnh sửa từ điển, ta sử dụng cú pháp như sau:
programming_dictionary["Bug"] = "Hello, world"
print(programming_dictionary)

#Nếu chúng ta không muốn in toàn bộ từ điển mà chỉ muốn lấy giá trị trong từ điển
#Chúng ta sẽ sử dụng vòng lặp để duyệt qua toàn bộ từ điển
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])
    