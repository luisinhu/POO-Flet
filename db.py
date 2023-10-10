import sqlite3
banco = sqlite3.connect("banco_de_dados.db")
cursor = banco.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Alunos(nome TEXT, sexo TEXT, turma TEXT, matricula INT PRIMARY KEY, senha TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Professor(nome TEXT, sexo TEXT, matricula INT PRIMARY KEY, senha TEXT)''')
banco.commit()
banco.close()