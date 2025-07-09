# This file contains the description of the "Event" class
# first version in python2, by R.Marcelin-Jimenez (11.11.10)
# port number by R.Marcelin-Jimenez (27.09.20) 
# python3-style getters by I.Martinez-Vargas (27.09.20)

""" An instance of "Event" encapsulates the information exchanged between the
active entities (processes) of a distributed system. """

# -----------------------------------------#---------------------------------------------
class Event:                               # Descends from "Object" (default)
    """ Event attributes: "name", "time", "target", "source", & "port", 
    contains constructor and getters in python 3 style. """
    
    def __init__(self, name, time, target, source, port=0):
        """ Builds an instance of "Event". """
        self.__name = name
        self.__time = time
        self.__target = target
        self.__source = source
        self.__port = port

    @property
    def name(self):
        """ Invoke as x.name, without "()". """
        return self.__name

    @property
    def time(self):
        """ Invoke as x.time, without "()". """
        return self.__time

    @property
    def target(self):
        """ Invoke as x.target, without "()". """
        return self.__target

    @property
    def source(self):
        """ Invoke as x.source, without "()". """
        return self.__source

    @property
    def port(self):
        """ Invoke as x.port, without "()". """
        return self.__port
