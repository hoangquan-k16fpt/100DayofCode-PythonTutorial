#Trong bài này chúng ta sẽ xây dựng chương trình mô phỏng trò chơi fizzbuzz, luật của trò chơi này như sau
#Đếm số lần lượt từ 1 đến 100, nếu đến số chia hết cho 3 thì thay vì nói số đó sẽ nói fizz, số chia hết cho 5 sẽ nói buzz, còn số chia hết cho cả 3 và 5 sẽ nói fizzbuzz
#Đây cũng là một chương trình đơn giản, lời khuyên của tôi đó là bạn hãy tự viết mã của mình rồi sau đó tham khảo mã dưới đây
number = 100
for num in range(1, number + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
