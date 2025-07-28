from reflex import box, center, text, mobile_and_tablet, desktop_only, link, image, button

def content_1():
    return box(
        mobile_and_tablet(
            center(
                box(
                    center(
                        text("Okinawa",
                             font_family="my-font",
                             color="white",
                             font_size="14vw",
                             text_shadow="2px 2px 4px rgba(0, 0, 0, 0.5)")
                    ),
                    center(
                        text("Estudio",
                             font_family="my-font4",
                             color="white",
                             font_size="7vw",
                             text_shadow="2px 2px 4px rgba(0, 0, 0, 0.5)",)
                    ),
                    center(
                        text("Fotografia | Maquillaje | Asesoría",
                             font_family="my-font4",
                             color="white",
                             font_size="3.5vw",
                             white_space="nowrap",
                             text_shadow="2px 2px 4px rgba(0, 0, 0, 0.5)")         
                    ),
                    box(
                        link(
                            button("Reserva", background_color= "#CB3233", box_shadow="2px 2px 4px rgba(0, 0, 0, 0.5)"),
                            href = "",
                            margin_top="20%",
                        ),
                        class_name="boton",
                    ),
                             width="42%",
                             height="90vh",
                             display="flex",
                             flex_direction="column",
                             justify_content="center",
                             align_items="center",
                    ),
                  ),
                    box(
                        link(image(src="/svg/instagram-logo.svg", width="1.5em"), href="https://www.instagram.com/okinawa.estudio/", alt="boton que lleva a la cuenta de instagram"),
                        link(image(src="/svg/whatsapp.svg", width="1.5em"), href="", alt="boton que lleva a al whatsapp"),
                        class_name="social-icons",
                        margin_top="auto",
                        background="none"
                    ),
                    
            class_name="content_1_mobile",
            bg="#032323",
            width="100%"
        ),
         
        desktop_only(
            center(
                box(
                    center(
                        text("Okinawa",
                             font_family="my-font",
                             color="#FFE1E3",
                             font_size="8vw",
                             padding_right="10%")
                    ),
                    center(
                        text("Estudio",
                             font_family="my-font4",
                             color="#FFE1E3",
                             font_size="4vw")
                    ),
                    center(
                        text("Fotografia | Maquillaje | Asesoría",
                             font_family="my-font4",
                             color="#FFE1E3",
                             font_size="2.5vw")
                    ),
                     width="42%",
                     height="90vh",
                     display="flex",
                     flex_direction="column",
                     justify_content="center",
                     align_items="center",
                )
            ),
        ),
        class_name="content_1",
        bg="#032323",
        width="100%"
    )