#Ở bài tập này chúng ta sẽ tạo một chương trình tung đồng xu ảo sử dụng module random để tạo ngẫu nhiên
#Bài tập này đơn giản chỉ là sử dụng random 0 và 1 để đặt cho mặt đồng xu là sấp và ngửa

#Đầu tiên chúng ta cần import thư viện random mà ta sử dụng
import random

#Khởi tạo 1 biến random integer từ 0 đến 1, tức là chỉ nhận 2 giá trị 0 và 1
random_side = random.randint(0,1)
if random_side == 0:
    print("Tails")
else:
    print("Heads")
