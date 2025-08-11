# Importando dependências do Tkinter
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import datetime
import os

# Importando Pillow
from PIL import ImageTk, Image

# Tk calendar
from tkcalendar import DateEntry

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


# Inserindo informações de data no título
data_atual = datetime.datetime.now()
data_formatada = data_atual.strftime("%d de %B de %Y")

janela = Tk()
janela.title(f"Data: {data_formatada}       |       Sistema de Registro de Alunos")
janela.geometry('1310x720')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)
janela.grid_rowconfigure(3, weight=1)
janela.grid_columnconfigure(0, weight=1)

estilo = Style(janela)
estilo.theme_use("clam")

# Criando Frames
frame_logo = Frame(janela, width=800, height=52, bg=co6)
frame_logo.grid(row=0,column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(janela, width=100, height=200, bg=co1, relief="raised")
frame_botoes.grid(row=1,column=0, pady=1, padx=0, sticky=NSEW)

frame_detalhes = Frame(janela, width=800, height=100, bg=co1, relief="solid" )
frame_detalhes.grid(row=1,column=1, pady=1, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=800, height=100, bg=co1, relief="solid")
frame_tabela.grid(row=3,column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)

frame_rodape = Frame(janela, height=20, bg=co6, relief='solid')
frame_rodape.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

# Trabalhando frame logo
global imagem, imagem_string, l_imagem

app_lg = Image.open('logar.png')
app_lg = app_lg.resize((60,60))
app_lg = ImageTk.PhotoImage(app_lg)

texto_label = f"  UnEB - Universidade Estadual da Bahia"
app_logo = Label(frame_logo, image=app_lg, text=texto_label, width=850, compound=LEFT, anchor=NW, font='Verdana 15', bg=co6, fg=co1)
app_logo.place(x=5, y=0)


# ---------------------------------------------Abrindo a Imagem-------------------------------------------------------------------------------------
imagem = Image.open('vetor.jpg')
imagem = imagem.resize((145,170))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_botoes, image=imagem, bg=co0, fg=co4, bd=2)
l_imagem.place(x=330, y=6)

# Função para escolher imagem
def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((145,170))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_botoes, image=imagem, bg=co0, fg=co4)
    l_imagem.place(x=330, y=7)

    botao_carregar['text'] = 'Trocar de Foto'

botao_carregar = Button(frame_botoes, command=escolher_imagem, text='Carregar Foto'.upper(), width=20, compound=CENTER,
                        overrelief=RIDGE, font='Ivy 8 bold', bg=co8, fg=co1, bd=2)
botao_carregar.place(x=330, y=190)

