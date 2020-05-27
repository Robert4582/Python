import sqlite3


class HishScore:

    def __init__(self):
        self.high_score = []
        self.testlist = [1, 3, 5, 2, 5]

        conn = sqlite3.connect('Score')

        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS HighScore(Score INTEGER);")
        c.execute("INSERT INTO HighScore VALUES (41)")
        # c.execute("INSERT INTO HighScore VALUES 2100")
        # c.execute("INSERT INTO HighScore VALUES 5100")
        # c.execute("INSERT INTO HighScore VALUES 1500")
        c.execute("SELECT * FROM HighScore ")
        print("databasechecak")
        print(c.fetchall())
        conn.commit()
        conn.close()

    def get_HighScore(self):
        conn = sqlite3.connect('Score')
        c = conn.cursor()

        c.execute("SELECT * FROM HighScore ")
        print(c.fetchall())
        self.Update_high_score()
        print(self.high_score)
        A = str(self.high_score[0])
        a = A.split("(")
        b = a[1]
        c = b.split(",")
        H = c[0]
        print("Getting new Score")
        print(H)
        return H

    def get_HighScore_list(self):
        conn = sqlite3.connect('Score')
        c = conn.cursor()

        c.execute("SELECT * FROM HighScore ")
        print(c.fetchall())
        self.Update_high_score()

        return self.high_score
    def Update_high_score(self):

        self.high_score = []

        conn = sqlite3.connect('score')
        c = conn.cursor()

        c.execute("SELECT * FROM HighScore ")

        self.high_score = c.fetchall()
        self.high_score.sort()
        self.high_score.reverse()

        conn.close()

    #  for score in self.high_score:
    #      print(score)

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

    def RemoveTable(self):
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
