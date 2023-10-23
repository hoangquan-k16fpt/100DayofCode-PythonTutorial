#Trong bài tập này chúng ta sẽ viết một chương trình nhập vào từ bàn phím một số, và ta sẽ tính tổng tất cả các số chẵn từ 0 tới số đó
#Đây là một bài tập cơ bản và đơn giản, bạn nên tự viết mã của mình rồi sau đó tham khảo mã dưới đây

number = int(input("Input your number: "))
total = 0
for num in range(0, number + 1, 2):
    total += num
print(f"Total: {total}")

#Ngoài cách giải quyết ở trên, ta cũng còn một cách giải quyết nữa sử dụng câu lệnh điều kiện bên trong vòng lặp for
total_2 = 0
for n in range(0, number + 1):
    if n % 2 == 0:
        total_2 += n
print(f"Total use condition function: {total_2}")
#Sau khi in ra ta có thể thấy 2 kết quả đều cho ra giống nhau