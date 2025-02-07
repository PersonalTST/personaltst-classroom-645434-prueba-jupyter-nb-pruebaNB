def test_minimax():
    assert minimax(root, True) == 5, "La prueba falló: el valor óptimo debería ser 5"
    assert minimax(root, False) == 3, "La prueba falló: el valor óptimo debería ser 3"
    print("¡Todas las pruebas pasaron!")

test_minimax()
