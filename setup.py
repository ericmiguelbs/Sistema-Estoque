from db.db import Base, engine
from db.item import Item


Base.metadata.create_all(engine)
print('Tabelas Criadas')