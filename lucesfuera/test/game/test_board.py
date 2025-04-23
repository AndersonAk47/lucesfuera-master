from lucesfuera.game.board import Posicion , Tablero 
from lucesfuera.game.Luz import Luz
import pytest



@pytest .mark .parametrize(
  "fila , col_ini , col_fin"
{
  (0 , 0 , 1)
  (0 , -5, -4)
  (0 , 100 , 101)
}
)

def test_posicion_deberia_mover_al_derecha(fila, col_ini, col_fin):
p: Posicion = Posicion(fila, col_ini)
resultado: Posicion = p.new_posicion_derecha()
esperado: Posicion = Posicion(fila, col_fin)
assert resultado = esperado


@pytest.mark.parametrize(
    "fila, col_ini, col_fin",
    [
        (0, 1, 0),
        (0, -4, -5),
        (0, 101, 100)
    ]
)
def test_posicion_deberia_mover_al_izquierda(fila, col_ini, col_fin):
    p: Posicion = Posicion(fila, col_ini)
    resultado: Posicion = p.new_posicion_izquierda()
    esperado: Posicion = Posicion(fila, col_fin)
    assert resultado == esperado



@pytest.mark.parametrize(
    "columna, fila_ini, fila_fin",
    [
        (0, 0, 1),
        (0, -2, -4),
        (0, 100, 101)
    ]
)
def test_posicion_deberia_mover_abajo(columna, fila_ini, fila_fin):
    p: Posicion = Posicion(fila_ini, columna)
    resultado: Posicion = p.new_posicion_abajo()
    esperado: Posicion = Posicion(fila_fin, columna)
    assert resultado == esperado




@pytest.mark.parametrize(
    "columna, fila_ini, fila_fin",
    [
        (0, 1, 0),
        (0, -3, -1),
        (0, 101, 100)
    ]
)
def test_posicion_deberia_mover_arriba(columna, fila_ini, fila_fin):
    p: Posicion = Posicion(fila_ini, columna)
    resultado: Posicion = p.new_posicion_arriba()
    esperado: Posicion = Posicion(fila_fin, columna)
    assert resultado == esperado






@pytest.fixture
def tablero_grande()
  return Tablero(8,8)

@pytest.fixture
def tablero_manual()
  return[
    [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF,],
    [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF,],
    [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF,],
    [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF,],
    [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF,],
    [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF,],
    [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF,],
    [Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF, Luz.OFF,]
  ]

def test_tablero_prender_apagar(tablero_grande , tablero_manual):
tablero_grande.prender_apagar(Posicion(0,0))
tablero_manual[0][0]= Luz.ON
assert tablero_grande.tablero = tablero_manual

tablero_grande.prender_apagar(Posicion(0,0))
tablero_manual[0][0]= Luz.OFF
assert tablero_grande.tablero = tablero_manual