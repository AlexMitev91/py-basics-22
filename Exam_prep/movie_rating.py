number_of_movies = int(input())

total_rating = 0
lowest_name = ""
highest_name = ""

lowest_rating = 10
highest_rating = 0

for current_movie in range(number_of_movies):
    movie_name = input()
    movie_rating = float(input())
    total_rating += movie_rating
    if movie_rating > highest_rating:
        highest_name = movie_name
        highest_rating = movie_rating
    if movie_rating < lowest_rating:
        lowest_name = movie_name
        lowest_rating = movie_rating

average_rating = total_rating / number_of_movies
print(f"{highest_name} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_name} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
