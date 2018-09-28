import sqlite3
from contextlib import closing
from objects import Movie

def add_movie(conn, movie):
    with closing(conn.cursor()) as cursor:
        stmt = """insert into movie (categoryID, name, year, minutes)
                    values (?,?,?,?)"""
        cursor.execute(stmt, (movie.category_id, 
                                movie.title, movie.year, movie.minutes))
        conn.commit()

def get_movies(conn):
    movies = []
    with closing(conn.cursor()) as cursor:
        query = "select name, year, minutes from movie"  
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            movies.append(Movie(row["name"],
                            row["year"], row["minutes"]))
    return movies


def main():
    #add add_movie function
    #add list_movies function. add movies to a Movie class
    conn = sqlite3.connect("/murach/python/_db/movies.sqlite")
    conn.row_factory = sqlite3.Row

    choice = input("enter list or add: ")

    if choice == "list":
        movies = get_movies(conn)
        for movie in movies:
            print(movie.title, movie.year, movie.minutes)
    elif choice == "add":
        print("Enter movie info")
        print()
        name = input("Movie title: ")
        year = input("Year: ")
        minutes = input("Minutes: ")
        movie = Movie(name, year, minutes)

        add_movie(conn, movie)


if __name__ == "__main__":
    main()