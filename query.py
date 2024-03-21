from movies import Movies
import sys

movies = Movies('./movies.txt')








        


#set up the menu options: 
def menu_options():
    print("Please choose an option:")
    print("\'list\' to display a list of movies in the database")
    print("\'q\' for exit")

#method for displaying the movie dictionary
def list_movies():
    print("here")

#process user input through the menu system
def menu_selection():
    while True:
        menu_options()
        option = input()

        if option == 'q':
            break
        elif option == 'list':
            list_movies()
        else:
            print("invalid option")


if __name__ == "__main__":
    menu_selection()