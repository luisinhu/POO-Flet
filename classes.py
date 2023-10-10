import sqlite3



class Usuario:
    def __init__(self,nome,sexo,matricula,senha):

        self.nome = nome
        self.sexo = sexo
        self.matricula = matricula
        self.senha = senha

    def Cadastrar(self, a, b):
        with sqlite3.connect("banco_de_dados.db") as banco:
            cursor = banco.cursor()
            if a == "Aluno":
                cursor.execute("INSERT INTO Aluno VALUES (?, ?, ?, ?, ?)", (
                    self.nome, self.matricula, self.senha, self.sexo, b))
                banco.commit()

            elif a == "Professor":
                cursor.execute("INSERT INTO Professor (nome, matricula, senha, sexo) VALUES (?, ?, ?, ?)",
                            (self.nome, self.matricula, self.senha, self.sexo))
                banco.commit()

    def Login(self):
        with sqlite3.connect("banco_de_dados.db") as banco:
            cursor = banco.cursor()
            cursor.execute(
                "SELECT * FROM Alunos WHERE (matricula == ? AND senha == ?)", (self.matricula, self.senha))
            verificador = cursor.fetchall()
            if len(verificador) > 0:
                print("Login feito com sucesso!")
                return True
            else:
                print("Alguma coisa estava incorreta!")
                return False


class Aluno(Usuario):
    def __init__(self, nome, sexo, matricula, senha, turma):
        super().__init__(nome, sexo, matricula, senha)
        self.turma = turma

    def Cadastrar(self):
        super().Cadastrar("Aluno", self.turma)

    def ExibirAlunos(self):
        print('a')


class Professor(Usuario):
    def __init__(self, nome, sexo, matricula, senha):
        super().__init__(nome, sexo, matricula, senha)

    def Cadastrar(self):
        return super().Cadastrar("Professor", None)
    
    
    def EditarInscricoes(self):
        print("oi")


def Cadastrar(self):
    banco = sqlite3.connect("banco_de_dados.db")
    cursor = banco.cursor()
    cursor.execute("INSERT TO INTO Alunos VALUES(:nome, :sexo, :turma, :matricula, :senha)",{
        'nome': self.nome,
        'sexo': self.sexo,
        'turma': self.turma,
        'matricula': self.matricula,
        'senha': self.senha
    })
    cursor.execute("INSERT TO INTO Professor VALUES(:nome, :sexo, :horario, :matricula, :senha)",{
        'nome': self.nome,
        'sexo': self.sexo,
        'horario': self.horario,
        'matricula': self.matricula,
        'senha': self.senha
    })
    if self.nome == '' or self.sexo == '' or self.turma == '' or self.matricula == None or self.senha == '':
        print("Você esqueceu de preencher alguma informação!")
        return False
    elif self.nome == '' or self.sexo == '' or self.horario == '' or self.matricula == None or self.senha == '':
        print("Você esqueceu de preencher alguma informação!")
        return False
    else:
        banco.commit()
        banco.close
def Login(self):
    banco = sqlite3.connect("banco_de_dados.db")
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM Alunos WHERE(matricula == ? AND senha == ?)",(self.matricula, self.senha),"SELECT * FROM Professor WHERE(matricula == ? AND senha == ?)",(self.matricula, self.senha))
    verificador = cursor.fetchall()
    if len(verificador) > 0 :
        print("Login feito com sucesso!")
        banco.close()
        return True
    else:
        print("Alguma coisa estava incorreto!")
        return False


class Aluno(Usuario):
    def __init__(self, nome, sexo, turma, matricula, senha):
        super().__init__(nome, sexo, matricula, senha)
        self.turma = turma
def ExibirAlunos(self):
    print("Oi")

class Professor(Usuario):
    def __init__(self, nome, sexo, horario, matricula, senha):
        super().__init__(nome, sexo, matricula, senha)
        self.horario = horario
def EditarInscricoes(self):
    print("oi")

