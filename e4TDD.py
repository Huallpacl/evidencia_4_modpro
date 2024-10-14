#Evidencia 4 Modpro

import time

class Licuadora:
    def __init__(self):
        self._encendida = False  
        self._velocidad = 0  
        self._temporizador = 0  
        self._rpm = 0  
    
    # Métodos para encender y apagar la licuadora
    def encender(self):
        self._encendida = True
        print("Licuadora encendida.")
    
    def apagar(self):
        self._encendida = False
        self._velocidad = 0
        self._rpm = 0
        print("Licuadora apagada.")
    
    # Método para establecer la velocidad
    def set_velocidad(self, velocidad):
        if not self._encendida:
            raise Exception("La licuadora debe estar encendida para cambiar la velocidad.")
        if velocidad not in [1, 2, 3]:
            raise ValueError("Velocidad inválida. Solo puede ser 1, 2 o 3.")
        
        self._velocidad = velocidad
        if velocidad == 1:
            self._rpm = 25
        elif velocidad == 2:
            self._rpm = 50
        elif velocidad == 3:
            self._rpm = 75
        
        print(f"Velocidad fijada en {velocidad} ({self._rpm} rpm).")
    
    # Método para establecer el temporizador en segundos
    def set_temporizador(self, segundos):
        if segundos < 0 or segundos > 120:  # 120 segundos = 2 minutos máximo
            raise ValueError("El temporizador debe estar entre 0 y 120 segundos.")
        
        self._temporizador = segundos
        print(f"Temporizador fijado en {segundos} segundos.")
    
    # Método para iniciar el programa de la licuadora
    def iniciar(self):
        if not self._encendida:
            raise Exception("La licuadora debe estar encendida para iniciar el programa.")
        if self._velocidad == 0:
            raise Exception("Debe fijarse una velocidad diferente de 0 para iniciar.")
        if self._temporizador <= 0:
            raise Exception("El temporizador debe ser mayor que 0 para iniciar.")
        
        print(f"Iniciando licuadora a {self._rpm} rpm por {self._temporizador} segundos.")
        try:
            for i in range(self._temporizador):
                time.sleep(1)  # Pausa de 1 segundo en cada iteración
                print(f"Licuadora en operación: {i + 1} segundos")
        except KeyboardInterrupt:
            print("Programa interrumpido.")
        
        self.apagar()
        
import unittest

class TestLicuadora(unittest.TestCase):
    def setUp(self):
        self.licuadora = Licuadora()

    def test_encender_apagar(self):
        self.licuadora.encender()
        self.assertTrue(self.licuadora._encendida)  # Verificamos el estado interno de encendido

        self.licuadora.apagar()
        self.assertFalse(self.licuadora._encendida)
        self.assertEqual(self.licuadora._velocidad, 0)
        self.assertEqual(self.licuadora._rpm, 0)

    def test_cambiar_velocidad(self):
        self.licuadora.encender()
        self.licuadora.set_velocidad(2)
        self.assertEqual(self.licuadora._velocidad, 2)
        self.assertEqual(self.licuadora._rpm, 50)

    def test_temporizador(self):
        self.licuadora.set_temporizador(60)
        self.assertEqual(self.licuadora._temporizador, 60)

    def test_iniciar_programa(self):
        self.licuadora.encender()
        self.licuadora.set_velocidad(3)
        self.licuadora.set_temporizador(1)
        # La siguiente línea simulará que el programa se inicia
        self.licuadora.iniciar()
        self.assertFalse(self.licuadora._encendida)  # Se apaga al finalizar

    def test_error_si_no_enciende(self):
        with self.assertRaises(Exception):
            self.licuadora.set_velocidad(1)

    def test_error_velocidad_invalida(self):
        self.licuadora.encender()
        with self.assertRaises(ValueError):
            self.licuadora.set_velocidad(0)

if __name__ == '__main__':
    unittest.main()
