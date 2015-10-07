from Persona import Persona


class Villano(Persona):
    """Clase villano, que hereda de persona"""
    def __init__(self):
        self.name = ""
        self.villanos_conocidos = []
        self.recompensa = 0
        self.vidas = 0
        self.es_chivato = False
        self.distancia = 0
        self.puntuacion = 0

    def set_recompensa(self,recompensa):
        self.recompensa = recompensa

    def get_recompensa(self):
        return self.recompensa

    def set_vidas(self,vidas):
        self.vidas = vidas

    def get_vidas(self):
        return self.vidas

    def set_es_chivato(self,es_chivato):
        self.es_chivato = es_chivato

    def get_es_chivato(self):
        return self.es_chivato

    def set_distancia(self,distancia):
        self.distancia = distancia

    def get_distancia(self):
        return self.distancia