# ------------------------------------------Criando os campos de entrada ---------------------------------------------------------------------------
# Campo nome
l_nome = Label(frame_detalhes, text="Aluno *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_nome.place(x=0, y=5)
e_nome = Entry(frame_detalhes, width=30, justify='left', relief="solid")
e_nome.place(x=0, y=30)

# Campo documento
def formatar_cpf(cpf_str):
    """
        Formata uma ‘string’ de CPF (apenas dígitos) para o formato XXX.XXX.XXX-XX.
        Remove caracteres não numéricos antes de formatar.
        """
    numeros_cpf = ''.join(filter(str.isdigit, cpf_str))

    if len(numeros_cpf) <= 3:
        return numeros_cpf
    elif len(numeros_cpf) <= 6:
        return f"{numeros_cpf[0:3]}.{numeros_cpf[3:6]}"
    elif len(numeros_cpf) <= 9:
        return f"{numeros_cpf[0:3]}.{numeros_cpf[3:6]}.{numeros_cpf[6:9]}"
    elif len(numeros_cpf) <= 11:
        return f"{numeros_cpf[0:3]}.{numeros_cpf[3:6]}.{numeros_cpf[6:9]}-{numeros_cpf[9:11]}"
    else:
        # Se tiver mais de 11 dígitos, trunca para 11 e formata
        return f"{numeros_cpf[0:3]}.{numeros_cpf[3:6]}.{numeros_cpf[6:9]}-{numeros_cpf[9:11]}"

# --- Função de callback para o evento KeyRelease ---
def formatar_entry_cpf(event):
    """
        Formata o conteúdo da entrada de CPF quando uma tecla é liberada.
        """
    cpf_str = e_documento.get()
    cpf_formatado = formatar_cpf(cpf_str)
    e_documento.delete(0, END)  # Limpa a entrada
    e_documento.insert(0, cpf_formatado)  # Insere o CPF formatado
    e_documento.icursor(END)  # Move o cursor para o final da entrada

l_documento = Label(frame_detalhes, text="CPF *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_documento.place(x=0, y=60)
e_documento = Entry(frame_detalhes, width=13, justify='left', relief="solid")
e_documento.place(x=0, y=85)
e_documento.bind('<KeyRelease>', formatar_entry_cpf)

# Campo genero
l_sexo = Label(frame_detalhes, text="Genêro *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_sexo.place(x=220, y=60)
e_sexo = Combobox(frame_detalhes, width=7, font='Ivy 8 bold',justify='center')
e_sexo['values'] = ('M', 'F')
e_sexo.place(x=220, y=85)

# Campo nascimento
l_data_nascimento = Label(frame_detalhes, text="Data de Nasc. *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_data_nascimento.place(x=380, y=5)
e_data_nascimento = DateEntry(frame_detalhes, width=10, justify='center', background='#1A2B3C', boderwidth=2, year=2025)
e_data_nascimento.place(x=380, y=30)

# Campo telefone
def formatar_telefone(tel_str):
    """
        Formata uma string de telefone (apenas dígitos) para o formato (xx) x xxxx-xxxx.
        Remove caracteres não numéricos antes de formatar.
        """
    # Remove tudo que não for dígito da ‘string’
    numeros_tel = ''.join(filter(str.isdigit, tel_str))

    # Formatação progressiva
    if len(numeros_tel) <= 2:
        return f"({numeros_tel}"
    elif len(numeros_tel) <= 3: # Para o caso de já ter (xx) e o primeiro dígito
        return f"({numeros_tel[0:2]}) {numeros_tel[2]}"
    elif len(numeros_tel) <= 7: # Para o caso de ter 9 dígitos (celular) ou 8 (fixo)
        # Verifica se é um 9 antes do 4º dígito para telefones celulares (ex: (xx) 9xxxx-xxxx)
        if len(numeros_tel) == 7 and numeros_tel[2] == '9':
            return f"({numeros_tel[0:2]}) {numeros_tel[2]} {numeros_tel[3:7]}"
        else: # Fixo ou ainda não chegou no 9º dígito do celular
            return f"({numeros_tel[0:2]}) {numeros_tel[2:7]}"
    elif len(numeros_tel) <= 11:
        # Se for celular com 9 dígitos (ex: 9xxxx-xxxx)
        if len(numeros_tel) == 11 and numeros_tel[2] == '9':
            return f"({numeros_tel[0:2]}) {numeros_tel[2]} {numeros_tel[3:7]}-{numeros_tel[7:11]}"
        # Se for fixo ou um celular antigo sem o 9º dígito (ex: xxxx-xxxx)
        elif len(numeros_tel) == 10:
            return f"({numeros_tel[0:2]}) {numeros_tel[2:6]}-{numeros_tel[6:10]}"
        else: # Caso geral para 10 ou 11 dígitos, formatando conforme padrão
            return f"({numeros_tel[0:2]}) {numeros_tel[2]} {numeros_tel[3:7]}-{numeros_tel[7:11]}"
    else:
        # Se tiver mais de 11 dígitos, trunca para 11 e formata
        return f"({numeros_tel[0:2]}) {numeros_tel[2]} {numeros_tel[3:7]}-{numeros_tel[7:11]}"

# --- Função de callback para o evento KeyRelease ---
def formatar_entry_tel(event):
    current_text = e_tel.get()

    if event.keysym == 'BackSpace' or event.keysym == 'Delete':
        # Permite que o BackSpace/Delete funcione normalmente sem reformatação
        # Mas vamos garantir que o cursor esteja no final se for BackSpace para remover formatacao
        if event.keysym == 'BackSpace':
            # Remove a formatação antes de aplicar o BackSpace virtualmente
            numeros_tel = ''.join(filter(str.isdigit, current_text))
            if current_text and current_text[-1] in '()- ': # Se o último caractere for formatacao
                # Se for um caractere de formatação sendo apagado, remove o último número também.
                # Isso impede que o cursor "salte"
                e_tel.delete(0, END)
                e_tel.insert(0, formatar_telefone(numeros_tel[:-1]))
                e_tel.icursor(END)
                return
        return

    formatted_text = formatar_telefone(current_text)

    if current_text != formatted_text:
        e_tel.delete(0, END)
        e_tel.insert(0, formatted_text)
        e_tel.icursor(END)

l_tel = Label(frame_detalhes, text="Telefone *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_tel.place(x=0, y=165)
e_tel = Entry(frame_detalhes, width=15, justify='left', relief="solid")
e_tel.place(x=0, y=190)
e_tel.bind('<KeyRelease>', formatar_entry_tel)

# Campo email
l_email = Label(frame_detalhes, text="E-mail *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_email.place(x=0, y=110)
e_email = Entry(frame_detalhes, width=30, justify='left', relief="solid")
e_email.place(x=0, y=135)

# Campo cidade
l_cidade = Label(frame_detalhes, text="Cidade *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_cidade.place(x=190, y=165)
e_cidade = Entry(frame_detalhes, width=15, justify='left', relief="solid")
e_cidade.place(x=190, y=190)

# Campo estado
estados = [
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ',
    'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
]
l_estado = Label(frame_detalhes, text="Estado *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_estado.place(x=360, y=165)
e_estado = Combobox(frame_detalhes, width=5, font='Ivy 8 bold', justify='center')
e_estado['values'] = estados
e_estado.place(x=360, y=190)

# Campo nacionalidade
paises = [
    'Afeganistão','África do Sul','Albânia','Alemanha','Andorra','Angola','Antígua e Barbuda','Arábia Saudita',
    'Argentina','Armênia','Austrália','Áustria','Azerbaijão','Bahamas','Bahrein','Bangladesh','Barbados',
    'Belarus','Bélgica','Belize','Benin','Butão','Bolívia','Bósnia e Herzegovina','Botsuana','Brasil','Brunei Darussalam',
    'Bulgária','Burquina Faso','Burundi','Cabo Verde','Camboja','Camarões','Canadá','Catar','Cazaquistão','Chade','Chile',
    'China','Chipre','Colômbia','Comores','Congo','Coreia do Norte','Coreia do Sul','Costa do Marfim','Costa Rica','Croácia',
    'Cuba','Dinamarca','Djibuti','Egito','El Salvador','Emirados Árabes Unidos','Equador','Eritreia','Eslováquia','Eslovênia',
    'Espanha','Estados Unidos','Estônia','Eswatini','Etiópia','Fiji','Filipinas','Finlândia','França','Gabão','Gâmbia','Gana',
    'Geórgia','Granada','Grécia','Guatemala','Guiana','Guiné','Guiné Equatorial','Guiné-Bissau','Haiti','Honduras','Hungria',
    'Iêmen','Ilhas Marshall','Ilhas Salomão','Índia','Indonésia','Irã','Iraque','Irlanda','Islândia','Israel','Itália','Jamaica',
    'Japão','Jordânia','Kiribati','Kuwait','Laos','Lesoto','Letônia','Líbano','Libéria','Líbia','Liechtenstein','Lituânia','Luxemburgo',
    'Macedônia do Norte','Madagascar','Malauí','Malásia','Maldivas','Mali','Malta','Marrocos','Maurício','Mauritânia','México',
    'Micronésia','Mônaco','Mongólia','Montenegro','Moçambique','Mianmar','Namíbia','Nauru','Nepal','Nicarágua','Níger','Nigéria',
    'Noruega','Nova Zelândia','Omã','Países Baixos','Paquistão','Palau','Panamá','Papua Nova Guiné','Paraguai','Peru','Polônia',
    'Portugal','Quênia','Quirguistão','Reino Unido','República Centro-Africana','República Democrática do Congo','República Dominicana',
    'República Tcheca','Romênia','Ruanda','Rússia','Samoa','San Marino','Santa Lúcia','São Cristóvão e Nevis','São Tomé e Príncipe',
    'São Vicente e Granadinas','Seicheles','Senegal','Serra Leoa','Sérvia','Singapura','Síria','Somália','Sri Lanka','Sudão',
    'Sudão do Sul','Suécia','Suíça','Suriname','Tailândia','Tajiquistão','Tanzânia','Timor-Leste','Togo','Tonga','Trinidad e Tobago',
    'Tunísia','Turcomenistão','Turquia','Tuvalu','Ucrânia','Uganda','Uruguai','Uzbequistão','Vanuatu','Venezuela','Vietnã',
    'Zâmbia','Zimbábue'
]
l_nacionalidade = Label(frame_detalhes, text="Nacionalidade *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_nacionalidade.place(x=400, y=60)
e_nacionalidade = Combobox(frame_detalhes, width=28, font='Ivy 9 bold', justify='left')
e_nacionalidade['values'] = paises
e_nacionalidade.place(x=400, y=85)

# Campo deficiencia
l_deficiencia = Label(frame_detalhes, text="Deficiência *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_deficiencia.place(x=320, y=110)
e_deficiencia = Combobox(frame_detalhes, width=7, font='Ivy 8 bold',justify='center')
e_deficiencia['values'] = ('SIM', 'NÃO')
e_deficiencia.place(x=320, y=135)

# Campo descrição
l_descricao = Label(frame_detalhes, text="Informações *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_descricao.place(x=470, y=110)
e_descricao = Text(frame_detalhes, width=40, height=4, font='Ivy 10', relief="sunken")
e_descricao.place(x=470, y=135)

# Campo curso
cursos = [
    'Medicina', 'Enfermagem', 'Odontologia', 'Fisioterapia', 'Fonoaudiologia', 'Nutrição', 'Pedagogia', 'Educação Física',
    'Administração', 'Ciências Contábeis', 'Econômia', 'Marketing', 'Ciência da Computação', 'Engenharia de Produção',
    'Engenharia de Software', 'Engenharia Civil', 'Agronomia', 'Zootecnia', 'Veterinária', 'Direito', 'Jornalismo'
    ]
l_cursos = Label(frame_detalhes, text="Curso *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_cursos.place(x=610, y=5)
e_cursos = Combobox(frame_detalhes, width=25, font='Ivy 8 bold', justify='center')
e_cursos['values'] = cursos
e_cursos.place(x=610, y=30)

# Campo turma
l_turma = Label(frame_detalhes, text="Turma *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_turma.place(x=715, y=60)
e_turma = Entry(frame_detalhes, width=8, justify='left', relief="solid")
e_turma.place(x=715, y=85)



# -------------------------------------------Tabela de Aluno----------------------------------------------------------------------------------------
def mostrar_alunos():
    # Criando uma visualização em árvore com barras de rolagem duplas
    lista_cabecalho = ['Id', 'Nome', 'CPF', 'Genêro', 'Nascimento', 'Telefone', 'Email', 'Cidade', 'Estado', 'Nacionalidade', 'Deficiência', 'Informações', 'Curso', 'Turma']

    # Ver todos Aluno
    def_lista = sistema_de_registro.visualizar_estudante()

    tree_aluno = ttk.Treeview(frame_tabela, selectmode='extended', columns=lista_cabecalho, show='headings')

    # Barra de rolagem vertical
    vsb = ttk.Scrollbar(frame_tabela, orient='vertical', command=tree_aluno.yview)

    # Barra de rolagem horizontal
    hsb = ttk.Scrollbar(frame_tabela, orient='horizontal', command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela.grid_rowconfigure(1, weight=1)
    frame_tabela.grid_columnconfigure(0, weight=1)

    for col in lista_cabecalho:
        tree_aluno.heading(col, text=col.title(), anchor=NW)

        # Ajuste das colunas
        # tree_aluno.column(col, width=96, anchor='center')
        tree_aluno.column('Id', width=40)
        tree_aluno.column('Nome', width=150)
        tree_aluno.column('CPF', width=120)
        tree_aluno.column('Genêro', width=59)
        tree_aluno.column('Nascimento', width=91)
        tree_aluno.column('Telefone', width=120)
        tree_aluno.column('Email', width=150)
        tree_aluno.column('Cidade', width=80)
        tree_aluno.column('Estado', width=55)
        tree_aluno.column('Nacionalidade', width=105)
        tree_aluno.column('Deficiência', width=85)
        tree_aluno.column('Informações', width=150)
        tree_aluno.column('Curso', width=160)
        tree_aluno.column('Turma', width=53)

    for item in def_lista:
        tree_aluno.insert('', 'end', values=item)
        
# Função para preencher os campos ao clicar em uma linha da tabela
def on_tree_select(event, tree_aluno=None):
    global imagem, imagem_string, l_imagem

    # Limpar todos os campos primeiro
    limpar_campos()

    try:
        item = tree_aluno.focus() # Obtém o item selecionado
        dados = tree_aluno.item(item, 'values') # Obtém os valores do item

        # Inserir os valores nos campos de entrada (ajustar índices conforme sua lista_cabecalho)
        # Atenção: 'Id' é o primeiro item agora (índice 0)
        e_procurar.insert(0, dados[0]) # ID para o campo de procurar

        e_nome.insert(0, dados[1])
        e_documento.insert(0, dados[2])
        e_sexo.set(dados[3]) # Use .set() para Combobox
        e_data_nascimento.set_date(dados[4]) # Use .set_date() para DateEntry
        e_tel.insert(0, dados[5])
        e_email.insert(0, dados[6])
        e_cidade.insert(0, dados[7])
        e_estado.set(dados[8])
        e_nacionalidade.set(dados[9])
        e_deficiencia.set(dados[10])
        e_descricao.insert("1.0", dados[11]) # Usar "1.0" para Text widget
        e_cursos.set(dados[12])
        e_turma.insert(0, dados[13])

        caminho_imagem = dados[14] # O caminho da imagem agora é o 15º elemento (índice 14)
        if caminho_imagem and os.path.exists(caminho_imagem): # Verifica se o caminho existe
            imagem_string = caminho_imagem
            imagem_temp = Image.open(caminho_imagem)
            imagem_temp = imagem_temp.resize((145, 170))
            imagem = ImageTk.PhotoImage(imagem_temp)
            l_imagem.config(image=imagem)
            botao_carregar['text'] = 'Trocar de Foto'
        else:
            # Se a imagem não for encontrada, volta para a imagem padrão
            imagem_string = 'vetor.jpg' # Caminho padrão
            imagem_temp = Image.open('vetor.jpg')
            imagem_temp = imagem_temp.resize((145, 170))
            imagem = ImageTk.PhotoImage(imagem_temp)
            l_imagem.config(image=imagem)
            botao_carregar['text'] = 'Carregar Foto'

    except IndexError:
        messagebox.showwarning('Aviso', 'Nenhum aluno selecionado ou dados incompletos.')
    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro ao carregar dados: {e}')


# Função para limpar todos os campos
def limpar_campos():
    e_nome.delete(0, END)
    e_documento.delete(0, END)
    e_sexo.set('') # Limpa Combobox
    e_data_nascimento.set_date(datetime.date.today()) # Reseta DateEntry para data atual
    e_tel.delete(0, END)
    e_email.delete(0, END)
    e_cidade.delete(0, END)
    e_estado.set('') # Limpa Combobox
    e_nacionalidade.set('') # Limpa Combobox
    e_deficiencia.set('') # Limpa Combobox
    e_descricao.delete("1.0", "end") # CORRIGIDO PARA TEXT WIDGET
    e_cursos.set('') # Limpa Combobox
    e_turma.delete(0, END)
    e_procurar.delete(0, END) # Limpa campo de procurar também

    # Reseta para a imagem padrão
    global imagem, imagem_string, l_imagem
    imagem_string = 'vetor.jpg' # Define o caminho da string para o padrão
    imagem_temp = Image.open('vetor.jpg')
    imagem_temp = imagem_temp.resize((145, 170))
    imagem = ImageTk.PhotoImage(imagem_temp)
    l_imagem.config(image=imagem)
    botao_carregar['text'] = 'Carregar Foto'

# ----------------------------------------------Criando funções CRUD-----------------------------------------------------------------------------
def cadastrar():
    global imagem, imagem_string, l_imagem

    # Obtendo os valores
    nome = e_nome.get()
    documento = e_documento.get()
    genero = e_sexo.get()
    data_nascimento = e_data_nascimento.get()
    tel = e_tel.get()
    email = e_email.get()
    cidade = e_cidade.get()
    estado = e_estado.get()
    nacionalidade = e_nacionalidade.get()
    deficiencia = e_deficiencia.get()
    informacoes = e_descricao.get("1.0", "end-1c")
    curso = e_cursos.get()
    turma = e_turma.get()
    imagem = imagem_string

    lista = [nome, documento, genero, data_nascimento, tel, email, cidade, estado, nacionalidade, deficiencia, informacoes, curso, turma, imagem]

    # Verificando se a lista contém valor vazio
    for i in lista:
        if not str(i).strip():
            messagebox.showerror('Erro', 'Preencha todos os campos!')
            return

    # Registrando os valores
    sistema_de_registro.cadastrar_estudante(lista)

    # Limpando os campos de entrada
    e_nome.delete(0, END)
    e_documento.delete(0, END)
    e_sexo.delete(0, END)
    e_data_nascimento.delete(0, END)
    e_tel.delete(0, END)
    e_email.delete(0, END)
    e_cidade.delete(0, END)
    e_estado.delete(0, END)
    e_nacionalidade.delete(0, END)
    e_deficiencia.delete(0, END)
    e_descricao.delete("1.0", "end")
    e_cursos.delete(0, END)
    e_turma.delete(0, END)

    # Abrindo a imagem
    imagem = Image.open('vetor.jpg')
    imagem = imagem.resize((145, 170))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_botoes, image=imagem, bg=co0, fg=co4)
    l_imagem.place(x=330, y=7)

    # Mostrando os valores na tabela
    mostrar_alunos()

def procurar():
    global imagem, imagem_string, l_imagem

    # Obtendo id
    id_aluno = e_procurar.get()

    # Procurando aluno
    dados = sistema_de_registro.procurar_estudante(id_aluno)

    # Limpando os campos de entrada
    e_nome.delete(0, END)
    e_documento.delete(0, END)
    e_sexo.delete(0, END)
    e_data_nascimento.delete(0, END)
    e_tel.delete(0, END)
    e_email.delete(0, END)
    e_cidade.delete(0, END)
    e_estado.delete(0, END)
    e_nacionalidade.delete(0, END)
    e_deficiencia.delete(0, END)
    e_descricao.delete("1.0", "end")
    e_cursos.delete(0, END)
    e_turma.delete(0, END)

    # Inserir os valores nos campos de entrada
    e_nome.insert(END, dados[1])
    e_documento.insert(END, dados[2])
    e_sexo.insert(END, dados[3])
    e_data_nascimento.insert(END, dados[4])
    e_tel.insert(END, dados[5])
    e_email.insert(END, dados[6])
    e_cidade.insert(END, dados[7])
    e_estado.insert(END, dados[8])
    e_nacionalidade.insert(END, dados[9])
    e_deficiencia.insert(END, dados[10])
    e_descricao.insert("1.0", dados[11])
    e_cursos.insert(END, dados[12])
    e_turma.insert(END, dados[13])

    imagem = dados[14]
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((145, 170))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_botoes, image=imagem, bg=co0, fg=co4)
    l_imagem.place(x=330, y=7)

def alterar():
    global imagem, imagem_string, l_imagem

    id_aluno = e_procurar.get()

    # Obtendo os valores
    nome = e_nome.get()
    documento = e_documento.get()
    genero = e_sexo.get()
    data_nascimento = e_data_nascimento.get()
    tel = e_tel.get()
    email = e_email.get()
    cidade = e_cidade.get()
    estado = e_estado.get()
    nacionalidade = e_nacionalidade.get()
    deficiencia = e_deficiencia.get()
    informacoes = e_descricao.get("1.0", "end-1c")
    curso = e_cursos.get()
    turma = e_turma.get()
    imagem = imagem_string

    lista = [nome, documento, genero, data_nascimento, tel, email, cidade, estado, nacionalidade, deficiencia, informacoes, curso, turma, imagem, id_aluno]

    # Verificando se a lista contém valor vazio
    for i in lista:
        if not str(i).strip():
            messagebox.showerror('Erro', 'Preencha todos os campos!')
            return

    # Registrando os valores
    sistema_de_registro.alterar_estudante(lista)

    # Limpando os campos de entrada
    e_nome.delete(0, END)
    e_documento.delete(0, END)
    e_sexo.delete(0, END)
    e_data_nascimento.delete(0, END)
    e_tel.delete(0, END)
    e_email.delete(0, END)
    e_cidade.delete(0, END)
    e_estado.delete(0, END)
    e_nacionalidade.delete(0, END)
    e_deficiencia.delete(0, END)
    e_descricao.delete("1.0", "end")
    e_cursos.delete(0, END)
    e_turma.delete(0, END)

    # Abrindo a imagem
    imagem = Image.open('vetor.jpg')
    imagem = imagem.resize((145, 170))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_botoes, image=imagem, bg=co0, fg=co4)
    l_imagem.place(x=330, y=7)

    # Mostrando os valores na tabela
    mostrar_alunos()

def excluir():
    global imagem, imagem_string, l_imagem

    id_aluno = int(e_procurar.get())

    # Deletando aluno
    sistema_de_registro.excluir_estudante(id_aluno)

    # Limpando os campos de entrada
    e_nome.delete(0, END)
    e_documento.delete(0, END)
    e_sexo.delete(0, END)
    e_data_nascimento.delete(0, END)
    e_tel.delete(0, END)
    e_email.delete(0, END)
    e_cidade.delete(0, END)
    e_estado.delete(0, END)
    e_nacionalidade.delete(0, END)
    e_deficiencia.delete(0, END)
    e_descricao.delete("1.0", "end")
    e_cursos.delete(0, END)
    e_turma.delete(0, END)

    e_procurar.delete(0, END)

    # Abrindo a imagem
    imagem = Image.open('vetor.jpg')
    imagem = imagem.resize((145, 170))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_botoes, image=imagem, bg=co0, fg=co4)
    l_imagem.place(x=330, y=7)

    # Mostrando os valores na tabela
    mostrar_alunos()

# ---------------------------------------------------Procurar aluno-----------------------------------------------------------------------------
frame_procurar_aluno = Frame(frame_botoes, width=40, height=55, bg=co1, relief=RAISED)
frame_procurar_aluno.grid(row=0,column=0, pady=0, padx=10, sticky=NSEW)

l_nome = Label(frame_procurar_aluno, text="[ N° Matricula do Aluno ] *", anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_nome.grid(row=0,column=0, pady=6, padx=4, sticky=NSEW)
e_procurar = Entry(frame_procurar_aluno, width=10, justify='center', relief="solid", font='Ivy 10')
e_procurar.grid(row=1,column=0, pady=11, padx=0, sticky=NSEW)

botao_procurar = Button(frame_procurar_aluno, command=procurar, text='Procurar', width=6, anchor=CENTER, overrelief=RIDGE, font='Ivy 7 bold', bg=co8, fg=co1, bd=2 )
botao_procurar.grid(row=1,column=1, pady=12, padx=4, sticky=NSEW)

# Botões
botao_cadastrar = Image.open('add.png')
botao_cadastrar = botao_cadastrar.resize((25, 25))
botao_cadastrar = ImageTk.PhotoImage(botao_cadastrar)
app_cadastrar = Button(frame_botoes, command=cadastrar, image=botao_cadastrar, relief=GROOVE, text=' Cadastrar', width=100, compound=LEFT, overrelief=RIDGE, font='Ivy 11', bg=co8, fg=co1, bd=3)
app_cadastrar.grid(row=1, column=0, pady=2, padx=20, sticky=NSEW)

botao_editar = Image.open('alterar.png')
botao_editar = botao_editar.resize((25, 25))
botao_editar = ImageTk.PhotoImage(botao_editar)
app_editar = Button(frame_botoes, command=alterar, image=botao_editar, relief=GROOVE, text=' Alterar', width=100, compound=LEFT, overrelief=RIDGE, font='Ivy 11', bg=co8, fg=co1, bd=3)
app_editar.grid(row=2, column=0, pady=2, padx=20, sticky=NSEW)

botao_excluir = Image.open('delete.png')
botao_excluir = botao_excluir.resize((25, 25))
botao_excluir = ImageTk.PhotoImage(botao_excluir)
app_excluir = Button(frame_botoes, command=excluir, image=botao_excluir, relief=GROOVE, text=' Excluir', width=100, compound=LEFT, overrelief=RIDGE, font='Ivy 11', bg=co8, fg=co1, bd=3)
app_excluir.grid(row=3, column=0, pady=2, padx=20, sticky=NSEW)

# Barra de divisão
barra_vertical = Label(frame_botoes, relief='sunken', width=0, height=80, bg=co3, fg=co0)
barra_vertical.place(x=280, y=0)

text_rodape = f"© {datetime.datetime.now().year} Robson Oliveira Rocha - Todos os direitos reservados."
label_copyright = Label(frame_rodape, text=text_rodape, bg=co6, fg=co1, font='Verdana 9')
label_copyright.pack(pady=3)

# Chamar a tabela
mostrar_alunos()

janela.mainloop()





