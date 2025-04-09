from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///db_fichas.db")
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

#CRUD

#create: 
#template: personagem = Personagens(nome="", hp="", pm="", classe="", subclasse="", level="", str="", dex="", con="", int="", wis="", cha="", descricao="")
personagem = Personagens(nome="Mormito", hp="30", pm="10", classe="Technomancer", subclasse="N/A", level="19", str="16", dex="16", con="16", int="18", wis="14", cha="14", descricao="lorem ipsum dolor")
session.add(personagem)
session.commit()


