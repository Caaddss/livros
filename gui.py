from tkinter import *

class gui():
    window = Tk()
    window.wm_title("Minha Biblioteca")

# Variáveis
    txtTitulo = StringVar()
    txtSubtitulo = StringVar()
    txtEditora = StringVar()
    txtAutor1 = StringVar()
    txtAutor2 = StringVar()
    txtAutor3 = StringVar()
    txtCidade = StringVar()
    txtAno = StringVar()
    txtEdicao = StringVar()
    txtPaginas = StringVar()
    txtVolume = StringVar()

# Objetos  que estarão na tela
    lbltitulo = Label(window, text="Título")
    lblsubtitulo = Label(window, text="Subtítulo")
    lbleditora =  Label(window, text="Editora")
    lblautor_1 = Label(window, text="1º Autor")
    lblautor_2 = Label(window, text="2º Autor")
    lblautor_3 = Label(window, text="3º Autor")
    lblcidade = Label(window, text="Cidade")
    lblano = Label(window,text="Ano da Publicação")
    lbledicao = Label(window, text="Edição")
    lblpaginas = Label(window,text="Páginas")
    lblvolume = Label(window, text="Volume")

# Campos de input
    enttitulo = Entry(window, textvariable=txtTitulo)
    entsubtitulo = Entry(window,textvariable=txtSubtitulo)
    enteditora = Entry(window, textvariable=txtEditora)
    entautor1 = Entry(window, textvariable=txtAutor1)
    entautor2 = Entry(window, textvariable=txtAutor2)
    entautor3 = Entry(window, textvariable=txtAutor3)
    entcidade = Entry(window, textvariable=txtCidade)
    entano = Entry(window, textvariable=txtAno)
    entedicao = Entry(window, textvariable=txtEdicao)
    entpaginas = Entry(window, textvariable=txtPaginas)
    entvolume = Entry(window, textvariable=txtVolume)

# Listbox com os livros cadastrados
    listLivros = Listbox(window)

# Scrollbar para funcionar junto com a listLivros
    scrollLivros = Scrollbar(window)

# Botões
    btnViewAll = Button(window, text = "Ver todos")
    btnBuscar  = Button(window, text = "Buscar")
    btnInserir = Button(window, text = "Inserir")
    btnUpdate  = Button(window, text = "Atualizar Selecionados")
    btnDel     = Button(window, text = "Deletar Selecionados")
    btnClose   = Button(window, text = "Fechar")

# Associar os objetos a grid da janela, primeiro as labels
    lbltitulo.grid(row=0, column=0)
    lblsubtitulo.grid(row=1, column=0)
    lbleditora.grid(row =2, column=0)
    lblautor_1.grid(row=3, column=0)
    lblautor_2.grid(row=4, column=0)
    lblautor_3.grid(row=5, column=0)
    lblcidade.grid(row=6, column=0)
    lblano.grid(row=7, column=0)
    lbledicao.grid(row=8, column=0)
    lblpaginas.grid(row=9, column=0)
    lblvolume.grid(row=10, column=0)

# Depois as entrys
    enttitulo.grid(row=0, column=1)
    entsubtitulo.grid(row=1, column=1)
    enteditora.grid(row=2, column=1)
    entautor1.grid(row=3, column=1)
    entautor2.grid(row=4, column=1)
    entautor3.grid(row=5, column=1)
    entcidade.grid(row=6, column=1)
    entano.grid(row=7, column=1)
    entedicao.grid(row=8, column=1)
    entpaginas.grid(row=9, column=1)
    entvolume.grid(row=10, column=1)

# Posicionando os Botões
    btnViewAll.grid(row=13,column=0,columnspan=2) #columnspan quando algo ocupa mais de uma coluna
    btnBuscar.grid(row=14, column=0,columnspan=2)
    btnInserir.grid(row=15, column=0,columnspan=2)
    btnUpdate.grid(row=16, column=0, columnspan=2)
    btnDel.grid(row=17, column=0, columnspan=2)
    btnClose.grid(row=18, column=0, columnspan=2)

# Posicionando a lista e o scrollLivros
    listLivros.grid(row=0, column=2,rowspan=10) #rowspan quando algo ocupa mais de uma linha
    scrollLivros.grid(row=0, column=6, rowspan=10)

# Associando o Scrollbar com a Listbox
    listLivros.configure(yscrollcommand=scrollLivros.set) # yscrollcommand responsável por definir qual objeto sera responsavel por acompanhar o rolamento vertical
    scrollLivros.configure(command=listLivros.yview) # qual função será chamada quando a ScrollBar for ativada

# Vamos agora arrumar a aparência
    x_pad = 5
    y_pad = 3
    width_entry = 50

    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')

    def run(self):
        gui.window.mainloop()
