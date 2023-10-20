#Trong bài tập này chúng ta sẽ viết một chương trình gọi là tính điểm tình yêu Love Calculator
#Ý tưởng của bài toán này là 2 người sẽ nhập tên vào và sau đó tính số lần xuất hiện của các chữ cái trong từ TRUE và từ LOVE trong tên của họ
#Ví dụ nếu số lần xuất hiện của các chữ cái trong từ TRUE là 5 và LOVE là 3, vậy số điểm của họ là 53

print("The love calculator is calculating your score...")
name1 = input("Input your name: ")
name2 = input("Input your lover name: ")
combined_name = name1 + name2
combined_name = combined_name.lower()
t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')
#Ở đây chúng ta sử dụng count để tính toán số chữ cái xuất hiện trong một chuỗi string
true_num = t + r + u + e
l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')
e = combined_name.count('e')
love_num = l + o + v + e

score = str(true_num) + str(love_num)
score = int(score)

if score < 10 and score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.") 
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
