#Các toán tử trong Python
#Python bao gồm các toán tử tính toán toán học thông thường
#Cộng:
print(7+5)

#Trừ:
print(10-3)

#Nhân:
print(3*6)
#Ta có thể kiểm tra kiểu dữ liệu của phép nhân 3*6 bằng cách như sau
print(type(3*6))

#Chia:
print(6/3)
##Ta có thể thấy khi thực hiện phép chia kiểu dữ liệu là kiểu float chứ không phải integer bằng cách kiểm tra
print(type(6/3))
#Output của lệnh print phía trên sẽ là 1 giá trị kiểu float

#Toán tử lũy thừa:
print(2**3)

#Trong Python cũng tuân thủ theo quy tắc của toán học thông thường, trong ngoặc sẽ được tính trước, rồi đến phép lũy thừa, nhân chia, cộng trừ
print(3 + 3 * 3 - 3 / 3)
#Hãy thử lại với lệnh sau:
print((3 + 3) * 3 - 3 / 3)
