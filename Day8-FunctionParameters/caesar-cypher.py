#Trong bài này chúng ta sẽ tìm hiểu về mã hóa Caesar Cypher, đây là mã hóa đơn giản và cổ xưa nhất
#Chúng ta sẽ xây dựng ứng dụng encode và decode của mã hóa Caesar Cypher
#Ý tưởng của mã hóa này là dịch chuyển tất cả các chữ cái trong bảng chữ cái tiếng Anh để tạo ra một mã hóa
#Ví dụ chúng ta có thể dịch chuyển sang trái 1, 2, 3 , 4... ký tự

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower().strip()
shift = int(input("Type the shift number:\n"))

#Trong bài tập này chúng ta sẽ phải xây dựng 2 hàm encode và decode cho Caesar Cypher
def encrypt(text, shift):
    cypher_text = ""
    for letter in text:
        if letter == " ":
            cypher_text += " "
            continue
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cypher_text += new_letter
    print(f"The encode is {cypher_text}")

def decrypt(text, shift):
    decypher_text = ""
    for letter in text:
        if letter == " ":
            decypher_text += " "
            continue
        position = alphabet.index(letter)
        new_position = position - shift
        new_letter = alphabet[new_position]
        decypher_text += new_letter
    print(f"The decrypt is {decypher_text}")
    
if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decrypt(text,shift)
else:
    print(f"You must type 'encode' or 'decode'")

#Sau khi xây dựng xong, chúng ta thấy có khá nhiều thao tác được lặp lại trong 2 hàm encrypt và decrypt, để tối ưu code, ta có thể đưa chúng về thành 1 hàm để thực hiện toàn bộ chức năng của Caesar Cypher
#Chúng ta sẽ xây dựng hàm đó trong file caesar-cypher-2.py

