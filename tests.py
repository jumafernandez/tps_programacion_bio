def cuadrado(n):
    return n*n

def test_cuadrado():
    print('Voy a probar la función cuadrado...')
    assert(cuadrado(2)==4)
    assert(cuadrado(3)==9)
    
    print('pasó los tests...')

test_cuadrado()
