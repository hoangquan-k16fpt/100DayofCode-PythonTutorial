#Trong bài toán này chúng ta sẽ thực hiện một chương trình đánh dấu bản đồ (map)
line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]

map = [line1, line2, line3]
print("Hiding your treasure. X marks the spot.")
position = input("Input position ")

letter = position[0].lower()
letter_list = ["a", "b", "c"]

letter_index = letter_list.index(letter)

num_index = int(position[1]) - 1
map[num_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}\n")

