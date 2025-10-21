```mermaid
classDiagram
    direction LR

    class engine{
    is a Simulator
    }
    
    class experiment{
    is a Simulation
    }

    class process{
    is a Process
    }

    class model{
    is a Model
    }

    class event{
    is an Event
    }

    class tabla{
    is a List
    }

    class graph{
    is a List
    }

    class neighbourhood{
    is a List
    }

    class agenda{
    is a List
    }


    experiment --|> engine : "has one"
    experiment --|> graph: "has one"
    experiment --|> tabla : "has one"
    tabla --|> process : "has"
    process --|> model : "associated to"
    process --|> engine : "schedules event in"
    model --|> process : "associated to"
    model --|> neighbourhood: "has one"
    engine --|> agenda: "has one"
    graph --|> neighbourhood: "has"
    agenda --|> event: "has"





