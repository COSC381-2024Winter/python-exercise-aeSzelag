from movies import Movies

movies = Movies('./movies.txt')


def menu():
    print("Menu:")
    print("Enter q for quit")

if __name__ == "__main__":
    menu()
    user=input()
    while user != "q":
        menu()
        user =input()