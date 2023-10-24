#Trong bài tập này chúng ta sẽ tạo ra một Hangman game đơn giản
#Hangman game còn được gọi là game treo cổ, người chơi sẽ phải đoán từng ký tự trong một từ, nếu đoán sai thì sẽ vẽ thêm một nét vào người treo cổ
#Nếu vẽ đủ 6 nét thành người treo cổ hoàn chỉnh, thì người chơi sẽ thua
#Ngược lại, nếu đoán đúng được tất cả các ký tự trong từ, người chơi sẽ thắng
#Trong bài này chúng ta sẽ sử dụng những kiến thức đã được học bao gồm list, vòng lặp for, while và random để tạo ra trò chơi hoàn chỉnh
import random
import word_list, stages
#Chúng ta cần tạo ra 2 file stages và word_list, 2 file này sẽ chứa lần lượt list hình ảnh ascii của người treo cổ và những từ mà máy sẽ random cho người chơi
#Vậy nên chúng ta cần import 2 file này vào file chính
stages = stages.stage
word_list = word_list.list

chosen_word = random.choice(word_list)

display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

isEnd = False
lives = 6

while not isEnd:
    user_chosen = input("Input your character: ").lower()
    for position in range(len(chosen_word)):
        if chosen_word[position] == user_chosen:
            display[position] = user_chosen
    print(display)
    if user_chosen not in chosen_word:
        lives -= 1
        if lives == 0:
            isEnd = True
            print("You lose!")
    if "_" not in display:
        isEnd = True
        print("You won!")
    print(stages[6 - lives])