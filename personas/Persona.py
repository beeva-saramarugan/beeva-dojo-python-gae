class Persona(object):
    """Clase persona"""
    def __init__(self):
        self.nombre = ""

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name