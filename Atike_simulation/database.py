import sqlite3
from _ast import Return


class Bruger_Data_Base:
    def __init__(self):
        pass
        self.conn = sqlite3.connect("Usher_DataBase")
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS Ushers("
                       "Usher_ID int,"
                       "First_Name varchar(255),"
                       "Last_Name varchar(255),"
                       "Password varchar(255));")
        #   self.c.execute("INSERT INTO Ushers VALUES (4321, 'abe','kage', '3superman')")
        self.c.execute("SELECT * FROM Ushers")

      #  print("databasechecak")
     #   print(self.c.fetchall())
        self.c.execute("SELECT PassWord FROM Ushers")
    #    print(Check_Usher_password_and_ID(self, "2superman", 1234))
        print(Insert_Usher(self, "Kage", "Dixen", 12345, "123super"))

        #  print(self.c.fetchall())

        self.conn.commit()
        self.conn.close()


def Check_Usher_password_and_ID(self, PassWord, UsherID):
    conn = sqlite3.connect('Usher_DataBase')
    c = conn.cursor()
    P = False
    ID = False
    c.execute("SELECT PassWord FROM Ushers")
    PassWords = c.fetchall()
    for passW in PassWords:
        print(str(passW))
        if str(passW[0]) == PassWord:
            P = True
            print("hey")
            break

    if not P:
        return False
    c.execute("SELECT Usher_ID FROM Ushers")
    Usher_IDs = c.fetchall()
    for U_ID in Usher_IDs:
        print(U_ID[0])
        if U_ID[0] == UsherID:
            ID = True
            break
    if ID and P:
        return True
    else:
        return False


def Insert_Usher(self, FirstName, lastname, UsherId, PassWord):
    print(UsherId)
    print(FirstName)
    print(lastname)
    print(PassWord)
    if not Check_Usher_password_and_ID(self, PassWord, UsherId):
        print("Hej Sa", FirstName)
        with self.conn:
            self.c.execute("INSERT INTO Ushers VALUES (?, ?, ?, ?)", (UsherId, FirstName, lastname, PassWord))
        return True
    else:
        return False


def Add_score_to_data_base(self, score):
    # cheack if Ta

    conn = sqlite3.connect('Score')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS HighScore(Score INTEGER);")
    c.execute("INSERT INTO HighScore VALUES (" + str(score) + ")")

    c.execute("SELECT * FROM HighScore ")
    print(c.fetchall())

    conn.commit()
    conn.close()


def RemoveTable(self, TableName):
    conn = sqlite3.connect('Score')
    c = conn.cursor()

    if self.high_score != 5:
        c.execute("DROP TABLE HighScore;")
        self.high_score = 5
        c.execute("CREATE TABLE IF NOT EXISTS HighScore(Score INTEGER);")
        c.execute("INSERT INTO HighScore VALUES (0)")

    else:
        print(self.high_score)
        print("no table")
    conn.commit()
    conn.close()
