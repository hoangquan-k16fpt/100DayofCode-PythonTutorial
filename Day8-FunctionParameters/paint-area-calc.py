#Trong bài này chúng ta sẽ giải quyết bài toán sơn tường, sử dụng hàm mà chúng ta vừa học
#Trong hướng dẫn của nhà sản xuất, một lọ sơn có thể sơn được 5m2 tường. Bạn hãy viết chương trình để người dùng nhập vào chiều dài và chiều rộng của bức tường, sau đó tính toán cần bao nhiêu lọ sơn để có thể sơn hết bức tường đó
#Viết hàm thực hiện việc tính toán
#Trong bài toán này, chúng ta có thể sử dụng hàm ceil của modeul math để làm tròn các giá trị float
import math
def paint_calc(height,width,cover):
    area = height * width
    total_paint = math.ceil(area/cover)
    print(f"Số thùng sơn cần có thể sơn hết bức tường: {total_paint} thùng.")

test_h = int(input("Chiều cao của bức tường: ")) # Height of wall (m)
test_w = int(input("Chiều rộng của bức tường: ")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)