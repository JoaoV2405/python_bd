from sqlalchemy import  Column, Integer, String, ForeignKey, create_engine, insert, inspect, select
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship


Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(9))
    contas = relationship("Conta",back_populates = "cliente")
    
    def __repr__(self):
        return f"({self.__class__.__name__}) name:{self.name}, cpf: {self.cpf}, contas:({self.contas})"
    
class Conta(Base):
    __tablename__ = "contas"

    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey("clientes.id"),nullable=False)
    cliente = relationship("Cliente",back_populates = "contas")
    def __repr__(self):
        return f"({self.__class__.__name__}) id:{self.id}"


engine = create_engine("sqlite+pysqlite:///:memory:")

#criando as tabelas
Base.metadata.create_all(engine)


#inspecionando esquema do  bd
inspector_engine = inspect(engine)
print(inspector_engine.get_columns("contas"))

print(inspector_engine.get_table_names())

print(inspector_engine.has_table("contas"))

#Adiçao de clientes
with Session(engine) as session:
    joao = Cliente(
        id = 1,
        name = "joao",
        cpf= 123456789,
        endereco= "abubu"
    )
    
    vito = Cliente(
        id = 2,
        name = "vito",
        cpf= 123456789,
        endereco= "abubu"
    )
    
    mendes = Cliente(
        id = 3,
        name = "mendes",
        cpf= 123456789,
        endereco= "abubu"
    )
    
    session.add_all([joao, vito, mendes])
    
    session.commit()
    
    
#Recuperando clientes    
stmt = select(Cliente)
for user in session.scalars(stmt): 
    print(user)
    
#Adicionando conta
conta_joao = Conta(
    id = 123,
    tipo = "corrente",
    agencia = "1",
    num = 1,
    id_cliente = 1
)
session.add(conta_joao)
session.commit() 

#recuperando usuarios que tem contas
aa = select(Cliente).where(Cliente.contas)
for user in session.scalars(aa): 
    print(user)
