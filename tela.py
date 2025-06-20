# Importando dependências do Tkinter
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# Importando Pillow
from PIL import ImageTk, Image

# Tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# Importando main
from main import *

# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = '#b6b3b3'  # + gray
co3 = "#e5e5e5"  # gray
co4 = "#00a095"  # Verde
co5 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#146C94"   # azul
co9 = "#263238"   # + verde
co10 = "#e9edf5"   # + verde

# ------------------------------------------------Criando janela---------------------------------------------------------------------------------
janela = Tk()
janela.title("Sistema de Registro de Alunos")
janela.geometry('910x535')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

estilo = Style(janela)
estilo.theme_use("clam")

# Criando Frames
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0,column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(janela, width=100, height=200, bg=co1, relief="raised")
frame_botoes.grid(row=1,column=0, pady=1, padx=0, sticky=NSEW)

frame_detalhes = Frame(janela, width=800, height=100, bg=co1, relief="solid" )
frame_detalhes.grid(row=1,column=1, pady=1, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=800, height=100, bg=co1, relief="solid")
frame_tabela.grid(row=3,column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)

# Trabalhando frame logo
global imagem, imagem_string, l_imagem

app_lg = Image.open('logar.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="  UnEB - Universidade Estadual da Bahia", width=850, compound=LEFT, anchor=NW, font='Verdana 15', bg=co6, fg=co1)
app_logo.place(x=5, y=0)

# ---------------------------------------------Abrindo a Imagem-------------------------------------------------------------------------------------
imagem = Image.open('vetor.jpg')
imagem = imagem.resize((125,140))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_detalhes, image=imagem, bg=co0, fg=co4)
l_imagem.place(x=500, y=7)

# Função para escolher imagem
def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((125,140))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_detalhes, image=imagem, bg=co0, fg=co4)
    l_imagem.place(x=500, y=7)

    botao_carregar['text'] = 'Trocar de Foto'

botao_carregar = Button(frame_detalhes, command=escolher_imagem, text='Carregar Foto'.upper(), width=20, compound=CENTER, overrelief=RIDGE, font='Ivy 7 bold', bg=co3, fg=co0 )
botao_carregar.place(x=500, y=160)

