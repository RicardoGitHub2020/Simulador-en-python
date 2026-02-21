```mermaid
classDiagram
    direction LR

    class coordinator{
    is a Scheduler
    }
    
    class experiment{
    is a Simulation
    }

    class process{
    is a Process
    }
    note for process "is the active entity in charge of a node"

    class algorithm{
    is a Model
    }

    class event{
    is an Event
    }

    class table{
    is a List
    }
    note for table "there is a process in table for each node in graph"
 
    class graph{
    is a List
    }
    note for graph "each entry contains the neighbours of node i, i in [1, ..., N]"

    class neighbourhood{
    is a List
    }

    class agenda{
    is a List
    }
    note for agenda "contains events ordered by time"

    experiment --|> coordinator : has one
    experiment --|> graph: has one
    experiment --|> table : has one
    table --|> process : has
    process --|> algorithm : associated to
    process --|> coordinator : schedules events invoking
    algorithm --|> process : associated to
    algorithm --|> neighbourhood: has one
    coordinator --|> agenda: has one
    graph --|> neighbourhood: has
    agenda --|> event: has





