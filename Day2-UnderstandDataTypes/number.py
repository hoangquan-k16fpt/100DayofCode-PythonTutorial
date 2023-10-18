#Trong Python cung cấp hàm để làm tròn số thập phân
print(round(7/4))

#Ngoài ra chúng ta cũng có thể lựa chọn làm tròn đến bao nhiêu chữ số thập phân bằng cách
print(round(33 / 4 , 2))
print(round(2.666666666,2))
#Làm tròn đến 2 chữ số thập phân
#Ngoài ra chúng ta cũng có thể thực hiện phép chia // để làm tròn thành integer
print(9 // 4)
print(type(9 // 4))

#Python cung cấp các toán gửi +=, -=, /= ,*=
result = 4 / 2
result /= 2
print(result)
score = 0
score += 4
print(score)

#Khi print chúng ta chỉ có thể nối những string với nhau, tuy nhiên ta không thể lúc nào cũng ép kiểu chúng về string được, ta có thể làm như sau:
score = 9
float_score = 8.3333
isLoad = True
name = "Angela"

print(f"Your name is {name} and your score is {score}, isLoaded is {isLoad} and float_score is {float_score}")
#Khi này chúng ta đã có thể in thành công mà không cần ép kiểu thủ công bất cứ một biến nào.
