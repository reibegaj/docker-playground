import mariadb 

conn = mariadb.connect(
    user="root",
    password="reidb",
    host="172.20.0.2",
    database="ReiDatabase")
cur = conn.cursor() 

#retrieving information 
some_name = "Denis" 
cur.execute("SELECT Emri,Mbiemri,Mosha FROM ReiTable WHERE Emri=?", (some_name,)) 

for first_name, last_name, age in cur: 
    print(f"Emri: {first_name}, Mbiemri: {last_name}, Mosha: {age},")
    
#insert information 
try: 
    cur.execute("INSERT INTO ReiTable (Emri,Mbiemri,Mosha) VALUES (?, ?, ?)", ("Lazaros","Ristani",19))
    print("Successfully inserted values")

except mariadb.Error as e: 
    print(f"Error: {e}")

conn.commit() 
    
conn.close()