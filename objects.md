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

    class algorithm{
    is a Model
    }

    class event{
    is an Event
    }

    class table{
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


    experiment --|> engine : has one
    experiment --|> graph: has one
    experiment --|> table : has one
    table --|> process : has
    process --|> algorithm : associated to
    process --|> engine : schedules event in
    algorithm --|> process : associated to
    algorithm --|> neighbourhood: has one
    engine --|> agenda: has one
    graph --|> neighbourhood: has
    agenda --|> event: has





