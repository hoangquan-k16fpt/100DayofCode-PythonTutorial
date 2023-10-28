#Ở bài này, chúng ta sẽ tìm hiểu thêm về một kiểu cấu trúc dữ liệu mới trong Python, được gọi là docstring
#Khi sử dụng kiểu docstring, giống như là một comment có nhiều dòng
#Miễn là bạn không sử dụng bất cứ biến nào cho docstring, chương trình của bạn vẫn sẽ chạy bình thường
#Khi sử dụng docstring, phần này sẽ xuất hiện khi bạn gọi hàm

from datetime import datetime
def example_docstring(name, age, gender):
    #Ta sẽ thêm docstring vào trong hàm
    """_summary_

    Args:
        name (_type_): name of person who entry the tower
        age (_type_): age of person who entry the tower
        gender (_type_): gender of person who entry the tower

    Returns:
        _type_: _description_
    """
    name = name.strip()
    age = age
    gender = gender.strip()
    current = datetime.now()
    return f"Name: {name}, Age: {age}, Gender: {gender}, Entry time: {current}."

#Khi di chuột vào hàm gọi, ta có thể thấy được docstring
info = example_docstring("Quan", 20, "Male")

print(info)
