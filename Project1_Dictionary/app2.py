import mysql.connector

def open_connection():
    con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
    )
    return con

def search_meaning():
    cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
    results = cursor.fetchall()

    if results:
        for result in results:
            print(result[1])
    else:
        print("No word found")


word = input("Enter a word: ")

connection = open_connection()

cursor = connection.cursor()

search_meaning()
