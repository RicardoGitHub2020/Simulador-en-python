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
    a->>+b: self.engine.returnEvent()
    b->>+c: self.agenda.pop()
    c-->>-b: return item
    b-->>-a: return nextEv
    a->>+d: nextEv.target()
    d-->>-a: return self.target
    a->>+e: nextProc = self.table[target]
    e-->>-a: return nextProc

    a->>+f: nextProc.setTime(nextEv.time)
    a->>f: nextProc.receive(nextEv)
    f->>+g: receive(nextEv)
    g-->>-f: transmit(newEv)

    activate b
    f-->>-b: self.engine.insertEvent(newEv)
    deactivate b
    deactivate a
