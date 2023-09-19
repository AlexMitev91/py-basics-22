movie_name = input()
theatre_type = input()
tickets_number = int(input())

total_income = 0

if movie_name == "A Star Is Born":
    if theatre_type == "normal":
        total_income = tickets_number * 7.50
    elif theatre_type == "luxury":
        total_income = tickets_number * 10.50
    elif theatre_type == "ultra luxury":
        total_income = tickets_number * 13.50
elif movie_name == "Bohemian Rhapsody":
    if theatre_type == "normal":
        total_income = tickets_number * 7.35
    elif theatre_type == "luxury":
        total_income = tickets_number * 9.45
    elif theatre_type == "ultra luxury":
        total_income = tickets_number * 12.75
elif movie_name == "Green Book":
    if theatre_type == "normal":
        total_income = tickets_number * 8.15
    elif theatre_type == "luxury":
        total_income = tickets_number * 10.25
    elif theatre_type == "ultra luxury":
        total_income = tickets_number * 13.25
elif movie_name == "The Favourite":
    if theatre_type == "normal":
        total_income = tickets_number * 8.75
    elif theatre_type == "luxury":
        total_income = tickets_number * 11.55
    elif theatre_type == "ultra luxury":
        total_income = tickets_number * 13.95

print(f"{movie_name} -> {total_income:.2f} lv.")