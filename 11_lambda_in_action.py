my_friends = ["Vári Róbert", "Kiss Balázs", "Kovács Elemér", "Tóth Krisztina"]
lucky_numbers = [12, 56, 83, 2, 4, 89]

movies = {
    1: {"title": "Lift", "score": 63},
    2: {"title": "Napoleon", "score": 65},
    3: {"title": "The Marvels", "score": 64},
    4: {"title": "Aquaman and the Lost Kingdom", "score": 65},
    5: {"title": "Society of the Snow", "score": 80},
    6: {"title": "Deep Fear", "score": 53}
}

# def get_sort_key(movie_id):
#     return movies[movie_id]["score"]

# result = sorted(movies, key=get_sort_key, reverse=True)

result = sorted(movies, key=lambda movie_id : movies[movie_id]["score"], reverse=True)
for movie_id in result:
    print(movies[movie_id])