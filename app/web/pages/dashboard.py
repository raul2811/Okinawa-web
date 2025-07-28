from reflex import box, page, text, desktop_only, mobile_and_tablet, link, vstack, hstack, form, input, button
from pages.login import InputState


@page(route="/dashboard", title='Okinawa Studio Admin',on_load=InputState.obtener_cookies)
def dashboard():
    return box(
        desktop_only(
            box(
                hstack(
                    box(
                        text("Okinawa Estudio", class_name="titulo-columna"),
                        link("- Inicio", href="#", class_name="opcion"),
                        link("- Trámites", href="#", class_name="opcion"),
                        link("- Fotos", href="#", class_name="opcion"),
                        link("- Contratos", href="#", class_name="opcion"),
                        class_name="barra-izquierda"
                    ),
                    box(
                        form(
                            input(type="search", placeholder="Buscar...", class_name="busqueda-input"),
                        ),
                         class_name="busqueda-form"  
                    ),
                    box(
                        text("Bienvenido al panel de administracion", class_name="saludo"),
                        class_name="saludo-derecho"
                    ),
                    box(
                        vstack(
                            text("Usuarios", class_name="usuarios-titulo"),
                            button("Añadir", class_name="usuarios-boton"),
                        ),
                        class_name="usuarios-box"
                    ),
                    box(
                        vstack(
                            text("Fotografias recientes", class_name="fotos-titulo"),
                            button("Añadir", class_name="fotos-boton"),
                        ),
                        class_name="fotos-box"
                    ),
                ),
                class_name="admin-container"
            ),
        ),
    

        mobile_and_tablet(
            box(
                text("Bienvenido a la página de administrador", class_name="admin-title-mobile"),
                # Aquí puedes agregar más contenido que se mostrará en móviles y tabletas
            ),
            class_name="admin-container-mobile"
        ),
    )