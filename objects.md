```mermaid
classDiagram
    direction LR

    class Simulator{

    }
    
    class Simulation{

    }

    class Process{

    }

    class Model{

    }

    class Event{

    }

    class ProcessList{

    }

    class NeighboursList{

    }

    class Neighbourhood{

    }

    class EventList{

    }


    Simulation --|> Simulator : "tiene una"
    Simulation --|> NeighboursList : "tiene una"
    Simulation --|> ProcessList : "tiene una"
    ProcessList --|> Process : "contiene"
    Process --|> Model : "asociado con"
    Process --|> Simulator : "inserta evento en "
    Model --|> Process : "asociado con"
    Model --|> Neighbourhood: "tiene una"
    Simulator --|> EventList: "tiene una"
    NeighboursList --|> Neighbourhood: "contiene"
    EventList --|> Event: "contiene"





