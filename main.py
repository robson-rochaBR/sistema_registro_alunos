import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('estudante.db')
        self.c = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS estudantes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL,
                            telefone TEXT NOT NULL,
                            sexo TEXT NOT NULL,
                            data_nascimento TEXT NOT NULL,
                            endereco TEXT NOT NULL,
                            curso TEXT NOT NULL,
                            imagem TEXT NOT NULL)''')

    def registrar_estudantes(self, estudantes):
        self.c.execute("INSERT INTO estudantes(nome, email, telefone, sexo, data_nascimento, endereco, curso, imagem) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       estudantes)
        self.conn.commit()

        # mostrando mensagem de sucesso.
        messagebox.showinfo("Parabêns", "Registro realizado com sucesso!")

    def visualizar_estudantes(self):
        self.c.execute("SELECT * FROM estudantes")
        dados = self.c.fetchall()

        return dados
            
    def procurar_estudantes(self, id):
        self.c.execute("SELECT * FROM estudantes WHERE id=?", (id,))
        dados = self.c.fetchone()

        return dados

    def atualizar_estudantes(self, novos_valores):
        self.c.execute('''UPDATE estudantes SET nome=?, email=?, telefone=?, sexo=?, data_nascimento=?, endereco=?, curso=?, imagem=? WHERE id=?''',
                       (novos_valores[0], novos_valores[1], novos_valores[2], novos_valores[3], novos_valores[4], novos_valores[5], novos_valores[6], novos_valores[7], novos_valores[8]))
        self.conn.commit()

        # mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', f'Estudante com Id: {novos_valores[8]} foi atualizado!')

    def deletar_estudantes(self, id):
        self.c.execute("DELETE FROM estudantes WHERE id=?", (id,))
        self.conn.commit()

        # mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', f'Estudante com Id: {id} foi deletado!') 

# Criando instância do sistema de registro
sistema_de_registro = SistemaDeRegistro()

# Registrar estudantes
# estudante = ('Robson', 'rrocha@gmail.com', '729874', 'M', '07/0/1987', 'Bahia, Brasil', 'Analista', 'imagem.png')
# sistema_de_registro.registrar_estudantes(estudante)

# Visualizar estudantes
# sistema_de_registro.visualizar_estudantes()

# Procurar estudantes
# sistema_de_registro.procurar_estudantes()

# Atualizar estudante
# novo_valor = ('Elena', 'elena@gmail.com', '444', 'F', '01/05/2007', 'Angola, Luanda', 'Jornalista', 'imagem2.png', 1)
# sistema_de_registro.atualizar_estudantes(novo_valor)

# Deletar estudante
# sistema_de_registro.deletar_estudantes()
