#Trong bài học này chúng ta sẽ làm quen với câu lệnh if/else. Đây là một câu điều kiện (condition) nếu ... thì ...
#Dưới đây là ví dụ về chương trình sử dụng câu điều kiện

print("Welcome to the rollercoaster")
your_height = float(input("Input your height in centimeters: "))

#Nếu chiều cao người dùng nhập vào lớn hơn 120 thì họ sẽ đủ điều kiện để có thể lái 1 chiếc rollercoaster
if your_height > 120:
    print("You can ride the rollercoaster")
#còn nếu người dùng nhập chiều cao nhỏ hơn 120 thì họ sẽ không đủ điều kiện để có thể lái một chiếc rollercoaster
else: 
    print("Sorry, you have to grow taller before you can ride")
    
#Khi sử dụng ngôn ngữ Python cần đặc biệt chú ý về thụt đầu dòng sau mỗi câu lệnh if/else

#Ngoài ra bạn cũng có thể sử dụng các toán tử khác bao gồm: >, <, >=, <=, ==, !=
print("Welcome to the automotive vehicle")
your_height = float(input("Input your height in centimeters: "))
if your_height >= 160:
    print("You can ride the vehicle")
else: 
    print("Sorry, you have to grow taller before you can ride")
    