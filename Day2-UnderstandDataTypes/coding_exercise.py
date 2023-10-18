#Trong bài tập này, nhập vào 1 số nguyên có 2 chữ số sau đó in ra tổng của các chữ số có trong đó
#Input: 39
#Output: 12
#input: 49
#Output: 13

#Do not change below code line
two_digits_number = input()
#Do not change above code line
###################################
#Write your code here
#Kiểm tra kiểu dữ liệu nhập vào
print(type(two_digits_number))

#Bởi vì là kiểu integer nên không thể lấy từng index trong giá trị mà phải ép kiểu về string
str_two_digits_number = str(two_digits_number)

#Lấy từng phần tử trong string mới và ép kiểu lại về integer
two_digits_number_1 = int(str_two_digits_number[0])
two_digits_number_2 = int(str_two_digits_number[1])

#Sau đó in ra tổng của 2 biến vừa có được là kết quả của bài toán
print(two_digits_number_1 + two_digits_number_2)