#Trong phần này chúng ta sẽ làm quen với module random của Python
#Ngoài ra chúng ta cũng sẽ tìm hiểu cách hoạt động của module bất kì trong Python
import random
#Lưu ý chúng ta cần thực hiện import các module ở trên đầu của mỗi file python để việc code được thuận tiện và dễ dàng hơn
import my_module
#Khi import my_module chúng ta đã có thể thấy không hề có lỗi, chứng tỏ chương trình đã chấp nhận module này của chúng ta là một phần của chương trình


integer_random = random.randint(1,1000)
print(integer_random)
#Chúng ta cũng sẽ làm quen với các module sẵn có của Python, vậy làm sao để các module có thể hoạt động
#Đầu tiên chúng ta sẽ tạo 1 file python có đuôi .py, đặt tên là my_module và thực hiện thiết kế các hàm và câu lệnh trong module, sau đó chúng ta sẽ sử dụng lệnh import để import chính file mà chúng ta vừa tạo
#Lưu ý rằng tại mỗi file python mà chúng ta sử dụng module cần import module đó

#Chúng ta sẽ thực hiện print số pi mà chúng ta đã định nghĩa trong my_module
#Cấu trúc của việc gọi một biến/ hàm trong 1 module, ta cần đặt tên module ở trước rồi dot tên hàm/biến
print(my_module.pi)

#Tiếp theo chúng ta sẽ làm quen với việc random float trong Python
#Ở Python random float sẽ chỉ cho giá trị chạy từ 0 - 1
#Vậy câu hỏi đặt ra là làm thế nào để có thể tăng range của việc random float? Chúng ta sẽ sử dụng random_float*x (trong đó x là range mà chúng ta muốn tăng)
#Ở đây chúng ta sẽ tăng giới hạn của random là từ 0.00000... - 4.999999...., random sẽ theo kiểu float 
random_float = random.random()
random_float = random_float *5
print(random_float)

#Ta có thể tạo điểm số tình yêu ngẫu nhiên từ 1 đến 100 như sau:
love_score = random.randint(1,100)
print(f"Your love score is {love_score}")