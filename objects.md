```mermaid
classDiagram
    direction LR

    class Pedido{
        id_pedido: 101
        fecha: 2025-10-15
        estado: "Enviado"
    }
    
    class Producto{
        nombre: "Teléfono Móvil"
        precio: 500
        cantidad: 1
    }

    class Cliente{
        nombre: "Juan Pérez"
        id_cliente: 12345
    }

    class Factura{
        id_factura: 789
        monto: 500
        fecha: 2025-10-15
    }

    Cliente --|> Pedido : "realiza"
    Pedido "1" -- "1" Producto : "contiene"
    Pedido --|> Factura : "genera"
