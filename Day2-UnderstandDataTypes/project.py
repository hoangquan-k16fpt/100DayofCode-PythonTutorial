#Viết chương trình tính tiền tip bằng cách nhập vào tổng bill, phần trăm số tiền tip trên tổng bill và số người sẽ chia tiền
#Output của bài toán sẽ hiển thị ra số tiền mà mỗi người cần phải trả

print("Welcome to tip calculator")
total_bill = float(input("What was the total bill? "))
tip_percentage = float(input("What percentage tip would like to give? "))
split_bill = int(input("How many people to split the bill? "))

person_pay = (total_bill + ((total_bill/100) * tip_percentage)) / split_bill
print(f"Each person should pay: ${round(person_pay, 2)}")