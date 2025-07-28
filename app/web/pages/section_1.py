from reflex import box, image, mobile_only, text, link, button, input, text_area, html, mobile_and_tablet, tablet_only, hstack

def section_1():
    image_data = [
        {"src": "fotos/01.avif"
        ,"bg": "lightgreen"},

        {"src": "fotos/02.avif"
        ,"bg": "lightblue"},

        {"src": "fotos/03.avif"
        ,"bg": "purple"},

        #son las imagenes intermedias
        {"src": "fotos/05.avif"
        ,"bg": "lightgreen"
        ,"text": "Sesiones de Estudio"
        ,"parrafo": "Vive una experiencia cautivadora en nuestras Sesiones de Estudio. Aunque estamos en Panamá, cada sesión es un viaje sensorial gracias a nuestros fondos y iluminación meticulosamente diseñados para evocar una estética distintiva. Déjate seducir por la magia de nuestros sets cuidadosamente creados, donde cada detalle te transportará a un mundo de belleza atemporal. "
        ,"texto_boton": "RESERVA TU SESIÓN!"},

        {"src": "fotos/02.avif"
        ,"bg": "lightgreen"
        ,"text": "Sesiones de Exterior"
        ,"parrafo": "Celebra tu esencia en los encantos naturales de Panamá durante nuestras Sesiones de Exterior. Nuestros fotógrafos capturarán momentos inolvidables en escenarios deslumbrantes, resaltando armoniosamente la belleza del entorno. Cada sesión es una experiencia única que plasma tu belleza en un lienzo moderno y cautivador."
        ,"texto_boton": "QUIERO MI SESIÓN"},

        {"src": "fotos/01.avif"
        ,"bg": "lightgreen"
        ,"text": "Graduaciones y Eventos"
        ,"parrafo": "Inmortaliza tus momentos más preciados con nuestras coberturas profesionales de Graduaciones y Eventos. Nuestro equipo de expertos capturará cada instante con pasión y destreza, asegurando que tus logros académicos, bodas, celebraciones y ocasiones especiales queden plasmados en recuerdos imborrables de la más alta calidad."
        ,"texto_boton": "CUBRE MI GRADUACIÓN"},

        #son las imagenes del equipo de trabajo
         {"src": "fotos/01.avif"
        ,"bg": "lightgreen"
        ,"text": "Kathleen Miranda"
        ,"parrafo": "Recién graduada de Diseño Gráfico en Panamá, Kathleen ha desarrollado un talento innato para el maquillaje. A través de estudios autodidactas, domina técnicas que realzan la belleza natural con toques sutiles pero impactantes, logrando looks luminosos y armoniosos que resaltan la esencia de cada persona."},

          {"src": "fotos/01.avif"
        ,"bg": "lightgreen"
        ,"text": "Carlos Correa"
        ,"parrafo": "Aunque es un joven estudiante panameño, Carlos posee conocimientos elevados en fotografía más allá de su edad. Con una pasión desbordante, logra captar la esencia de las personas a través de composiciones cautivadoras e iluminación distintiva. Su habilidad es hacer que los modelos luzcan naturales frente a la cámara."},

          {"src": "fotos/01.avif"
        ,"bg": "lightgreen"
        ,"text": "Raul Serrano"
        ,"parrafo": "Raúl se ha sumergido en Panamá en el estudio de posturas y expresiones corporales elegantes para la fotografía. Con paciencia inagotable y un profundo entendimiento de la imagen personal, guía a los clientes para encontrar poses orgánicas que resaltan su auténtica belleza interior y exterior de manera memorable."},
    ]
    
    text_box_inicial = [
    mobile_only(
        box(
            box(
                image(
                    src="fotos/tore.png",  
                    width="20%",
                    height="auto",
                    alt="Si no saben que es un tore es un portal de entrada a un templo en Japón xd",
                ),
                text("Quieres Saber Más de Nosotros?"),
                class_name="text-box-inicial slide-in",
            ),
            box(
                text ("Okinawa Estudio se enfoca en la fotografía con estilo japonés. Nuestro objetivo es brindarte algo único y un recuerdo que pasará a generaciones."),
                text ("Queremos que disfrutes de nuestro estudio tanto como puedas."),
                class_name="parrafo slide-in",
            ),
            box(
                link(
                    button("¡Trabaja con nosotros!", background_color= "#6E593C"),
                    href = ""
                ),
                class_name="boton slide-in",
            ),
            html("""
                <script>
                window.addEventListener('scroll', function() {
                  document.querySelectorAll('.slide-in').forEach(function(element) {
                   const slideInAt = (window.scrollY + window.innerHeight) - element.offsetHeight / 8;
                   const isHalfShown = slideInAt > element.offsetTop;
                   const isNotScrolledPast = window.scrollY < element.offsetTop + element.offsetHeight;

                   if (isHalfShown && isNotScrolledPast) {
                     element.classList.add('active');
                    } else {
                     element.classList.remove('active');
                    }
                });
            });
            </script>""")
        ),
    ),
]

    image_boxes = [
    mobile_and_tablet(
        box(
            *[
                box(
                    image(
                        src=img["src"],
                        width="100%",
                        height="100%",
                        alt="Que miras bobo xd",
                    ),
                    class_name="galeria"
                )
                for i, img in enumerate(image_data[0:9])
            ],
                html("""
                <script>
                document.querySelectorAll('.galeria').forEach(item => {
                    item.addEventListener('click', event => {
                        if (event.target.classList.contains('modo-zoom')) {
                            event.target.classList.remove('modo-zoom');
                        } else {
                            if (!document.querySelector('.modo-zoom')) {
                                event.target.classList.add('modo-zoom');
                            }
                        }
                    })
                })
                </script>
            """),
                class_name="image-galeria"
            )
        ),
    ]
        
    text_box_intermedio = [
        mobile_only(
            box(
                image(
                    src="fotos/camara.png",
                    width="20%",
                    height="auto",
                    alt="Camara de fotos con el tore xd",
                ),
                text("Nuestros Servicios"),
                class_name="text-box-intermedio",
            ),
        ),
    ]

    image_box_intermedio =[
    mobile_only(
        box(
            image(
                src=img["src"],
                width="100%",
                height="100%",
                alt="anda pa ya bobo xd",
            ),
            box(
                text(img["text"], class_name="text-box-imagen-intermedio"),
                text(img["parrafo"], class_name="parrafo-box-imagen-intermedio"),
                box(
                    button(img.get("texto_boton", ""), class_name="boton-box-imagen-intermedio"),
                    class_name="boton-contenedor"
                ),
            ),
            class_name="image-box-intermedio slide-in",
        ),
    )
    for i, img in enumerate(image_data[3:6])
]
    
    equipo_trabajo = [
        mobile_only(
            box(
                image(
                    src="fotos/mascara.png",
                    width="20%",
                    height="auto",
                    alt="Mascara samurai japonesa",
                ),
                text("Nuestro Equipo"),
                class_name="equipo-trabajo",
            ),
        ),
    ]

    equipo_trabajo_images = [
    mobile_only(
        box(
            *[
                box(
                    image(
                        src=img["src"],
                        width="100%",
                        height="100%",
                        alt="como tan muchacho xd",
                    ),
                    box(
                        text(img["text"], class_name="text-equipo"),
                        text(img["parrafo"], class_name="parrafo-equipo"),
                    ),
                    class_name="image-box-equipo-trabajo",
                )
                for i, img in enumerate(image_data[6:9])
            ],
            class_name="equipo-trabajo-images-container",
        ),
    ),
]
    
    redes_sociales_text = [
    mobile_only(
        box(
            image(
                src="fotos/josei.png",
                width="20%",
                height="auto",
                alt="Pos es una mujer con un kimono, bobo o que",
            ),
            text("Redes Sociales"),
            class_name="redes-sociales-text slide-in",
        ),
        box(
            text("¡Déjate cautivar por la magia de Okinawa Estudio! Síguenos en nuestras redes sociales para descubrir un mundo de belleza cautivadora donde la elegancia oriental se fusiona con la vibrante esencia panameña."),
            class_name="parrafo-redes-sociales slide-in",
        ),
        box(
            image(
                src="divisor.svg", 
                alt="Patron dorado con fondo rojo carmesi",
                class_name="divisor"
            )
        ),
        box(
            link(image(src="/svg/instagram-logo.svg", width="1.5em"), href="https://www.instagram.com/okinawa.estudio/", alt="boton que lleva a la cuenta de instagram"),
            link(image(src="/svg/whatsapp.svg", width="1.5em"), href="", alt="boton que lleva a al whatsapp"),
            class_name="social-icons"
        ),
        box(
            image(
                src="divisor.svg", 
                alt="Patron dorado con fondo rojo carmesi",
                class_name="divisor"
            )
        ),
    ),
]
    
    formulario = [
    mobile_only(
        box(
            text("¡CONTACTANOS!"),
            class_name="formulario-text",
        ),
        box(
            input(
                placeholder="Ingresar su nombre",
                class_name="form1",
            ),
            class_name="input-box",
        ),
        box(
            input(
                placeholder="Ingresar un correo electrónico",
                class_name="form2",
            ),
            class_name="input-box",
        ),
        box(
            text_area(
                placeholder="Ingresar un mensaje...",
                class_name="form3",
            ),
            class_name="input-box",
        ),
        button("Enviar", type="submit"),
        reset_on_submit=True,
    ),
]
    
    #apartado de pc
    text_box_inicial_ta= [
    tablet_only(
        box(
            box(
                box(
                    box(
                        image(
                            src="fotos/tore.png",  
                            width="14%",
                            height="auto",
                            alt="Si no saben que es un tore es un portal de entrada a un templo en Japón xd",
                        ),
                        text("Quieres Saber"),
                        text("Más de Nosotros?", class_name="segundo-text"),
                        class_name="text-box-inicial-ta",
                    ),
                    box(
                        box(
                            text ("Okinawa Estudio se enfoca en la fotografía con estilo japonés. Nuestro objetivo es brindarte algo único y un recuerdo que pasará a generaciones."),
                            text ("Queremos que disfrutes de nuestro estudio tanto como puedas."),
                            class_name="parrafo-ta",
                        ),
                        box(
                            link(
                                button("¡Trabaja con nosotros!", background_color= "#6E593C", padding="10px 40px", width="200px", height="50px", font_size="20px", text_align="center"),
                                href = ""
                            ),
                            class_name="boton-ta",
                        ),
                        class_name="contenedor-parrafo-boton", 
                    ),
                    class_name="contenedor-ta", 
                ),
            ),
        ),
    ),
]
    text_box_intermedio_ta = [
        tablet_only(
            box(
                image(
                    src="fotos/camara.png",
                    width="14%",
                    height="auto",
                    alt="Camara de fotos con el tore xd",
                ),
                text("Nuestros Servicios", class_name="segundo-text"),
                class_name="text-box-intermedio-ta",
            ),
        ),
    ]

    image_box_intermedio_ta = [
    tablet_only(
        box(
            *[
                box(
                    image(
                        src=img["src"],
                        width="100%",
                        height="100%",
                        alt="anda pa ya bobo xd",
                    ),
                    box(
                        text(img["text"], class_name="text-box-imagen-intermedio-ta"),
                        text(img["parrafo"], class_name="parrafo-box-imagen-intermedio-ta"),
                    ),
                    box(
                        button(img.get("texto_boton", ""), class_name="boton-box-imagen-intermedio-ta"),
                        class_name="boton-contenedor-ta"
                    ),
                    class_name="image-box-intermedio-ta",
                )
                for i, img in enumerate(image_data[3:6])
            ],
            class_name="intermedio-images-container-ta",
        ),
    ),
]
    
    equipo_trabajo_ta = [
        tablet_only(
            box(
                image(
                    src="fotos/mascara.png",
                    width="14%",
                    height="auto",
                    alt="Mascara samurai japonesa",
                ),
                text("Nuestro Equipo"),
                class_name="equipo-trabajo-ta",
            ),
        ),
    ]

    equipo_trabajo_images_ta = [
    tablet_only(
        box(
            *[
                box(
                    image(
                        src=img["src"],
                        width="100%",
                        height="100%",
                        alt="como tan muchacho xd",
                    ),
                    box(
                        text(img["text"], class_name="text-equipo-ta"),
                        text(img["parrafo"], class_name="parrafo-equipo-ta"),
                    ),
                    class_name="image-box-equipo-trabajo-ta",
                )
                for i, img in enumerate(image_data[6:9])
            ],
            class_name="equipo-trabajo-images-container-ta",
        ),
    ),
]

    
  
    
    return box(
        *(text_box_inicial + text_box_inicial_ta + image_boxes +  text_box_intermedio + text_box_intermedio_ta + image_box_intermedio_ta + image_box_intermedio +  equipo_trabajo + equipo_trabajo_ta + equipo_trabajo_images + equipo_trabajo_images_ta + redes_sociales_text + formulario),
        class_name="Section_1"
    )