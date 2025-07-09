# This file contains the description of the "Simulation" class
# first version in python2, by R.Marcelin-Jimenez (11.11.10)
# support of concurrent algorithms using port number by R.Marcelin-Jimenez (27.09.20)
# support of weighted graphs by M.Lopez-Chavira (27.09.20)
# python3-style getters by I.Martinez-Vargas (27.09.20)
# detection of empty lines in input file by I.Martinez-Vargas (27.09.20)

""" An instance of "Simulation" represents an experiment in which a distributed
algorithm (or several) is (are) executed on top of a network.  """

from process import Process                # to build the table of active entities
from simulator import Simulator            # the definition of the engine
import re                                  # regular expressions library
# -----------------------------------------#---------------------------------------------
class Simulation:                          # Descends from "Object" (default)
    """ Simulation attributes: "engine", "graph", "weights" & "table", 
    contains constructor and getters in python3-style, as well as the 
    methods "setModel()", "insertEvent()" & "run()". """

    def __init__(self, filename, maxtime):
        """ Builds an instance of "Simulation", including its events engine, the 
        underlying network, the weights of the links & the table of processes. """
 
        emptyline = re.compile('\n')
        self.__numnodes = 0  # <-- Contador
        self.__engine = Simulator(maxtime)

        f = open(filename)
        lines = f.readlines()
        f.close()
        self.__graph = []
        self.__weights = []
        for line in lines:
            fields = line.split()
            neighbors = []
            nweight = []
            if not emptyline.match(line): # <-- Revisa
                self.__numnodes += 1      # <-- Aumenta contador
                for f in fields:
                    subf = f.split(",")
                    if len(subf) == 1:
                        neighbors.append(int(f))
                        nweight.append(1)
                    elif len(subf) == 2:
                        neighbors.append(int(subf[0]))
                        nweight.append(int(subf[1]))
                self.__graph.append(neighbors)
                self.__weights.append(nweight)

        self.__table  = [[]]          # la entrada 0 se deja vacia
        for i,row in enumerate(self.__graph):
            newprocess = Process(row, self.__weights[i], self.__engine, i+1)
            self.__table.append(newprocess)
 
    @property
    def engine(self):
        return self.__engine

    @property
    def graph(self):
        return self.__graph

    @property
    def table(self):
        return self.__table

    @property
    def numnodes(self): 
        return self.__numnodes
        
    def setModel(self, model, id, port=0):
        """ asocia al proceso con el modelo que debe ejecutar y viceversa """
        process = self.__table[id]
        process.setModel(model, port)
 		
    def init(self, event):
        """ inserta un evento semilla en la agenda """
        self.__engine.insertEvent(event)

    def run(self):	
        """ arranca el motor de simulacion """
        while self.__engine.isOn():
            nextevent = self.__engine.returnEvent()
            target = nextevent.target 
            time = nextevent.time
            port = nextevent.port
            nextprocess = self.__table[target]
            nextprocess.setTime(time, port)
            nextprocess.receive(nextevent, port)
