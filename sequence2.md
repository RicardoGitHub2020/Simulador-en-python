```mermaid
sequenceDiagram
    participant a as "experiment: Simulation"
    participant b as "engine: Simulator"
    participant c as "agenda: List"
    participant d as "nextEv: Event"
    participant e as "processTable: List"
    participant f as "nextProc: Process"
    participant g as "myModel: Model"

    a->>b: depositar(100)
    activate b
    b-->>a: saldoActualizado()
    deactivate b
