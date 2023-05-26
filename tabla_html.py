# -*- coding: utf-8 -*-

"""
Devuelve el código de una tabla en html

Dependencias: mypy 1.3
"""
from typing import List

class TablaHtmlException(Exception):
    pass

class TablaHtml:
    def __init__(self, cabecera: List[str], datos: List[List[str]]):
        self.datos_cabecera = cabecera
        self.datos_cuerpo = datos
        self.estilo_cabecera = None
        self.estilo_cuerpo = None

    def crea_tabla(self) -> str:
        table_html = "<table>"
        table_html += self._crea_html_cabecera()
        table_html += self._crea_html_cuerpo()
        table_html += "</table>"
        return table_html

    def inserta_estilo_cabecera(self, estilo_cabecera: List[str]) -> None:
        if not self._valida_longitud_estilo_cabecera(estilo_cabecera):
            raise TablaHtmlException("La longitud de los estilos de cabecera no coincide con la longitud de la cabecera")
        self.estilo_cabecera = estilo_cabecera

    def inserta_estilo_cuerpo(self, estilo_cuerpo: List[List[str]]) -> None:
        if not self._valida_longitud_estilo_cuerpo(estilo_cuerpo):
            raise TablaHtmlException("La longitud de los estilos de cuerpo no coincide con la longitud del cuerpo")
        self.estilo_cuerpo = estilo_cuerpo

    def _crea_html_cabecera(self) -> str:
        cabecera_html = "<tr>"
        for h in self.datos_cabecera:
            cabecera_html += f"<th>{h}</th>"
        cabecera_html += "</tr>"
        return cabecera_html

    def _crea_html_cuerpo(self) -> str:
        filas_html = ""
        for i in range(len(self.datos_cuerpo)):
            fila_dato = self.datos_cuerpo[i]
            filas_html += self._crea_html_fila(fila_dato)
        return filas_html

    def _crea_html_fila(self, fila) -> str:
        fila_html = "<tr>"
        for celda in fila:
            fila_html += f"<td>{celda}</td>"
        fila_html += "</tr>"
        return fila_html

    def _valida_longitud_estilo_cabecera(self, estilo_cabecera: List[str]) -> bool:
        return len(estilo_cabecera) == len(self.datos_cabecera)

    def _valida_longitud_estilo_cuerpo(self, estilo_cuerpo: List[List[str]]) -> bool:
        if len(estilo_cuerpo) != len(self.datos_cuerpo):
            return False

        for fila_estilo_cuerpo, fila_datos_cuerpo in zip(estilo_cuerpo, self.datos_cuerpo):
            if len(fila_estilo_cuerpo) != len(fila_datos_cuerpo):
                return False

        return True

h = ['c1', 'c2']
d = [['d1', 'd2'], ['d3', 'd4'], ['d5', 'd6']]
t = TablaHtml(h, d)
print(t.crea_tabla())
