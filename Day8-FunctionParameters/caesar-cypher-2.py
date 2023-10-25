#Trong bài này chúng ta sẽ tìm hiểu về mã hóa Caesar Cypher, đây là mã hóa đơn giản và cổ xưa nhất
#Chúng ta sẽ xây dựng ứng dụng encode và decode của mã hóa Caesar Cypher
#Ý tưởng của mã hóa này là dịch chuyển tất cả các chữ cái trong bảng chữ cái tiếng Anh để tạo ra một mã hóa
#Ví dụ chúng ta có thể dịch chuyển sang trái 1, 2, 3 , 4... ký tự
cont = True
while cont:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower().strip()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    #Trong bài tập này, ta sẽ xây dựng 1 hàm Caesar Cypher duy nhất để thực hiện cả công việc decode và encode luôn trong 1 hàm
    #Ta sẽ thực hiện chia luồng chạy của hàm bằng cách dựa vào direction
    #Vì vậy ta cần phải truyền tham số direction vào trong hàm Caesar Cypher
    def CipherCaesar(direction, text, shift):
        end_text = ""
        if direction == "decode":
            shift *= -1
        for letter in text:
            if letter not in alphabet:
                end_text += letter
                continue
            position = alphabet.index(letter)
            new_position = position + shift
            new_letter = alphabet[new_position]
            end_text += new_letter
        print(f"{direction} successfully: {end_text}")

    #Sau khi xây dựng xong hàm, ta chỉ cần gọi hàm và truyền tham số cần thiết vào hàm
    #Code của chúng ta đã ngắn gọn và dễ nhìn hơn rất nhiều, tránh được câu lệnh if else lặp di lặp lại nhiều lần
    CipherCaesar(direction=direction, text = text, shift= shift)
    
    restart = input("Type 'yes' to continue and 'no' to quit the program.\n").strip().lower()
    if restart == 'no':
        cont = False
        print("Thanks for using Caesar Cipher Cryption Program!")
#Sau khi làm xong phần hàm chính, ta cần phải tinh chỉnh lại code để chương trình có thể chạy một cách mượt mà, tôi đã thêm vào vòng lặp while để có thể kiểm soát luồng xem người dùng có còn muốn tiếp tục sử dụng chương trình nữa hay không
#Ngoài ra, tôi cũng đã xử lý một số case đặc biệt, ví dụ như người dùng nhập số/ký tự/khoảng trắng thì chúng ta sẽ giữ nguyên
#Hoặc khi người dùng nhập một shift quá lớn, tôi đã thêm vào đó một câu lệnh để giảm shift nhỏ đi bằng cách lấy shift chia lấy dư cho 26 ký tự trong bảng chữ cái tiếng Anh
