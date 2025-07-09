# This file contains the description of the "Simulator" class
# first version in python2, by R.Marcelin-Jimenez (11.11.10)
# python3-style getters by I.Martinez-Vargas (27.09.20)

""" An instance of "Simulator" represents the engine that moves the experiment
enabling the communication between processes, enforcing the causal order of the
exchanged events. """

# -----------------------------------------#---------------------------------------------
class Simulator:                           # Descends from "Object" (default)
    """ Simulator attributes: "clock" & "agenda", 
    contains constructor and getters in python3-style, as well as the 
    methods "insertEvent()", "returnEvent()" & "isOn()". """
	
    def __init__(self, lastmoment):
        """ Builds an instance of "Simulator", sets the initial value of clock 
        and inserts the extreme (fixed) positions of agenda. """
        self.__clock = 0.0
        self.__agenda = [[-1.0],[lastmoment+0.1]]
		
    @property
    def clock(self):
        """ Invoke as x.clock, without "()". """
        return self.__clock

    @property
    def agenda(self):
        """ Invoke as x.genda, without "()". """
        return self.__agenda
    
    def insertEvent(self, event):
        """ Inserts an event in the agenda (list) in ascending order, according 
        to its attribute of time. The extrem values of agenda are fixed to avoid 
        special cases. """
        key=event.time
        newitem = [key, event]
        for i,item in enumerate(self.__agenda):
            if key < item[0]: 
                self.__agenda.insert(i,newitem)
                break
    
    def returnEvent(self):
        """ Returns the 2nd position of the agenda. Notice that this element or item
         is, in turn, a list of 2 elements: key and event. """
        item = self.__agenda.pop(1)
        return item[1]

    def isOn(self):
        """ True, provided that there are more that 2 elements in the agenda. """
        return len(self.__agenda)>2
