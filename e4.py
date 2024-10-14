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


mi_licuadora = Licuadora()

mi_licuadora.encender()  # Enciende la licuadora
mi_licuadora.set_velocidad(2)  # Establece la velocidad en 2 (50 rpm)
mi_licuadora.set_temporizador(5)  # Establece el temporizador en 5 segundos
mi_licuadora.iniciar()  # Inicia el proceso de la licuadora

