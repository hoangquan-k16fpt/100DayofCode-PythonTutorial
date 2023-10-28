#Ở bài học này, chúng ta sẽ làm quen với hàm (function) có đầu ra, tức là hàm sẽ return lại cụ thể một giá trị nào đó
#Giá trị mà hàm return lại có thể là string, int, float ... hay bất cứ kiểu dữ liệu nào như list, dictinary...

def format_name(f_name,l_name):
    #Tại đây chúng ta có gọi hàm title(), đây là hàm để đọc các phần tử trong 1 string truyền vào và sẽ viết hoa chữ cái đầu tiên của string đó, còn các kí tự tiếp theo sẽ viết thường
    format_f_name = f_name.title()
    format_l_name = l_name.title()
    #Ở đây chúng ta sẽ return trở lại một string bao gồm first name và last name
    return f"{format_f_name} {format_l_name}"
#Cuối cùng, để sử dụng, chúng ta gọi hàm. Tuy nhiên lưu ý vì hàm sẽ trả về một giá trị hay nói cách khác hàm khi này mang một giá trị cụ thể, nên chúng ta cần phải gán biến cho giá trị đó
formatted_name = format_name(f_name = "Quan", l_name= "ngo ba hoang")
print(formatted_name)
#Ngoài ra chúng ta cũng có thể print hẳn hàm mà không cần thông qua một biến khác
print("In hàm không thông qua biến: " + format_name(f_name = "Quan", l_name= "ngo ba hoang"))

