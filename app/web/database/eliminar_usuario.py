from db import session, Usuario, Password, DatosUsuario

def eliminar_usuario(user_id):
    #filtram el registro en la tabla "datos_usuario" que hace referencia al registro a la tabla que se va a eliminar usuarios
    datos_usuario = session.query(DatosUsuario).filter_by(user_id=user_id).first()

    # Verificamos si el registro existe en la tabla "datos_usuario"
    if datos_usuario:
        session.delete(datos_usuario)

    #filtramos el registro en la tabla "password" que hace referencia al registro de la tabla eliminar usuarios
    password = session.query(Password).filter_by(user_id=user_id).first()

    # Verificar si el registro existe en la tabla "password"
    if password:
        session.delete(password)

    #filtramos el registro en la tabla "usuarios"
    usuario = session.query(Usuario).filter_by(user_id=user_id).first()

    if usuario:
        session.delete(usuario)

        #Guardar los cambios en la base de datos
        session.commit()
        print("Usuario eliminado correctamente.")
    else:
        raise ValueError("El usuario no existe en la base de datos")

#ejemplo 
#eliminar_usuario(14)