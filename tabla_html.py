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
        self.datos_cabecera:  List[str] = cabecera
        self.datos_cuerpo:    List[List[str]] = datos
        self.estilo_cabecera: List[str] = []
        self.estilo_cuerpo:   List[List[str]] = [[]]
        self.estilo_tabla: str = "table { table-layout: auto; border-collapse: collapse; } " \
                                 "tr.cabecera { border-bottom: 2px solid #999; } " \
                                 "th, td { border-bottom: 1px solid #ddd; padding: 15px; text-align: left; }"

    def crea_tabla(self) -> str:
        table_html = "<table>"
        table_html += self._crea_estilo_tabla()
        table_html += self._crea_html_cabecera()
        table_html += self._crea_html_cuerpo()
        table_html += "</table>"
        return table_html

    def inserta_estilo_tabla(self, estilo_tabla: str) -> None:
        self.estilo_tabla = estilo_tabla

    def inserta_estilo_cabecera(self, estilo_cabecera: List[str]) -> None:
        if not self._valida_longitud_estilo_cabecera(estilo_cabecera):
            raise TablaHtmlException(
                "La longitud de los estilos de cabecera no coincide con la longitud de la cabecera")
        self.estilo_cabecera = estilo_cabecera

    def inserta_estilo_cuerpo(self, estilo_cuerpo: List[List[str]]) -> None:
        if not self._valida_longitud_estilo_cuerpo(estilo_cuerpo):
            raise TablaHtmlException("La longitud de los estilos de cuerpo no coincide con la longitud del cuerpo")
        self.estilo_cuerpo = estilo_cuerpo

    def _crea_estilo_tabla(self) -> str:
        estilo_tabla = "<style>"
        estilo_tabla += self.estilo_tabla
        estilo_tabla += "</style>"
        return estilo_tabla

    def _crea_html_cabecera(self) -> str:
        if self._hay_estilo_cabecera():
            return self._crea_html_cabecera_con_estilo()
        else:
            return self._crea_html_cabecera_sin_estilo()

    def _crea_html_cabecera_con_estilo(self) -> str:
        cabecera_html = "<tr>"
        for dato, estilo in zip(self.datos_cabecera, self.estilo_cabecera):
            cabecera_html += f"<th style='{estilo}'>{dato}</th>"
        cabecera_html += "</tr>"
        return cabecera_html

    def _crea_html_cabecera_sin_estilo(self) -> str:
        cabecera_html = "<tr class='cabecera'>"
        for h in self.datos_cabecera:
            cabecera_html += f"<th>{h}</th>"
        cabecera_html += "</tr>"
        return cabecera_html

    def _crea_html_cuerpo(self) -> str:
        if self._hay_estilo_cuerpo():
            return self._crea_html_cuerpo_con_estilo()
        else:
            return self._crea_html_cuerpo_sin_estilo()

    def _crea_html_cuerpo_sin_estilo(self) -> str:
        filas_html = ""
        for fila in self.datos_cuerpo:
            filas_html += self._crea_html_fila_sin_estilo(fila)
        return filas_html

    def _crea_html_cuerpo_con_estilo(self) -> str:
        filas_html = ""
        for fila_datos, fila_estilo in zip(self.datos_cuerpo, self.estilo_cuerpo):
            filas_html += self._crea_html_fila_con_estilo(fila_datos, fila_estilo)
        return filas_html

    def _crea_html_fila_con_estilo(self, fila_datos: List[str], fila_estilo: List[str]) -> str:
        fila_html = "<tr>"
        for celda, estilo in zip(fila_datos, fila_estilo):
            fila_html += f"<td style='{estilo}'>{celda}</td>"
        fila_html += "</tr>"
        return fila_html

    def _crea_html_fila_sin_estilo(self, fila: List[str]) -> str:
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

    def _hay_estilo_cabecera(self):
        return self.estilo_cabecera != []

    def _hay_estilo_cuerpo(self):
        return self.estilo_cuerpo != [[]]

