from gui import *
import backend as core

app = None
app = gui()

def view_command():
    rows = core.view()
    app.listLivros.delete(0, END)
    for r in rows:
        app.listLivros.insert(END,r)

def search_command():
    app.listLivros.delete(0, END)
    rows =  core.search(app.txtTitulo.get(),app.txtSubtitulo.get(),app.txtEditora.get(), app.txtAutor1.get(), app.txtAutor2.get(), app.txtAutor3.get(), app.txtCidade.get(),app.txtAno.get(),app.txtEdicao.get(), app.txtPaginas.get(), app.txtVolume.get())
    for r in rows:
        app.listLivros.insert(END, r)

def insert_command():
    core.insert(app.txtTitulo.get(),app.txtSubtitulo.get(),app.txtEditora.get(), app.txtAutor1.get(), app.txtAutor2.get(), app.txtAutor3.get(), app.txtCidade.get(),app.txtAno.get(),app.txtEdicao.get(), app.txtPaginas.get(), app.txtVolume.get())
    view_command()

def update_command():
    core.update(selected[0],app.txtTitulo.get(),app.txtSubtitulo.get(),app.txtEditora.get(), app.txtAutor1.get(), app.txtAutor2.get(), app.txtAutor3.get(), app.txtCidade.get(),app.txtAno.get(),app.txtEdicao.get(), app.txtPaginas.get(), app.txtVolume.get())
    view_command()

def del_command():
    id = selected[0]
    core.delete(id)
    view_command()

def getSelectedRow(event):
    global selected
    index = app.listLivros.curselection()[0]
    selected = app.listLivros.get(index)
    app.enttitulo.delete(0, END)
    app.enttitulo.insert(END, selected[1])
    app.entsubtitulo.delete(0, END)
    app.entsubtitulo.insert(END, selected[2])
    app.enteditora.delete(0, END)
    app.enteditora.insert(END, selected[3])
    app.entautor1.delete(0, END)
    app.entautor1.insert(END, selected[4])
    app.entautor2.delete(0, END)
    app.entautor2.insert(END, selected[5])
    app.entautor3.delete(0, END)
    app.entautor3.insert(END, selected[6])
    app.entcidade.delete(0, END)
    app.entcidade.insert(END, selected[7])
    app.entano.delete(0, END)
    app.entano.insert(END, selected[8])
    app.entedicao.delete(0, END)
    app.entedicao.insert(END, selected[9])
    app.entpaginas.delete(0, END)
    app.entpaginas.insert(END, selected[10])
    app.entvolume.delete(0, END)
    app.entvolume.insert(END, selected[11])
app = gui()

app.listLivros.bind('<<ListboxSelect>>', getSelectedRow)

app.btnViewAll.configure(command=view_command)
app.btnBuscar.configure(command=search_command)
app.btnInserir.configure(command=insert_command)
app.btnUpdate.configure(command=update_command)
app.btnDel.configure(command=del_command)
app.btnClose.configure(command=app.window.destroy)


app.run()
