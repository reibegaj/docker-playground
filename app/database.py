import mariadb 
import os

#user = os.environ['MY_USER']
#password = os.environ ['MY_PASS']
#host = ['HOST_IP']
#database = ['DB_NAME']

if os.environ['ENV'] != "docker":
    dotenv_path = Path('./app.env')
    load_dotenv(dotenv_path=dotenv_path)

conn = mariadb.connect(
    user = os.environ["DB_USER"],
    password = os.environ["DB_PASS"],
    host = os.environ["DB_HOST"],
    database = os.environ["DB_NAME"]
    )

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
