from aluno_model import Aluno
import pymysql.cursors
class Alunodata():
    def __init__(self):
        self.conexao = pymysql.connect(host='localhost',
                                       user='root',
                                       password='',
                                       database='escola',
                                       cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conexao.cursor()
    def insert(self, aluno: Aluno):
        try:
            sql = 'INSERT INTO alunos ' \
                   'VALUES (%s, %s, %s, %s, %s)'
            self.cursor.execute(sql, (aluno.matricula,
                                      aluno.nome,
                                      aluno.idade,
                                      aluno.curso,
                                      aluno.nota))
            self.conexao.commit()
        except Exception as error:
            print(f'Erro ao inserir! erro: {error}')

    def update(self, aluno: Aluno):
        try:
            sql = 'UPDATE alunos SET nome = %s, idade = %s, curso =%s, ' \
                  'nota = %s WHERE matricula = %s'
            self.cursor.execute(sql, (aluno.nome,
                                      aluno.idade,
                                      aluno.curso,
                                      aluno.nota,
                                      aluno.matricula))
            self.conexao.commit()
        except Exception as error:
            print(f'Erro ao atualizar! erro: {error}')

    def select(self):
        try:
            sql = 'SELECT * FROM alunos'
            self.cursor.execute(sql)
            alunos = self.cursor.fetchall()
            return alunos
        except Exception as error:
            print(f'Erro ao listar! erro: {error}')

    def delete(self, matricula: str):
        try:
            sql = 'DELETE FROM alunos WHERE matricula = %s'
            self.cursor.execute(sql, matricula)
            self.conexao.commit()
        except Exception as error:
            print(f'Erro ao deletar! erro: {error}')




if __name__ == '__main__':
    a = Alunodata()
    a.delete('b9aed05b-ff05-4010-b1ab-fe6c8f9b76dc')
    print(a.select())