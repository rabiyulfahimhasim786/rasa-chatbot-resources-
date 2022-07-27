import sqlite3

conn = sqlite3.connect('datas.db')
print("Opened database successfully")

## Table Creation
conn.execute('''CREATE TABLE rasa (ID INT PRIMARY KEY  NOT NULL,
        NAME TEXT,
        PHONE TEXT);''')
print("Table created successfully");

## Print All the rows In table
cursor = conn.execute("SELECT ID, NAME, PHONE from rasa")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("PHONE = ", row[2], "\n")

## Insert In The Table
#conn.execute("INSERT INTO rasa (ID,NAME,PHONE) \
#      VALUES (1, 'Rabiyul fahim', '+918778763117')");
   #   VALUES (1, 'Kaustubh Pathak', '+919149042316', 'kaus.pathak@gmail.com', 'veg')");
#conn.commit()
conn.close()