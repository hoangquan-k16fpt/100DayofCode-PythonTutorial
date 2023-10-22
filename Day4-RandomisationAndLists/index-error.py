#Trong khi làm việc với list, ta sẽ thường hay gặp phải lỗi index error
#Lỗi này sẽ được chương trình đưa ra khi ta cố gắng truy xuất chỉ mục lớn hơn số chỉ mục của list (vượt khỏi phạm vi), tức là ta cố gắng truy xuát một phần tử không tồn tại trong list
state_of_us = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", 
               "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", 
               "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", 
               "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", 
               "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", 
               "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", 
               "Wyoming", "Washington, D.C."]

#Chúng ta sẽ kiểm tra len của list, tức là chúng ta đang đếm số phần tử đang có thực tế của list, tức là bắt đầu từ 1
#Tuy nhiên, index (chỉ mục) của list và các cấu trúc dữ liệu khác trong lập trình sẽ được bắt đầu từ 0
#Vì vậy, index (chỉ mục) của list sẽ trong phạm vi từ 0 đến len của list - 1
print(len(state_of_us))
#Ta thấy sau khi in ra len của list state_of_us là 51. Tuy nhiên để gọi phần tử cuối cùng của list trên, ta sẽ sử dụng chỉ mục 50.
print(state_of_us[50])

#Tiếp theo, chúng ta sẽ tìm hiểu về list lồng nhau, cũng là một cấu trúc của list mà ta sử dụng rất nhiều trong quá trình viết mã

fruits = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
vegetables = ["Avocados", "Sweet corn", "Pineapples", "Cabbages", "Onions", "Sweet peas (frozen)", "Papayas", "Asparagus", "Mangoes", "Eggplants", "Honeydew melons", "Kiwis", "Cantaloupes", "Cauliflower", "Broccoli"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
#Sau khi in ra chúng ta sẽ thấy được các list lồng nhau nằm trong 1 list lớn, bao gồm fruits và vegetables, tuy nhiên chúng cũng nằm trong list dirty_dozen
#Để truy xuất khi sử dụng list lồng nhau, ta sử dụng index lồng nhau

print(dirty_dozen[1][2])
#Như vậy ta có thể truy xuất được phần tử index thứ 2 trong phần tử index thứ 1 trong dirty_dozen

