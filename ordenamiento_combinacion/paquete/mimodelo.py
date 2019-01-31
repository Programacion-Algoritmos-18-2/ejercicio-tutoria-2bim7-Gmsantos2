class Persona(object):
    """docstring for Persona"""
    def __init__(self,edad):
        '''
        self.nombre = nombre  #variables inicializadas en el init
        self.apellido = apellido
        '''
        self.edad = int(edad)
    '''
    def set_nombre(self,nombre): #metodos set y get (en este caso solo ocuparemos el de edades)
        self.nombre = nombre
    def get_nombre(self):
        return self.nombre

    def set_apellido(self,apellido):
        self.apellido = apellido
    def get_apellido(self):
        return self.apellido
    '''

    def set_edad(self,edad):
        self.edad = int(edad)
    def get_edad(self):
        return self.edad

    def __str__(self):   #metodos  to string
    	return "%d" % (self.get_edad())

    def __repr__(self):
        return "%d" % (self.get_edad())

		