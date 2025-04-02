import sqlite3

def criar_tabela():
    connect = sqlite3.connect('db_fichas')
    cursor = connect.cursor()
    cursor.execute('''
                   
    CREATE TABLE IF NOT EXISTS personagens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(200), 
    
    classe VARCHAR(100),
    subclasse VARCHAR(100),
    nivel SMALLINT,

    forca SMALLINT,
    destreza SMALLINT,
    vigor SMALLINT,
    inteligencia SMALLINT,
    sabedoria SMALLINT
)
''')
    
    connect.commit()
    connect.close()

def add_personagem(nome, classe, subclasse, nivel, forca, destreza, vigor, inteligencia, sabedoria):
    connect = sqlite3.connect('db_fichas')
    cursor = connect.cursor()

    cursor.execute('''INSERT INTO personagens 
    (nome, classe, subclasse, nivel, forca, destreza, vigor, inteligencia, sabedoria) 
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''', (nome, classe, subclasse, nivel, forca, destreza, vigor, inteligencia, sabedoria))

    connect.commit()
    connect.close()
    

def listar_personagens():
    connect = sqlite3.connect('db_fichas')
    cursor = connect.cursor()

    cursor.execute('''SELECT * FROM personagens''')

    personagens = cursor.fetchall()
    for personagem in personagens:
        print(personagem)
    connect.close()


def atualizar_personagem(nome, classe, subclasse, nivel, forca, destreza, vigor, inteligencia, sabedoria):
    connect = sqlite3.connect('db_fichas')
    cursor = connect.cursor()

    cursor.execute('''UPDATE personagens SET nome = ?, classe = ?, subclasse = ?, nivel = ?, forca = ?, destreza = ?, vigor = ?, 
    inteligencia = ?, sabedoria = ?''', (nome, classe, subclasse, nivel, forca, destreza, vigor, inteligencia, sabedoria))

    connect.commit()
    connect.close()


def deletar_personagem(id):
    connect = sqlite3.connect('db_fichas')
    cursor = connect.cursor()

    cursor.execute('''DELETE FROM personagens WHERE id = ?''', (id,))

    connect.commit()
    connect.close()



criar_tabela()
listar_personagens()
atualizar_personagem("Mormito", "Lutador", "Technomancer", 20, 16, 14, 14, 18, 16)
listar_personagens()