# ------------------------------------------Criando os campos de entrada ---------------------------------------------------------------------------
l_nome = Label(frame_detalhes, text="Nome *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_nome.place(x=7, y=10)
e_nome = Entry(frame_detalhes, width=30, justify='left', relief="solid")
e_nome.place(x=7, y=40)

l_email = Label(frame_detalhes, text="E-mail *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_email.place(x=7, y=70)
e_email = Entry(frame_detalhes, width=30, justify='left', relief="solid")
e_email.place(x=7, y=100)

l_tel = Label(frame_detalhes, text="Telefone *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_tel.place(x=7, y=130)
e_tel = Entry(frame_detalhes, width=15, justify='left', relief="solid")
e_tel.place(x=7, y=160)

l_sexo = Label(frame_detalhes, text="Genêro *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_sexo.place(x=190, y=130)
e_sexo = ttk.Combobox(frame_detalhes, width=7, font='Ivy 8 bold',justify='center')
e_sexo['values'] = ('M', 'F')
e_sexo.place(x=190, y=160)

l_data_nascimento = Label(frame_detalhes, text="Data de Nascimento *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_data_nascimento.place(x=270, y=10)
e_data_nascimento = DateEntry(frame_detalhes, width=10, justify='center', background='dark blue', boderwidth=2, year=2025)
e_data_nascimento.place(x=270, y=40)

cursos = [
    'Medicina', 'Enfermagem', 'Odontologia', 'Fisioterapia', 'Fonoaudiologia', 'Nutrição', 'Pedagogia', 'Educação Física',
    'Administração', 'Ciências Contábeis', 'Econômia', 'Marketing', 'Ciência da Computação', 'Engenharia de Produção',
    'Engenharia de Software', 'Engenharia Civil', 'Agronomia', 'Zootecnia', 'Veterinária', 'Direito', 'Jornalismo'
    ]
l_cursos = Label(frame_detalhes, text="Curso *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_cursos.place(x=270, y=70)
e_cursos = ttk.Combobox(frame_detalhes, width=25, font='Ivy 8 bold', justify='center')
e_cursos['values'] = cursos
e_cursos.place(x=270, y=100)

l_endereco = Label(frame_detalhes, text="Endereço *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_endereco.place(x=270, y=130)
e_endereco = Entry(frame_detalhes, width=25, justify='left', relief="solid")
e_endereco.place(x=270, y=160)

# -------------------------------------------Tabela de Aluno----------------------------------------------------------------------------------------
def mostrar_alunos():
    # Criando uma visualização em arvore com barras de rolagem duplas
    lista_cabecalho = ['Id', 'Nome', 'Email', 'Telefone', 'Sexo', 'Data', 'Endereço', 'Curso']

    # Ver todos Aluno
    def_lista = sistema_de_registro.visualizar_estudantes()

    tree_aluno = ttk.Treeview(frame_tabela, selectmode='extended', columns=lista_cabecalho, show='headings')

    # Barra de rolagem vertical
    vsb = ttk.Scrollbar(frame_tabela, orient='vertical', command=tree_aluno.yview)

    # Barra de rolagem horizontal
    hsb = ttk.Scrollbar(frame_tabela, orient='horizontal', command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela.grid_rowconfigure(0, weight=12)

    for col in lista_cabecalho:
        tree_aluno.heading(col, text=col.title(), anchor=NW)

        # Ajuste das colunas
        # tree_aluno.column(col, width=96, anchor='center')
        tree_aluno.column('Id', width=30, anchor='center')
        tree_aluno.column('Nome', width=150, anchor='center')
        tree_aluno.column('Email', width=150, anchor='center')
        tree_aluno.column('Telefone', width=100, anchor='center')
        tree_aluno.column('Sexo', width=42, anchor='center')
        tree_aluno.column('Data', width=100, anchor='center')
        tree_aluno.column('Endereço', width=150, anchor='center')
        tree_aluno.column('Curso', width=150, anchor='center')

    for item in def_lista:
        tree_aluno.insert('', 'end', values=item)

# ----------------------------------------------Criando funções CRUD-----------------------------------------------------------------------------
def adicionar():
    global imagem, imagem_string, l_imagem

    # Obtendo os valores
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    sexo = e_sexo.get()
    data_nascimento = e_data_nascimento.get()
    endereco = e_endereco.get()
    curso = e_cursos.get()
    imagem = imagem_string

    lista = [nome, email, tel, sexo, data_nascimento, endereco, curso, imagem]

    # Verificando se a lista contém valor vazio
    for i in lista:
        if i == " ":
            messagebox.showerror('Error: Preencha todos os campos!')
            return

    # Registrando os valores
    sistema_de_registro.registrar_estudantes(lista)

    # Limpando os campos de entrada
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    e_sexo.delete(0, END)
    e_data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    e_cursos.delete(0, END)

    # Abrindo a imagem
    imagem = Image.open('vetor.jpg')
    imagem = imagem.resize((125, 140))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_detalhes, image=imagem, bg=co0, fg=co4)
    l_imagem.place(x=500, y=7)

    # Mostrando os valores na tabela
    mostrar_alunos()

def procurar():
    global imagem, imagem_string, l_imagem

    # Obtendo id
    id_aluno = e_procurar.get()

    # Procurando aluno
    dados = sistema_de_registro.procurar_estudantes(id_aluno)

    # Limpando os campos de entrada
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    e_sexo.delete(0, END)
    e_data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    e_cursos.delete(0, END)

    # Inserir os valores nos campos de entrada
    e_nome.insert(END, dados[1])
    e_email.insert(END, dados[2])
    e_tel.insert(END, dados[3])
    e_sexo.insert(END, dados[4])
    e_data_nascimento.insert(END, dados[5])
    e_endereco.insert(END, dados[6])
    e_cursos.insert(END, dados[7])

    imagem = dados[8]
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((125, 140))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_detalhes, image=imagem, bg=co0, fg=co4)
    l_imagem.place(x=500, y=7)
    
def atualizar():
    global imagem, imagem_string, l_imagem

    id_aluno = e_procurar.get()

    # Obtendo os valores
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    sexo = e_sexo.get()
    data_nascimento = e_data_nascimento.get()
    endereco = e_endereco.get()
    curso = e_cursos.get()
    imagem = imagem_string

    lista = [nome, email, tel, sexo, data_nascimento, endereco, curso, imagem, id_aluno]

    # Verificando se a lista contém valor vazio
    for i in lista:
        if i == " ":
            messagebox.showerror('Error: Preencha todos os campos!')
            return

    # Registrando os valores
    sistema_de_registro.atualizar_estudantes(lista)

    # Limpando os campos de entrada
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    e_sexo.delete(0, END)
    e_data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    e_cursos.delete(0, END)

    # Abrindo a imagem
    imagem = Image.open('vetor.jpg')
    imagem = imagem.resize((125, 140))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_detalhes, image=imagem, bg=co0, fg=co4)
    l_imagem.place(x=500, y=7)

    # Mostrando os valores na tabela
    mostrar_alunos()

def deletar():
    global imagem, imagem_string, l_imagem

    id_aluno = int(e_procurar.get())

    # Deletando aluno
    sistema_de_registro.deletar_estudantes(id_aluno)

    # Limpando os campos de entrada
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    e_sexo.delete(0, END)
    e_data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    e_cursos.delete(0, END)

    e_procurar.delete(0, END)

    # Abrindo a imagem
    imagem = Image.open('vetor.jpg')
    imagem = imagem.resize((125, 140))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_detalhes, image=imagem, bg=co0, fg=co4)
    l_imagem.place(x=500, y=7)

    # Mostrando os valores na tabela
    mostrar_alunos()

# ---------------------------------------------------Procurar aluno-----------------------------------------------------------------------------
frame_procurar_aluno = Frame(frame_botoes, width=40, height=55, bg=co1, relief=RAISED)
frame_procurar_aluno.grid(row=0,column=0, pady=0, padx=10, sticky=NSEW)

l_nome = Label(frame_procurar_aluno, text="Procurar aluno [Entra ID] *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_nome.grid(row=0,column=0, pady=10, padx=0, sticky=NSEW)
e_procurar = Entry(frame_procurar_aluno, width=5, justify='center', relief="solid", font='Ivy 10')
e_procurar.grid(row=1,column=0, pady=10, padx=0, sticky=NSEW)

botao_procurar = Button(frame_procurar_aluno, command=procurar, text='Procurar', width=6, anchor=CENTER, overrelief=RIDGE, font='Ivy 7 bold', bg=co3, fg=co0 )
botao_procurar.grid(row=1,column=1, pady=10, padx=4, sticky=NSEW)

# Botões
botao_adicionar = Image.open('add.png')
botao_adicionar = botao_adicionar.resize((25,25))
botao_adicionar = ImageTk.PhotoImage(botao_adicionar)
app_adicionar = Button(frame_botoes, command=adicionar, image=botao_adicionar, relief=GROOVE, text=' Adicionar', width=100, compound=LEFT, overrelief=RIDGE, font='Ivy 11', bg=co3, fg=co0)
app_adicionar.grid(row=1,column=0, pady=2, padx=12, sticky=NSEW)

botao_atualizar = Image.open('atualizar.png')
botao_atualizar = botao_atualizar.resize((25,25))
botao_atualizar = ImageTk.PhotoImage(botao_atualizar)
app_atualizar = Button(frame_botoes, command=atualizar, image=botao_atualizar, relief=GROOVE, text=' Atualizar', width=100, compound=LEFT, overrelief=RIDGE, font='Ivy 11', bg=co3, fg=co0)
app_atualizar.grid(row=2,column=0, pady=2, padx=12, sticky=NSEW)

botao_deletar = Image.open('delete.png')
botao_deletar = botao_deletar.resize((25,25))
botao_deletar = ImageTk.PhotoImage(botao_deletar)
app_deletar = Button(frame_botoes, command=deletar, image=botao_deletar, relief=GROOVE, text=' Deletar', width=100, compound=LEFT, overrelief=RIDGE, font='Ivy 11', bg=co3, fg=co0)
app_deletar.grid(row=3,column=0, pady=2, padx=12, sticky=NSEW)

# Barra de divisão
barra_divisao = Label(frame_botoes, relief=GROOVE, text='h', width=1, height=72, anchor=NW, font='Ivy 1', bg=co6, fg=co0)
barra_divisao.place(x=252, y=1)


# Chamar a tabela
mostrar_alunos()

janela.mainloop()



