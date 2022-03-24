import sqlite3

def convertToBinaryData(filename):
# Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
       
        return blobData
def create():
   con = sqlite3.connect("project.db")
   cur = con.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS new_image(id TEXT,Image VARCHAR)" ) 

   con.commit()
   con.close()
def insertBLOB(imid,image):
   
        sqliteConnection = sqlite3.connect('project.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO new_image
                                   VALUES (?, ?)"""
        
        dcd = convertToBinaryData(image)
        
       
        # Convert data into tuple format
        data_tuple = (imid,dcd)
        
        cursor.execute(sqlite_insert_blob_query, (imid,dcd))
        
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()
        
   

