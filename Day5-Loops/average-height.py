#Đầu tiên ta sẽ input vào chiều cao của các học sinh, mỗi chiều cao sẽ được ngăn cách nhau bởi space
#Tiếp theo ta sẽ gán chiều cao của học sinh thành một list danh sách bằng cách sử dụng vòng lặp for
student_height = input().split()
for n in range(0, len(student_height)):
    student_height[n] = student_height[n]

#Tiếp theo ta sẽ tính tổng chiều cao bằng cách duyệt qua list bằng vòng lặp for
#Sau đó in ra tổng chiều cao, len của list chính là số students và sử dụng round để làm tròn average chiều cao
total_height = 0
for height in student_height:
    total_height += int(height)

#Ngoài ra ta có thể sử dụng vòng lặp để tính toán số students, tuy nhiên cách này sẽ dài hơn sử dụng hàm len
student = 0
for students in student_height:
    student += 1
    
print(f"Total height = {total_height}")
print(f"Number of students = {len(student_height)}")
print(f"Average height = {round(total_height / len(student_height))}")

#Khi in ra số student trong vòng lặp, ta vẫn có kết quả tương tự như khi sử dụng len:
print(f"Number of students using loops: {student}")