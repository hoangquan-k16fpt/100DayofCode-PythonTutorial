#Trong bài này chúng ta sẽ nâng cấp chương trình tính toán BMI đơn giản học ở bài trước
#Khi biết được chỉ số BMI của user, sẽ đưa ra nhận định đối với mỗi user đó (béo, gầy, thừa cân...)

print("Welcome to BMI checker program.")
weight = float(input("Input your weight: "))
height = float(input("Input your height: "))
#Sử dụng lệnh điều kiện để kiểm tra chỉ số bmi của người dùng
bmi = weight / height**2
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you are normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese")
else:
    print(f"Your BMI is {bmi}, you are clinically obese")