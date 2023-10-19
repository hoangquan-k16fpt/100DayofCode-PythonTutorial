#Tiếp tục từ bài tập trước, ở bài tập này ta sẽ học cách sử dụng lệnh điều kiện lồng nhau
print("Welcome to the rollercoaster")
your_height = float(input("Input your height in centimeters: "))
if your_height > 120:
    print("You can ride the rollercoaster")
    #Sau khi kiểm tra điều kiện height > 120 đúng thì sẽ kiểm tra tiếp điều kiện tuổi, nếu trên 18 tuổi thì sẽ pay 12$ còn nếu dưới 18 tuổi pay 7$.
    #Sử dụng lệnh điều kiện con tương tự như sử dụng lệnh điều kiện bình thường
    age = int(input("Enter your age: "))
    #Chú ý khi sử dụng lệnh điều kiện có elif thì để tối giản code cần kiểm tra flow xem có hợp lý hay không, một ví dụ minh họa:
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else :
        print("Please pay $12.")
else: 
    print("Sorry, you have to grow taller before you can ride")