from lucesfuera.game.board import Posicion , Tablero  

def test_posicion_deberia_mover_al_derecha() :
  p=  Posicion = (0 , 0) 
  p1 = nueva_posicion_derecha() 
  assert p1.fila == 0   
  assert p1.columna == 1