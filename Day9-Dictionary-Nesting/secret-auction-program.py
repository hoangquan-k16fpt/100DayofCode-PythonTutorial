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
#Khai báo dictionary chứa thông tin người đấu giá và giá mà họ chọn
#Khi sử dụng dictionary, nếu một người ra giá nhiều lần ta có thể ghi đè giá của họ, tức là sẽ ghi đè giá cuối cùng của mỗi người
bid = {}
bidding_finished = False
#Ta sẽ gọi vòng lặp while để chương trình có thể chạy một cách mượt mà nhất và sẽ không bị dừng chương trình
while not bidding_finished:
    #Input các thông tin cần thiết bao gồm tên người đấu giá và mức giá mà họ đưa ra
    name = input("What is your name? ").strip()
    price = int(input("What is your price? $"))
    #Tiếp tục ghi thông tin vào trong dictionary
    bid[name] = price
    #Để buổi đấu giá tiếp tục hoặc dừng lại, cần hỏi xem có ai còn muốn trả mức giá cao hơn nữa không
    cont = input("Are there any other bidders? Type 'yes' or 'no'\n").lower().strip()
    if cont == 'yes':
        clear_cmd()
    elif cont == 'no':
        clear_cmd()
        bidding_finished = True
        find_winner(bid)
