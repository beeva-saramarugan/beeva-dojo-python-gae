from Persona import Persona


class Villano(Persona):
    """Clase villano, que hereda de persona"""
    def __init__(self):
        self._villanos_conocidos = []
        self._recompensa = 0
        self._vidas = 0
        self._es_chivato = False
        self._distancia = 0

    def set_recompensa(self, recompensa):
        self._recompensa = recompensa

    def get_recompensa(self):
        return self._recompensa

    def set_vidas(self, vidas):
        self._vidas = vidas

    def get_vidas(self):
        return self._vidas

    def set_es_chivato(self, es_chivato):
        self._es_chivato = es_chivato

    def get_es_chivato(self):
        return self._es_chivato

    def set_distancia(self, distancia):
        self._distancia = distancia

    def get_distancia(self):
        return self._distancia
