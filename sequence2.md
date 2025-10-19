```mermaid
sequenceDiagram
    participant u as "usuario: Cliente"
    participant g as "gestor: CuentaBancaria"

    u->>g: depositar(100)
    activate g
    g-->>u: saldoActualizado()
    deactivate g
