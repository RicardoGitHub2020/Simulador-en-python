# This file contains the description of the "Model" class
# first version in python2, by R.Marcelin-Jimenez (11.11.10)
# support of concurrent algorithms using multiports by R.Marcelin-Jimenez (27.09.20)
# support of weighted graphs by M.Lopez-Chavira (27.09.20)
# python3-style getters by I.Martinez-Vargas (27.09.20)

""" You can not generate a direct instance of this class. Instead you have to
create a descendant where those methods labeled as abstracts must be implemented.
This is the mechanism to program a particular application, i.e. a concrete 
algorithm. A process is in charge of information exchange, but it relies on its
algorithm(s) to deploy the intended behavior. Each model is associated to a unique
port, but all the models living at the same node share the id of their only process.  """

from abc import ABCMeta, abstractmethod

# -----------------------------------------#---------------------------------------------
class Model:                               # Descends from "Object" (default)
    """ Model attributes: "clock", "process", "neighbors", "weights", "id" & "port", 
    contains constructor and getters in python3-style, as well as the 
    methods "setTime()", "setProcess()", "(abstract) init()" & "(abstract) receive()". """

    __metaclass__ = ABCMeta
    def __init__(self):
        """ Sets the initial value of its local clock. """
        self.__clock = 0.0
		
    def setTime(self, time):
        """ Updates the value of the local clock. """
        self.__clock = time
		
    def setProcess(self, process, neighbors, weights, id, port=0):
        """ asocia al modelo con su entidad activa (proceso), su lista 
        de vecinos y su identificador """
        self.__process = process
        self.__neighbors = neighbors        
        self.__weights = weights
        self.__id = id
        self.__port = port

    @property
    def clock(self):
        return self.__clock

    @property
    def process(self):
        return self.__process

    @property
    def neighbors(self):
        return self.__neighbors

    @property
    def weights(self):
        return self.__weights

    @property
    def id(self):
        return self.__id

    @property
    def port(self):
        return self.__port

    def transmit(self, event):
        """ invoca el metodo de transmision de su entidad activa (proceso) """
        self.__process.transmit(event)

    def up(self, event):
        """ invoca el metodo de transmision de su entidad activa (proceso) """
        self.__process.up(event, self.port)

    def down(self, event):
        """ invoca el metodo de transmision de su entidad activa (proceso) """
        self.__process.down(event, self.port)

    @abstractmethod
    def init(self):
        """ Que se inicializa? eso se define en la aplicacion """
        pass

    @abstractmethod
    def receive(self, event):
        """ Que se hace con un evento recibido desde una capa inferior? eso se define la aplicacion """
        pass

    @abstractmethod
    def send(self, event):
        """ Que se hace con un evento recibido desde una capa superior? eso se define la aplicacion """
        pass