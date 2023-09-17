import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="8889",
    user="root",
    password="root",
    database="newslist"
)

mycursor = mydb.cursor()

sql = "INSERT INTO emails (email) VALUES (%s)"
val = ["mahmud@example.com"]
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

sql = "SELECT * FROM emails WHERE email LIKE 'mahmud%' "
mycursor.execute(sql)

table = mycursor.fetchall()

for row in table:
    print(row)

# Stäng cursor och databasanslutning när programmet är klart
mycursor.close()
mydb.close()