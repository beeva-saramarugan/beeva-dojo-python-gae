from Persona import Persona


class Chivato(Persona):
    """Clase chivato, que hereda de persona"""
    def __init__(self):
        self._villanos_conocidos = []

    def set_villanos(self, villanos_conocidos):
        self._villanos_conocidos = villanos_conocidos

    def get_villanos(self):
        return self._villanos_conocidos
