#Trong phần này chúng ta sẽ thực hiện thiết kế trò chơi blackjack phỏng theo trò chơi blackjack thông thường
#Blackjack là trò chơi với bộ bài tây, bao gồm nhiều lá bài 2,3,4,5,6,7,8,9,10,J,Q,K,A
#Luật của trò chơi này như sau:
#Người chia bài gọi là nhà cái sẽ chia cho chúng ta 2 lá bài và chia cho họ (nhà cái) 2 lá bài
#Chúng ta được quyền biết trước 2 lá bài của mình và lá bài đầu tiên của người chia bài
#Chúng ta có quyền được bốc thêm 1 lá bài hoặc không sao cho tổng các lá bài của chúng ta gần với 21 nhất và đồng thời phải dự đoán xem có lớn hơn tổng điểm của người chia bài hay không
#Nếu tổng số điểm của chúng ta lớn hơn người chia bài và không quá 21, chúng ta sẽ thắng
#Ngược lại chúng ta sẽ thua khi tổng điểm của chúng ta lớn hơn 21 hoặc bé hơn tổng điểm của người chia bài
#Nếu điểm của người chia bài bé hơn 16 điểm thì họ phải bốc thêm 1 lá nữa

import random

def game(computer_cards, your_cards, cards):
    computer_cards_score = 0
    your_cards_score = 0
    for card in computer_cards:
        computer_cards_score += cards[card]
    for card in your_cards:
        your_cards_score += cards[card]
    if computer_cards_score == your_cards_score or computer_cards_score > 21 and your_cards_score > 21:
        return f"Computer scores: {computer_cards_score}, your scores: {your_cards_score}. Draw!"
    elif your_cards_score <= 21 and computer_cards_score <= 21:
        if your_cards_score > computer_cards_score:
            return f"Computer scores: {computer_cards_score}, your scores: {your_cards_score}. You win!"
        else: 
            return f"Computer scores: {computer_cards_score}, your scores: {your_cards_score}. You lose!"
    elif your_cards_score > 21:
        return f"Computer scores: {computer_cards_score}, your scores: {your_cards_score}. You lose!"
    else:
        return f"Computer scores: {computer_cards_score}, your scores: {your_cards_score}. You win!"


def main_game():
    cards = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 10
}
    computer_cards = [random.choice(list(cards.keys())) for i in range(2)]
    your_cards = [random.choice(list(cards.keys())) for i in range(2)]

    print(f"Computer cards: {list(computer_cards[0])}")
    print(f"Your cards: {your_cards}")

    continue_collect = input("Do you want to collect a new card? Type 'yes' or 'no'.\n")
    if continue_collect == 'yes':
        your_cards.append(random.choice(list(cards.keys())))

    computer_cards_score_now = 0
    for card in computer_cards:
        computer_cards_score_now += cards[card]
    if computer_cards_score_now <= 16:
        computer_cards.append(random.choice(list(cards.keys())))
    
    result = game(computer_cards, your_cards, cards)

    print(f"Computer cards: {list(computer_cards)}")
    print(f"Your cards: {your_cards}")

    print(result)
    new_game = input("Do you want start a new game? (y/n): ")
    if new_game == "y":
        main_game()
    else:
        print("GOOD BYE!")

if __name__ == "__main__":
    main_game()