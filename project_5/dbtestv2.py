import sqlite3

def main():
    try:
        con = sqlite3.connect('test.db')

        cur = con.cursor()
        cur.execute('CREATE TABLE Pets(Id INT, Name TEXT, Price INT)')
        cur.execute('INSERT INTO Pets VALUES(1, "Cat", 400)')
        cur.execute('INSERT INTO Pets VALUES(1, "Dog", 600)')
        cur.execute('INSERT INTO Pets VALUES(1, "Rabbit", 200)')
        cur.execute('INSERT INTO Pets VALUES(1, "Bird", 60)')

        con.commit()


        cur.execute('SELECT * FROM Pets')
        data = cur.fetchall()

        for row in data:
            print(row)

    except sqlite3.Error:
        if con:
            print("Error: Rolling back")
            con.rollback()
    finally:
        if con:
            con.close()

if __name__ == '__main__':
    main()
