#Trong bài này chúng ta sẽ tìm hiểu về mã hóa Caesar Cypher, đây là mã hóa đơn giản và cổ xưa nhất
#Chúng ta sẽ xây dựng ứng dụng encode và decode của mã hóa Caesar Cypher
#Ý tưởng của mã hóa này là dịch chuyển tất cả các chữ cái trong bảng chữ cái tiếng Anh để tạo ra một mã hóa
#Ví dụ chúng ta có thể dịch chuyển sang trái 1, 2, 3 , 4... ký tự

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction= input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your meassage:\n").lower().strip()
shift = int(input("Type the shift number:\n"))

