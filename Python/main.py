import os
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

#Definindo o caminho absoluto para a criação e manipulação do banco (no caso, é junto dos arquivos python).
basedir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(basedir, "db_fichas.db")

db = create_engine(f"sqlite:///{db_path}")
Session = sessionmaker(bind=db) #Objeto para criação de sessão
session = Session()

Base = declarative_base() 

#Tables
class Personagens(Base):
    __tablename__ = "Personagens"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    hp = Column("hp", Integer)
    pm = Column("pm", Integer)

    classe = Column("classe", String)
    subclasse = Column("subclasse", String)

    level = Column("level", Integer)
    str = Column("str", Integer)
    dex = Column("dex", Integer)
    con = Column("con", Integer)
    int = Column("int", Integer)
    wis = Column("wis", Integer)
    cha = Column("cha", Integer)

    descricao = Column("descricao", String)

    def __init__(self, nome, hp, pm, classe, subclasse, level, str, dex, con, int, wis, cha, descricao):
        self.nome = nome
        self.hp = hp
        self.pm = pm
        self.classe = classe
        self.subclasse = subclasse
        self.level = level
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.descricao = descricao

Base.metadata.create_all(bind=db)

#Crud - CREATE
def create():
    nome="Rubens"
    hp=15 
    pm=30
    classe="Mago"
    subclasse="N/A" 
    level=17
    str=10 
    dex=12 
    con=10 
    int=22 
    wis=14
    cha=14 
    descricao="Um mago implacavel"

    personagem = Personagens(nome=nome, hp=hp, pm=pm, classe=classe, subclasse=subclasse, 
    level=level, str=str, dex=dex, con=con, int=int, wis=wis, cha=cha, descricao=descricao)
    session.add(personagem)
    session.commit()

#cRud - READ
def read_all():
    personagens = session.query(Personagens).all()
    for p in personagens:
        print(
        f"ID: {p.id}, Nome: {p.nome}, HP: {p.hp}, PM: {p.pm}, "
        f"Classe: {p.classe}, Subclasse: {p.subclasse}, Level: {p.level}, "
        f"STR: {p.str}, DEX: {p.dex}, CON: {p.con}, "
        f"INT: {p.int}, WIS: {p.wis}, CHA: {p.cha}, "
        f"Descrição: {p.descricao}"
)
        
#crUd - UPDATE
def update():
    id = 0
    personagemFiltrado = session.query(Personagens).filter_by(id=id).first()
    personagemFiltrado.nome = "Null"
    session.add(personagemFiltrado)
    session.commit()


#cruD - DELETE
def delete():
    id = input("Insira o ID do personagem que deseja deletar >> ").strip()
    personagem = session.query(Personagens).filter_by(id=id).first()
    if personagem:
        session.delete(personagem)
        session.commit()
        print(f"Personagem {personagem.nome} de id {personagem.id} foi excluido com sucesso.")
    else: print("Não encontrado para exclusão")


read_all()