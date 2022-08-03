import  unittest
import cambiaTexto

class probarCmbiaTexto(unittest.TestCase):

    def test_mayuscula(self):
        palabra = "buen dia"
        resultado = cambiaTexto.todoMyus(palabra)
        self.assertEqual(resultado,"BUEN DIA")

if __name__ =='__main__':
    unittest.main()