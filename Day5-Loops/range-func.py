#Trong bài này, chúng ta sẽ tìm hiểu về vòng lặp trong range function
#Khi viết mã không phải lúc nào ta cũng có thể sử dụng vòng lặp với list danh sách
#Ví dụ như khi chúng ta muốn cộng tổng tất cả các số từ 0 đến 100, chúng ta không nên đưa tất cả các số đó vào trong 1 danh sách và cộng chúng lại với nhau
#Chúng ta sẽ thử làm một ví dụ nhỏ

total = 0
#Khi sử dụng vòng lặp for với range, ta phải chú ý đó là range(a,b) sẽ được duyệt từ a tới b-1
for number in range(0,101):
    total += number
print(total)

#Ngoài ra hàm range còn có một chức năng đặt bước nhảy của giá trị
for number in range(0,10,3):
    print(number)

