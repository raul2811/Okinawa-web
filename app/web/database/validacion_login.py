from bcrypt import checkpw
from database.db import Usuario, Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import or_
import datetime

class Login:
    """
    Esta clase proporciona un método estático para iniciar sesión a un usuario
    en el sistema.

    Args:
        username (str): Nombre de usuario del usuario que intenta iniciar sesión.
        password (str): Contraseña ingresada por el usuario.

    Returns:
        Usuario: Objeto Usuario si la contraseña es correcta, None en caso contrario.

    Raises:
        NoResultFound: Si el usuario no se encuentra en la base de datos.
        Exception: Si ocurre cualquier otra excepción inesperada.
    """

    @staticmethod
    def login(username: str, password: str):
        """
        Intenta iniciar sesión a un usuario en el sistema.

        1. Abre una sesión con la base de datos usando el contexto `with Session() as session:`.
        2. Busca el usuario en la base de datos por su nombre de usuario o email.
        3. Si se encuentra el usuario, compara la contraseña ingresada con la contraseña almacenada usando `checkpw`.
          - Si las contraseñas coinciden, imprime un mensaje de inicio de sesión exitoso y devuelve el objeto `usuario`.
          - Si las contraseñas no coinciden, imprime un mensaje de contraseña incorrecta y devuelve `None`.
        4. Si no se encuentra el usuario, imprime un mensaje indicando que el usuario no existe y devuelve `None`.
        5. Si ocurre cualquier excepción durante el proceso, imprime un mensaje de error genérico y devuelve `None`.
        """

        with Session() as session:
            try:
                usuario = session.query(Usuario).filter(or_(Usuario.email == username, Usuario.username == username)).one()
                stored_password = usuario.password.password
                if checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                    print(datetime.datetime.now())
                    print("La contraseña es correcta.")
                    print(f"Bienvenido {usuario.username} el usuario actual es un {usuario.tipo_usuario.tipo}.")
                    return usuario.tipo_usuario.tipo
                else:
                    print(datetime.datetime.now())
                    print(f"{usuario.username} La contraseña es incorrecta.")
                    return None
            except NoResultFound:
                print(datetime.datetime.now())
                print(f"El usuario:{username} no se encontró en la base de datos.")
                return None
            except Exception as e:
                print(datetime.datetime.now())
                print(f"Ocurrió un error inesperado: {e}")
                return None