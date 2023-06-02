from tabla_html import TablaHtml
from mailer import Mailer


def crea_tabla():
    cabecera = ["c1", "c2"]
    datos = [["d1", "d2"], ["d3", "d4"], ["d5", "d6"]]
    estilo_cabecera = ["font-weight: bold;", "font-style: italic;"]
    estilo_datos = [["font-weight: bold;", "font-style: italic;"],
                    ["font-weight: bold;", "font-style: italic;"],
                    ["font-weight: bold;", "font-style: italic;"]]

    tabla = TablaHtml(cabecera, datos)
    tabla.inserta_estilo_cabecera(estilo_cabecera)
    tabla.inserta_estilo_cuerpo(estilo_datos)
    result = tabla.crea_tabla()
    return result

def crea_cuerpo(introduccion, tabla):
    return introduccion + '\n' + tabla

def envia_correo(cuerpo):
    mailer = Mailer()
    mailer.remitente = "soygonzalodeniz@gmail.com"
    mailer.destinatario = "relora9840@ratedane.com"
    mailer.asunto = "Hello"
    mailer.body = cuerpo
    mailer.envia_email_html()

def main():
    tabla = crea_tabla()
    intro = "Esto es una introduccion a la siguiente tabla\n"
    cuerpo = crea_cuerpo(intro, tabla)
    envia_correo(cuerpo)


if __name__ == "__main__":
    main()
