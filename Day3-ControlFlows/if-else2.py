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
        bill = 5
        print("Children ticket: $5.")
    elif age <= 18:
        bill = 7
        print("Youth ticket: $7.")
    else:
        bill = 12
        print("Adult ticket: $12.")
    
    #Ở đây chúng ta sẽ sử dụng kiểm tra điều kiện if thêm 1 lần nữa. 
    #Sự khác biệt ở đây là nếu chúng ta sử dụng if liên tục thì cho dù lệnh if ở trên có đúng hay không thì lệnh if ở dưới vẫn sẽ được thực thi
    takephoto = input("Do you want to take a photo? (y/n): ")
    if takephoto == "y":
        bill += 3
    print(f"Your total bill is ${bill}") 
else: 
    print("Sorry, you have to grow taller before you can ride")