```mermaid

sequenceDiagram
    actor Cliente
    participant Servidor

    Cliente->>+Servidor: login(usuario, password)
    Note right of Servidor: Validando credenciales
    Servidor-->>-Cliente: 200 OK
