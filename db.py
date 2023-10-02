import sqlite3 as sql

banco = sql.connect("teste.db", check_same_thread= False)

cursor = banco.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Alunos(
    matricula INT PRIMARY KEY NOT NULL,
    senha TEXT NOT NULL
)
""")