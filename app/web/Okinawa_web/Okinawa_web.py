
from reflex import App, box, html, script, page, State,Component
from templates.navbar import navbar
from templates.divider import divider
from pages.content_1 import content_1
from pages.section_1 import section_1
from templates.footer import footer
from pages.login import login
from database.db import engine, session, Usuario
from pages.dashboard import dashboard


class State(State):
    "NADA DE MOMENTO XD"
    
@page(route='/'
         ,title="Okinawa Estudio - Fotografía en Panamá")


def index() -> Component:	
  return box(
     html("<meta name='description' content='Okinawa Studio es un apasionante y creativo estudio de fotografía en Panamá que encuentra su inspiración en la rica y cautivadora cultura japonesa. Al fusionar técnicas tradicionales y contemporáneas, así como incorporar costumbres arraigadas en la cultura nipona, este estudio se distingue por ofrecer una experiencia fotográfica única y significativa. A pesar de su enfoque en las tradiciones, Okinawa Studio también abraza la modernidad y la tecnología. La edición de imágenes y las técnicas de postproducción se utilizan de manera creativa para realzar la historia que se cuenta en cada fotografía, respetando al mismo tiempo los principios fundamentales de la estética japonesa.'/>")
    ,html("<lang='es'>")
    ,html("<link rel='apple-touch-icon' sizes='120x120' href='/apple-touch-icon-120x120.png' /> <link rel='apple-touch-icon' sizes='152x152' href='apple-touch-icon-152x152.png' />")
    ,script("document.addEventListener('contextmenu', event => event.preventDefault());")#elimina la accion del boton derecho del mouse
  	,navbar()
    ,script(src="js/service_worker_register.js")
    ,script(src="js/service_worker_update.js")
    ,script(src="js/service_worker.js")
    ,content_1()
    ,section_1()
    ,footer()
    ,class_name="Badground_slider"
		)
  
  
app = App(stylesheets=[
        "css/fonts.css"
        ,"css/global.css"
        ,"css/navbar.css"
        ,"css/content_1.css"
        ,"css/section_1.css"
        ,"css/login.css"
        ,"css/admin.css"
    ],)
app.add_page(index)