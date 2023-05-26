# -*- coding: utf-8 -*-

import pytest
from tabla_html import TablaHtml, TablaHtmlException


def test_crea_tabla():
    cabecera = ["c1", "c2"]
    datos = [["d1", "d2"], ["d3", "d4"], ["d5", "d6"]]

    tabla = TablaHtml(cabecera, datos)
    result = tabla.crea_tabla()

    assert "<table><tr><th>c1</th><th>c2</th></tr><tr><td>d1</td><td>d2</td></tr><tr><td>d3</td><td>d4</td></tr><tr><td>d5</td><td>d6</td></tr></table>" == result


def test_inserta_estilo_cabecera():
    cabecera = ["c1", "c2"]
    estilo_cabecera = ["bold", "italic"]

    tabla = TablaHtml(cabecera, [])

    tabla.inserta_estilo_cabecera(estilo_cabecera)

    assert tabla.estilo_cabecera == estilo_cabecera


def test_inserta_estilo_cabecera_error():
    cabecera = ["c1", "c2"]
    estilo_cabecera = ["bold"]

    tabla = TablaHtml(cabecera, [])

    with pytest.raises(TablaHtmlException) as excinfo:
        tabla.inserta_estilo_cabecera(estilo_cabecera)

    assert "La longitud de los estilos de cabecera no coincide con la longitud de la cabecera" == str(excinfo.value)


def test_inserta_estilo_cuerpo():
    datos = [["d1", "d2"], ["d3", "d4"], ["d5", "d6"]]
    estilo_cuerpo = [["bold", "italic"], ["underline", "normal"], ["small", "big"]]

    tabla = TablaHtml([], datos)

    tabla.inserta_estilo_cuerpo(estilo_cuerpo)

    assert tabla.estilo_cuerpo == estilo_cuerpo


def test_inserta_estilo_cuerpo_error():
    datos = [["d1", "d2"], ["d3", "d4"], ["d5", "d6"]]
    estilo_cuerpo = [["bold"], ["underline", "normal"], ["small", "big"]]

    tabla = TablaHtml([], datos)

    with pytest.raises(TablaHtmlException) as excinfo:
        tabla.inserta_estilo_cuerpo(estilo_cuerpo)

    assert "La longitud de los estilos de cuerpo no coincide con la longitud del cuerpo" == str(excinfo.value)
