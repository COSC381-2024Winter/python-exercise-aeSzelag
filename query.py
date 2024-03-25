from movies import Movies
import sys

movies = Movies('./movies.txt')








        


#set up the menu options: 
def menu_options():
    print("----------------------------------")
    print("Main Menu:")
    print("\'list\' to display a list of movies in the database")
    print("\'name\' to search movie names in the database")
    print("\'cast\' to search movie database by cast member name")
    print("\'q\' for exit")

#method for displaying the movie dictionary
def list_movies():
    print("Movie List:")
    for row_idx, movie_name in enumerate(movies._movies, start=1):
        print(f"{row_idx}. {movie_name['name']}")

def search_movies_name(search_term):
    found_movies = [movie['name'] for movie in movies._movies if search_term.lower() in movie['name'].lower()]

    if found_movies:
        print("Movies found:")
        for movie in found_movies:
            print(movie)
    else:
        print("No movies found with that search term.")

def search_movies_cast(search_term):
    found_movies = []

    for movie in movies._movies:
        cast_list = movie['cast']
        for cast_member in cast_list:
            if search_term.lower() in cast_member.lower():
                found_movies.append((movie['name'], cast_member))

    if found_movies:
        print("Movies found:")
        for movie, cast_member in found_movies:
            print(f"{movie}: {cast_member}")
    else:
        print("No movies found with that cast member.")

#process user input through the menu system
def menu_selection():
    while True:
        menu_options()
        option = input()

        if option == 'q':
            break
        elif option == 'list':
            list_movies()
        elif option == 'name':
            search_term = input("What movie name do you want to find? ")
            search_movies_name(search_term)
        elif option == 'cast':
            search_term = input("What cast name do you wish to look for? ")
            search_movies_cast(search_term)
        else:
            print("invalid option")


if __name__ == "__main__":
    menu_selection()
