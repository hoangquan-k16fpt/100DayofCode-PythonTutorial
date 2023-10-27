#Trong bài này chúng ta sẽ tạo ra một chương trình mô phỏng một buổi đấu giá 
#Các người đấu giá sẽ nhập tên và giá mà họ đặt cho món đồ, điều này sẽ được lưu trữ vào trong một dictionary, cho đến cuối cùng nếu không còn ai ra giá nữa thì sẽ trích xuất dữ liệu từ dictionary xem ai là người thắng cuộc
#Đây chính là project cuối ngày của bạn mà bạn phải thực hiện
import os
#Đầu tiên chúng ta cần phải tạo một hàm xóa cmd bằng cách sử dụng module os của Python
def clear_cmd():
    os.system('cls' if os.name == 'nt' else 'clear')
#Định nghĩa hàm xử lý tìm ra người thắng cuộc
def find_winner(bid):
    highest_bid = 0
    winner = ""
    for item in bid:
        bidding_amount = bid[item]
        if highest_bid < bidding_amount:
            highest_bid = bidding_amount
            winner = item
    print(f"The winner of the bidding is {winner} with ${highest_bid}")

#Khai báo và thực thi hàm main thực thi chính
bid = {}
bidding_finished = False
while not bidding_finished:
    name = input("What is your name? ").strip()
    price = int(input("What is your price? $"))
    bid[name] = price
    cont = input("Are there any other bidders? Type 'yes' or 'no'\n").lower().strip()
    if cont == 'yes':
        clear_cmd()
    elif cont == 'no':
        bidding_finished = True
        find_winner(bid)
