#Trong bài toán này chúng ta sẽ tạo một game kéo bao búa đơn giản bằng cách sử dụng kiến thức mà ta đã học
#Ý tưởng của bài toán này là ta sẽ chọn một thứ trong kéo, bao, búa, sau đó sử dụng random để coi đó là lựa chọn của máy tính
import random

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papers = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
#Đặt hình ảnh của rock, paper and scissors vào trong 1 list
game_img = [rock, papers, scissors]

#Cho người dùng input số từ 0 đến 2 tương ứng với búa, bao, kéo
#Đồng thời random từ 0 đến 2 tương ứng với búa, bao, kéo
#Sử dụng câu lệnh điều kiện để tạo ra game, luật chơi tương tự như trò chơi kéo bao búa
#Để có thể in được game_img, ta sử dụng lệnh print và gọi phần tử trong list tương ứng với phần tử mà user hoặc computer đã chọn
user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
print(game_img[user_choose])
computer_choose = random.randint(0, 2)
print (f"Computer choose: {computer_choose}")
print(game_img[computer_choose])
if user_choose == 0 and computer_choose == 2:
    print("You win!")
elif computer_choose == 0 and user_choose == 2:
    print("You lose!")
elif computer_choose > user_choose:
    print("You lose!")
elif user_choose >= 3:
    print("You typed an invalid number, you lose!")
elif computer_choose < user_choose:
    print("You win!")
elif computer_choose == user_choose:
    print("It's draw!")



    