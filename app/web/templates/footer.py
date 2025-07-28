from reflex import (
    box,
    hstack,
    vstack, 
    mobile_only,
    image,
    spacer,
    text,
    link,
)
import datetime  

# Definir colores como constantes
COLOR_BG = "#CB3233"
COLOR_TEXT = "#FFE1E3"

def footer():
    current_year = datetime.datetime.now().year  # Obtener el año actual
    return box(
        mobile_only(
            vstack(
                image(src="okinawa_logos/logo_navbar_mobil.svg", width="15%", alt="Logo Okinawa"),
                hstack(
                    link(image(src="svg/facebook-f.svg", width="0.65em", class_name="icon-border"), href="", alt="Facebook link", margin_left="1em", margin_right="1em"),  
                    link(image(src="svg/instagram-logo.svg", width="1em", class_name="icon-border"), href="https://www.instagram.com/okinawa.estudio/", alt="Instagram link", margin_left="1em", margin_right="1em"),  
                    link(image(src="svg/whatsapp.svg", width="1em", class_name="icon-border"), href="", alt="WhatsApp link", margin_left="1em", margin_right="1em"),    
                    justify_content="center",  # Centrar los iconos
                ),  
                spacer(size="2em"),  # Añadir un espacio en la parte inferior
                class_name="social-icons-container",  
                justify_content="center",  # Centrar el contenido horizontalmente
                align_items="center",  # Centrar el contenido verticalmente
            ),
            text(f"© {current_year} Okinawa Estudio",  # Usar el año actual
                display="flex",
                justify_content="center",
                align_items="center",
                padding="5px",
                font_size="10px",
                color="#ffffff",
                font_family="'my-font4'",
                background_color="#8E2324",
            ),
            class_name="footer",
            bg=COLOR_BG,
        )
    )