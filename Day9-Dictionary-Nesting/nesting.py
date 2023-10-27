#Tiếp theo, chúng ta sẽ tìm hiểu một cấu trúc được gọi là Nesting trong Python
#Ta sẽ có một từ điển lồng trong từ điển, hoặc một danh sách lồng trong từ điển và ngược lại, khi đó đây chính là cấu trúc nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "Indonesia": "Jakarta",
}

travel_logs = {
    "France": ["Paris", "Lille", "Lyon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Cấu trúc nesting từ điển nằm trong từ điển và list nằm trong từ điển
travel_logs_2 = {
    "France": {"cities visited": ["Paris", "Lille", "Lyon"], "total_vistited": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visited": 5},
}

#Cấu trúc nesting từ điển nằm trong list và list nằm trong từ điển
travel_logs_3 = [
    {
        "country": "France" , 
        "cities visited": ["Paris", "Lille", "Lyon"], 
        "total_vistited": 12
        },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visited": 5
        },
]

#Nếu muốn in France:
print(travel_logs_3[0]["country"])