#Trong bài này chúng ta sẽ có một từ điển bao gồm tên và điểm số của từng học sinh
#Nhiệm vụ của bạn là hãy dựa vào điểm số của từng học sinh để tạo ra một từ điển mới đánh giá xếp hạng của từng học sinh đó

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#Trước tiên, chúng ta cần phải tạo một từ điển mới
student_grades = {}
#Tiếp theo, chúng ta sẽ lặp qua từng students trong student_scores và tạo thêm các giá trị cho từ điển mới
for item in student_scores:
    score = student_scores[item]
    if score > 90:
        student_grades[item] = "Outstanding"
    elif score > 80:
        student_grades[item] = "Exceeded Expectations"
    elif score > 70:
        student_grades[item] = "Acceptable"
    else:
        student_grades[item] = "Fail"

print(student_grades)

