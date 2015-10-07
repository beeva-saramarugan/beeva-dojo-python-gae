from Persona import Persona


class Chivato(Persona):
    """Clase chivato, que hereda de persona"""
    def __init__(self):
        self.name = ""
        self.villanos_conocidos = []

    def set_villanos(self,villanos_conocidos):
        self.villanos_conocidos = villanos_conocidos

    def get_villanos(self):
        return self.villanos_conocidos
