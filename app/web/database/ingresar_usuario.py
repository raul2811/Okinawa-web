from bcrypt import hashpw, gensalt
from sqlalchemy.exc import SQLAlchemyError
from db import Session, Usuario, Password, DatosUsuario

def ingresar_usuario(username, email, password, nombre, apellido, telefono, rank):
    with Session() as session:
        # Verificamos si el usuario ya se encuentra en la base de datos
        usuario_existente = session.query(Usuario).filter_by(username=username).first()
        if usuario_existente:
            raise ValueError("El usuario ya existe en la base de datos")

        #verficamos si el correo ya esta siendo usado en otro udsuario
        existing_email = session.query(Usuario).filter_by(email=email).first()
        if existing_email:
            raise ValueError("El correo electrónico ya está en uso")

        # Metodo para encriptar la contraseña
        hashed_password = hashpw(password.encode('utf-8'), gensalt())

        # Creacion de las nuevas instancias de las distintas tablas para el nuevo usuario
        nuevo_usuario = Usuario(username=username, email=email)
        nueva_password = Password(password=hashed_password.decode('utf-8'))
        nuevos_datos_usuario = DatosUsuario(nombre=nombre, apellido=apellido, telefono=telefono)

        # Establecemos la relacion en las distintas instancias al nuevo usuario
        nuevo_usuario.rank = rank
        nuevo_usuario.password = nueva_password
        nuevo_usuario.datos_usuario = nuevos_datos_usuario

        # Agregamos los cambios a la session y luego le realizamos un commit
        try:
            session.add(nueva_password)  # Agregamos la instancia de Password a la sesión
            session.add(nuevo_usuario)
            session.add(nuevos_datos_usuario)
            session.commit()
            print("Usuario ingresado correctamente.")
        except SQLAlchemyError as error:
            session.rollback()
            print(f"Error al ingresar el usuario: {error}")
# Ejemplo
#ingresar_usuario("angelcl", "angelcruz@gmail.com", "megadolon", "Angel", "Cruz", "62877034", 1)
#ingresar_usuario("raul2810", "raulantoni2810@gmail.com", "raul2810@", "Raul", "Serrano", "63633231", 2)