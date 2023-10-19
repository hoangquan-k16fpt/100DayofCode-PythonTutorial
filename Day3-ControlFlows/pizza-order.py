#Trong bài toán này chúng ta sẽ xây dựng hệ thống đặt pizza có tên Pizza Delivery
#Sử dụng câu lệnh điều kiện để xây dựng chương trình đặt hàng pizza đơn giản
print("Thank you for choosing Pizza Devlivery.")
print("Small pizza (S): $15\nMedium pizza (M): $20\nLarge pizza (L): $25")
size = input("Choose your size of your pizza: ")
add_peperonies = input("Add peperonies: ")
if size == "S":
    bill = 15
    if add_peperonies == "Y":
        bill += 2
elif size == "M":
    bill = 20
    if add_peperonies == "Y":
        bill += 3
elif size == "L":
    bill = 25
    if add_peperonies == "Y":
        bill += 3
add_cheese = input("Add extra cheese: ")
if add_cheese == "Y":
    bill += 1

print(f"Your total bill is ${bill}")
