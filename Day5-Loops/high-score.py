#Trong bài toán này chúng ta sẽ xây dựng chương trình tương tự như ở bài tập trước
#Ý tưởng của bài toán là nhập vào các điểm số của học sinh trong 1 lớp và thực hiện việc tìm ra điểm số cao nhất
#Đầu vào input sẽ là một string bao gồm các điểm số của học sinh, mỗi điểm số sẽ cách nhau bằng 1 space
#Chúng ta có thể định nghĩa kiểu của score là int hoặc float, ở đây tôi đang sử dụng float, nếu định nghĩa score kiểu int, chuyển toàn bộ float thành int
scores = input().split()
for n in range(0, len(scores)):
    scores[n] = scores[n]

highest_score = scores[0]
highest_score = float(highest_score)
for score in scores: 
    if(float(score) > highest_score):
        highest_score = float(score)

print(f"Highest score: {highest_score}")
    