from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker ,relationship
from sqlalchemy.engine.url import URL

connection_string = URL.create(
    'postgresql',
    username='okinawa-estudio_owner',
    password='AvtTj9e5HIoP',
    host='ep-frosty-recipe-a5qztc43.us-east-2.aws.neon.tech',
    database='okinawa-estudio'
)

engine = create_engine(connection_string, connect_args={'sslmode': 'require'})

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

#hacemos el modelo de tipo_de_usuario
class TipoUsuario(Base):
    __tablename__ = 'tipo_de_usuarios'

    id_tipo_de_usuario= Column(Integer, primary_key=True)
    tipo= Column(String(50), nullable=False)

    def __repr__(self):
        return f"<id_tipo_de_usuario=(id={self.id_tipo_de_usuario}, tipo='{self.tipo}')>"

class Usuario(Base):
    __tablename__ = 'usuarios'#nombre de la tabla 

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    email = Column(String)
    rank = Column(Integer, ForeignKey('tipo_de_usuarios.id_tipo_de_usuario'))#se hace referencia a la key foranea de la tabla tipo de usuarios ,columna id de tipo de usuario

    # Definir la relación con la tabla de tipo_de_usuarios
    tipo_usuario = relationship("TipoUsuario")
    # Relación con la tabla de contraseñas
    password = relationship("Password", uselist=False, back_populates="usuario")  # Relación con la contraseña asociada a este usuario
    # Relación con la tabla de datos_usuario
    datos_usuario = relationship("DatosUsuario", uselist=False, back_populates="usuario")  
    
    def __repr__(self):
        return f"<Usuario(user_id={self.user_id}, username='{self.username}', email='{self.email}', rank='{self.rank}')>"

class Password(Base):
    __tablename__ = 'password'

    user_id = Column(Integer, ForeignKey('usuarios.user_id'), primary_key=True)  # user_id también es la clave primaria
    password = Column(String)

    # Definir la relación con la tabla de usuarios
    usuario = relationship("Usuario", back_populates="password")  # Relación con el usuario al que pertenece esta contraseña
    
    def __repr__(self):
        return f"<Password(user_id={self.user_id}, password='{self.password}')>"

class DatosUsuario(Base):
    __tablename__ = 'datos_usuario'

    user_id = Column(Integer, ForeignKey('usuarios.user_id'), primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    telefono = Column(String)
    # Relación con la tabla de usuarios
    usuario = relationship("Usuario", back_populates="datos_usuario")

    def __repr__(self):
        return f"<DatosUsuario(user_id={self.user_id}, nombre='{self.nombre}', apellido='{self.apellido}', telefono='{self.telefono}')>"