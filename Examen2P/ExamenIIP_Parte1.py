import math

class Figura:
    def __init__(self, radio):
        self.radio = radio

    def AreaCirculo(self):
        area_circulo = (2 * math.pi * self.radio)
        print("Area del Circulo: ",area_circulo)

    def AreaEsfera(self):
        area_esfera = (4 * math.pi) * (self.radio)**2
        print("Area de la Esfera: ",area_esfera)

    def VolumenEsfera(self):
        volumen_esfera = (4/3) * (math.pi) * (self.radio)**3
        print("Volumen de la Esfera: ",volumen_esfera)

    def Calcular(self):
        figura = input("Ingrese el tipo de figura (circulo, esfera): ")
        radio = float(input("Ingrese el radio: "))

        calcular = Figura(radio)

        if(figura == 'circulo'):
            calcular.AreaCirculo()
        elif(figura == 'esfera'):
            calcular.AreaEsfera()
            calcular.VolumenEsfera()