#Hàm trong Python còn có thể return nhiều lần, ta sẽ sử dụng cách này khi có nhiều trường hợp cho hàm và mỗi trường hợp sẽ được return một giá trị khác nhau

def format_name(f_name,l_name):
    #Ví dụ về việc xử lý return khi người không nhập gì vào f_name và l_name
    if f_name == "" and l_name == "":
        return "You do not input valid name!"
    format_f_name = f_name.title()
    format_l_name = l_name.title()
    return f"Result: {format_f_name} {format_l_name}"

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
formatted_name = format_name(f_name,l_name)
print(formatted_name)
