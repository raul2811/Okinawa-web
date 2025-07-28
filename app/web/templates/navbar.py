from reflex import (
    box,
    link,
    image,
    hstack,
    spacer,
    desktop_only,
    mobile_and_tablet,
    button,
    icon,
    html,
    script
)

# Definir colores como constantes
COLOR_BG = "#CB3233"
COLOR_TEXT = "#FFE1E3"

def create_link(text, href, **kwargs):
    # Función auxiliar para crear enlaces con estilos comunes
    return link(text
                   ,href=href
                   ,color=COLOR_TEXT
                   ,font_family="my-font4"
                   ,font_size="125%"
                   ,**kwargs)

def navbar():
    return box(
            desktop_only(
            hstack(
                hstack(
                    link(image(src="svg/facebook-f.svg"
                                    ,width="1em")
                                    ,href=""
                                    ,alt="boton que lleva a la cuenta de facebook")#enlaces de la barra de navegacion
                    ,link(image(src="svg/instagram-logo.svg"
                                    ,width="1.5em")
                                    ,href="https://www.instagram.com/okinawa.estudio/"
                                    ,alt="boton que lleva a la cuenta de instagram")#enlaces dela barra de navegacion
                    ,link(image(src="svg/whatsapp.svg"
                                      ,width="1.5em"))
                                      ,spacing="7"
                                      ,padding_left="2%"
                                      ,padding_top="1.5%"
                                      ,href=""
                                      ,alt="boton que lleva a al whatsapp")#enlaces dela barra de navegacion
                    ,create_link("Quienes Somos"
                                ,"#"
                                ,padding_top="1.5%"
                                ,padding_left="7%")
                    ,create_link("Portafolio"
                                ,"#"
                                ,padding_top="1.5%"
                                ,padding_left="4%")
                    ,create_link("Contacto"
                                ,"#"
                                ,padding_top="1.5%"
                                ,padding_left="4%")
                    ,create_link("Iniciar sesión"
                                ,"login"
                                ,padding_top="1.5%"
                                ,padding_left="4%")
                    ,spacer()
                    ,link("Okinawa Estudio"
                         ,font_family="my-font4"
                         ,color=COLOR_TEXT
                         ,font_size="150%"
                         ,padding_right="2%"
                         ,padding_top="1.5%"
                         ,href="/")
                )
            )
                    ,mobile_and_tablet(
                        hstack(
                            button(icon(tag="align_justify"
                                        ,color=COLOR_TEXT
                                        ,font_size="8vw"
                                        ,padding_top="1.5%"
                                        ,alt="Hamburguesa"
                                        ,id="hamburgerButton"
                                        ,margin_top="0.50em")  # Añadir margen en la parte superior
                                        ,variant="ghost")
                            ,spacer()
                            ,image(src="okinawa_logos/logo_navbar_mobil.svg"
                                    ,width="15%"
                                    ,padding_left="5%"
                                    ,alt="Logo Okinawa")
                        )
                        ,html("""
                            <!-- Se crea un div con la id 'dropdownMenu' que inicialmente no se vera -->
                            <div id="dropdownMenu" style="display: none;"> 

                            <!-- Se crea un div con la clase menu-container -->
                            <div class="menu-container"> <!-- Se crea un div con la clase menu-container -->

                            <!-- Se crean los enlaces del menu desplegable -->
                                <a href="#" class="menu-item">Quienes Somos</a>
                                <a href="#" class="menu-item">Portafolio</a>
                                <a href="#" class="menu-item">Contacto</a>
                                <a href="login" class="menu-item">Iniciar sesión</a>
                            </div>
                        </div>
                        """)
                        ,script("""
                            // Se agrega un event listener al boton de la hamburguesa
                            document.getElementById('hamburgerButton').addEventListener('click', function() {
                                var dropdownMenu = document.getElementById('dropdownMenu'); // Se obtiene el div con la id 'dropdownMenu'
                                if (dropdownMenu.style.display === 'none') { // Si el div esta oculto, se muestra
                                    dropdownMenu.style.display = 'grid'; // Se cambia el display a grid
                                } else {
                                    dropdownMenu.style.display = 'none'; // Si el div esta visible, se oculta
                                }
                            });
                                
                            // Se agrega un script para abrir una nueva pestaña al hacer click en los enlaces de redes sociales
                            (function() {
                                var anchors = document.getElementsByTagName("a");
                                for (var i = 0; i < anchors.length; i++) {
                                    var href = anchors[i].getAttribute('href');
                                    if (href === "https://www.facebook.com/" || href === "https://www.instagram.com/okinawa.estudio/" || href === "https://wa.me/yourNumber") {
                                        anchors[i].setAttribute('target', '_blank');
                                    }
                                }
                            })();
                       """)
                    )
        ,class_name="navbar"
        ,bg=COLOR_BG
)



