```mermaid
sequenceDiagram
    participant a as "experiment: Simulation"
    participant b as "engine: Simulator"
    participant c as "agenda: List"
    participant d as "nextEv: Event"
    participant e as "processTable: List"
    participant f as "nextProc: Process"
    participant g as "myModel: Model"

    activate a
    a->>+b: hola()
    b->>+c: hola()
    c-->>-b: adios()
    b-->>-a: adios()
    a->>+d: hola()
    d-->>-a: adios()
    a->>+e: hola()
    e-->>-a: adios()

    a->>+f: hola()
    a->>f: quetal()
    f->>+g: hola()
    g-->>-f: adios()

    activate b
    f-->>-b: adios()
    deactivate b
    deactivate a
