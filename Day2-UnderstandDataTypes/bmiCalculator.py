#Trong phần này chúng ta sẽ viết một chương trình tính chỉ số BMI (khối cơ thể) của một ai đó bất kì

#1st input: enter height in meters (ex: 1.65)
height = input("Enter your height:\t")
#2nd input: enter weight in kilograms (ex: 50)
weight = input("Enter your weight:\t")
#Do not change the code above
#Write your code here
#Khi nhập vào từ bàn phím, kiểu dữ liệu sẽ là string, nên cần phải ép kiểu cho height và weight
#Nếu không muốn phải ép kiểu, bạn còn có thê, 1 lựa chọn nữa cho lệnh input:

# height = float(input())
# weight = float(input())

weight = float(weight)
height = float(height)

bmi = weight / (height ** 2)

#Ta cần chuyển chỉ số BMI về dạng integer để làm tròn
bmi = int(bmi)

print("Your BMI: " + str(bmi))

