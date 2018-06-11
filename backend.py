import sqlite3
import sqlite3 as sql

def iniitDB():
    database = "minhabiblioteca.db"
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE livros(id INTEGER PRIMARY KEY, titulo TEXT, subtitulo TEXT, editora TEXT, autor1 TEXT, autor2 TEXT, autor3 TEXT, cidade TEXT, ano TEXT, edicao TEXT, paginas TEXT, volume TEXT);""")
    conn.commit()
    conn.close()
iniitDB()
def view():
    database = "minhabiblioteca.db"
    conn = sqlite3.connect(database)
    cur  = conn.cursor()
    cur.execute("SELECT * FROM livros")
    for rows in cur.fetchall():
        return rows
    conn.commit()
    conn.close()

def insert (titulo,subtitulo,editora,autor1,autor2,autor3,cidade,ano,edicao,paginas,volume):
    database = "minhabiblioteca.db"
    conn = sqlite3.connect(database)
    cur  = conn.cursor()
    cur.execute("""INSERT INTO livros VALUES(NUll,?,?,?,?,?,?,?,?,?,?,?)""",[titulo,subtitulo,editora,autor1,autor2,autor3,cidade,ano,edicao,paginas,volume])
    conn.commit()
    conn.close()

def search(titulo="",subtitulo="",editora="",autor1="",autor2="",autor3="",cidade="",ano="",edicao="",paginas="",volume=""):
    database = "minhabiblioteca.db"
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM livros WHERE titulo=? or subtitulo=? or editora=? or autor1=? or autor2=? or autor3=? or cidade=? or ano=? or edicao=? or paginas=? or volume=?",(titulo,subtitulo,editora,autor1,autor2,autor3,editora,ano,edicao,paginas,volume))
    for rows in cur.fetchall():
        return rows
    conn.commit()
    conn.close()

def update(titulo,subtitulo,editora,autor1,autor2,autor3,cidade,ano,edicao,paginas,volume):
    database = "minhabiblioteca.db"
    conn = sqlite3.connect(database)
    cur  = conn.cursor()
    cur.execute("UPDATE livros SET titulo=? or subtitulo=? or editora=? or autor1=? or autor2=? or autor3=? or cidade=? or ano=? or edicao=? or paginas=? or volume=?",(titulo,subtitulo,editora,autor1,autor2,autor3,editora,ano,edicao,paginas,volume,id))
    conn.commit()
    conn.close()

def delete(id):
    database = "minhabiblioteca.db"
    conn = sqlite3.connect(database)
    cur  = conn.cursor()
    cur.execute("DELETE FROM livros WHERE id=?",(id,))
    conn.commit()
    conn.close()
