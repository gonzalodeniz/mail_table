from tabla_html import TablaHtml

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

print(result)