from reflex import box,vstack,center,page,input,State,button, text, image, desktop_only, mobile_and_tablet,redirect,html, Cookie
from database.validacion_login import Login
import threading
import jwt

class InputState(State):
    """
    Esta clase representa el estado de los datos introducidos por el usuario para iniciar sesión y administra la información relacionada.
    """
    username: str = ""
    password: str = ""
    user_role: str = ""
    error: str = ""
    cookie: str = Cookie(name="auth")  # Use rx.Cookie for cookie management
    def clear_error(self):
        """
        Limpia el mensaje de error después de un breve retraso (0.1 segundos usando threading.Timer).
        Esto proporciona una señal visual temporal al usuario sin saturar la interfaz de usuario por mucho tiempo.
        """
        self.error = ""
    def login_handler(self):
        """
        Gestiona el proceso de inicio de sesión iniciado por una acción del usuario (p. ej., hacer clic en un botón de inicio de sesión).
        """
        if not self.username or not self.password:
            """
            Comprueba si tanto el nombre de usuario como la contraseña están vacíos.
            Si es así, establece un mensaje de error y lo borra después de un retraso utilizando clear_error.
            """
            self.error = "Ambos campos son obligatorios."
            threading.Timer(0.1, self.clear_error).start()  
            return
        try:
            """
            Intenta realizar el inicio de sesión utilizando una clase Login (se asume que existe en otro lugar)
            y almacena el rol del usuario si tiene éxito.
            """
            self.user_role = Login.login(self.username, self.password)
            print("el tipo de usuario es {}".format(self.user_role))
            """
            Si el inicio de sesión es exitoso, almacena el nombre de usuario y la contraseña en un JWT (JSON Web Token)
            y establece la cadena JWT como el valor de la cookie "auth".
            """
            if self.user_role:
                self.guardar_cookies(self.username, self.password)
                return redirect("/dashboard")
            else:
                """
                Si el inicio de sesión falla, establece un mensaje de error y lo borra después de un retraso.
                """
                self.error = "Nombre de usuario o contraseña incorrectos."  
                threading.Timer(0.1, self.clear_error).start()  
        except Exception as e:
            """
            Captura cualquier excepción durante el proceso de inicio de sesión y registra el error.
            Limpia el rol del usuario para garantizar un estado limpio.
            """
            print(e)
            self.user_role = None
    def guardar_cookies(self, username, password):
        jwt_payload = {"username": username, "password": password}
        self.cookie = str(jwt.encode(jwt_payload, "secret", algorithm="HS256"))

        print("Valor de la cookie:", self.cookie)

    def obtener_cookies(self): 
        """
        Comprueba si existe la cookie "auth". Si es así, imprime el valor de la cookie.
        De lo contrario, imprime un mensaje que indica que no se encuentra el token y redirige al inicio de sesión.
        Es probable que este método se use en una parte separada de su aplicación para verificar la autenticación del usuario
        en función de la presencia de una cookie válida.
        """
        if self.cookie:
            print(self.cookie)
        else:
            print("No se encuentra el token")
            return redirect("/login")
            
@page(route="/login", title='Okinawa Studio login')
def login():
    return box(
        desktop_only(
            box(
                box(
                    image(src="/fotos/01.avif", class_name="left-image"),
                    class_name="left-container"
                ),
                box(
                    image(src="/divisor.svg", class_name="top-image"),
                    text("OKINAWA ESTUDIO", class_name="parrafo-title"),  
                    center(
                        vstack(
                            box(
                                text("¡Hola! ¡Bienvenido a tu espacio! "),
                                class_name="login-title",
                            ),
                            box(
                                input(
                                    value=InputState.username,
                                    on_change=InputState.set_username,
                                    placeholder="Ingresar su nombre de usuario",
                                    id="username-input",  
                                ),
                                class_name="input-box",
                            ),
                            box(
                                input(
                                    value=InputState.password,
                                    on_change=InputState.set_password,
                                    placeholder="Ingresar su contraseña", 
                                    type="password",
                                    id="password-input",  
                                ),
                                class_name="input-box",
                            ),
                            box(
                                text(InputState.error),
                                class_name="error-message",
                            ),
                            box(
                                button(
                                    "Iniciar Sesion",
                                    on_click=InputState.login_handler,
                                    id="login-button",
                                )
                                ,class_name="button-container"
                            ),
                             html("""
                                <script>
                                    document.addEventListener('DOMContentLoaded', (event) => {
                                        document.getElementById('username-input').addEventListener('keypress', function(event) {
                                            if (event.keyCode == 13) {
                                                document.getElementById('login-button').click();
                                            }
                                        });
                                        document.getElementById('password-input').addEventListener('keypress', function(event) {
                                            if (event.keyCode == 13) {
                                                document.getElementById('login-button').click();
                                            }
                                        });
                                    });
                                </script>
                            """),
                        ),
                        class_name="login-form",
                    ),
                    image(src="/divisor.svg", class_name="bottom-image"),  
                    class_name="right-container"
                ),
                class_name="main-container"
            )
        ),

        mobile_and_tablet(
        box(
            image(src="/divisor.svg", class_name="mobile-top-image"),
            center(
                vstack(
                    box(
                        text("OKINAWA ESTUDIO", class_name="mobile-parrafo-title"),
                        class_name="mobile-parrafo-title-container"
                    ),
                    box(
                        text("¡Hola! ¡Bienvenido a tu espacio! "),
                        class_name="mobile-login-title",
                    ),
                    box(
                        input(
                            value=InputState.username,
                            on_change=InputState.set_username,
                            placeholder="Ingresar su nombre de usuario",
                        ),
                        class_name="mobile-input-box",
                    ),
                    box(
                        input(
                            value=InputState.password,
                            on_change=InputState.set_password,
                            placeholder="Ingresar su contraseña", 
                            type="password",
                        ),
                        class_name="mobile-input-box",
                    ),
                    box(
                        text(InputState.error),
                        class_name="mobile-error-message",
                    ),
                    box(
                        button(
                            "Iniciar Sesion",
                            on_click=InputState.login_handler,
                        ),
                        class_name="mobile-button-container",
                    ),
                ),
                class_name="mobile-login-form",
            ),
            image(src="/divisor.svg", class_name="mobile-bottom-image"),
        ),
        class_name="mobile-main-container"
    ),
)