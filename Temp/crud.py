# CRUD i Python

import mysql.connector

# Anslut till MySQL-databasen
db_connection = mysql.connector.connect(
    host="localhost",
    port="8889",
    user="root",
    password="root",
    database="newslist"
)

# Skapa en cursor för att utföra SQL-frågor
cursor = db_connection.cursor()


def create_record():
    email = input("Ange email: ")

    # SQL-fråga för att lägga till en ny rad i tabellen
    sql_query = "INSERT INTO emails (email) VALUES (%s)"
    val = [(email)]
    cursor.execute(sql_query, val)
    db_connection.commit()
    print("Ny rad har skapats.")


def read_records():
    # SQL-fråga för att hämta data från tabellen
    sql_query = "SELECT * FROM emails"
    cursor.execute(sql_query)
    result = cursor.fetchall()

    # Skriv ut resultaten
    for row in result:
        print(row)


def update_record():
    record_id = int(input("Ange ID för raden som ska uppdateras: "))
    new_email = input("Ange den nya e-postadressen: ")

    # SQL-fråga för att uppdatera data i tabellen
    sql_query = "UPDATE emails SET email = %s WHERE id = %s"
    val = (new_email, record_id)
    cursor.execute(sql_query, val)
    db_connection.commit()
    print("Raden har uppdaterats.")


def delete_record():
    record_id = int(input("Ange ID för raden som ska tas bort: "))

    # SQL-fråga för att ta bort en rad från tabellen
    sql_query = "DELETE FROM emails WHERE id = %s"
    val = (record_id,)
    cursor.execute(sql_query, val)
    db_connection.commit()
    print("Raden har tagits bort.")


while True:
    print("\nVälj en åtgärd:")
    print("1. Skapa ny rad")
    print("2. Visa alla rader")
    print("3. Uppdatera rad")
    print("4. Ta bort rad")
    print("5. Avsluta")

    choice = input("Ange ditt val: ")

    if choice == "1":
        create_record()
    elif choice == "2":
        read_records()
    elif choice == "3":
        update_record()
    elif choice == "4":
        delete_record()
    elif choice == "5":
        break
    else:
        print("Ogiltigt val. Försök igen.")

# Stäng cursor och databasanslutning när programmet är klart
cursor.close()
db_connection.close()
