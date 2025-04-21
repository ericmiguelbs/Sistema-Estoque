from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

#Base para as tabelas
Base = declarative_base()

#Criação do banco SQLite
engine = create_engine('sqlite:///itens.db', echo=True)


#Sessão para interagir com o banco
Session = sessionmaker(bind=engine)
session = Session()
