import sqlite3

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

def readBlobData(Id):
    try:
        sqliteConnection = sqlite3.connect('project.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_fetch_blob_query = """SELECT * from new_image where id = ?"""
        cursor.execute(sql_fetch_blob_query, (Id,))
        record = cursor.fetchall()
        for row in record:
           
            
            photo = row[1]
            

          
            photoPath = "File.jpg"
            
            writeTofile(photo, photoPath)
            

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")

