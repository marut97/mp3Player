import sqlite3

def main():
    try:
        sqliteConnection = sqlite3.connect('M:\\Projects\\MP3Player\\Database\\trialUser.dbo')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO `Music`
                              ('Title', 'Artist', 'Album', 'Genre','Path')
                               VALUES
                              ('Sugar','Maroon5','Sugar','Pop','M:\\Projects\\MP3Player\\Songs\\Sugar')"""

        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

if __name__ == '__main__':
    main()
