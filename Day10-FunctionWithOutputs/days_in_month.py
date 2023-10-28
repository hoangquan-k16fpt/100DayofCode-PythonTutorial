#Trong bài tập này, chúng ta sẽ làm một project nhỏ về tính toán số ngày trong 1 tháng
#Đầu tiên chúng ta cần viết hàm kiểm tra xem năm đó có phải năm nhuận hay không

def is_leaf_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "leaf year"
            else:
                return "not leaf year"
        else:
            return "leaf year"
    else:
        return "not leaf year"

#Viết hàm tính toán ngày trong tháng, chú ý kiểm tra năm nhuận để tính toán chính xác
def days_in_month(year, month):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leaf_year(year) == "not leaf year" and month == 2:
        return 28
    else:
        return days[month - 1]

while True:
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    if month in range(1, 13):
        days = days_in_month(year, month)
        print(f"Total days of the month of the year is {days}.")
    else:
        print("You entered invalid month!")
        