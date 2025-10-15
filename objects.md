```mermaid
objectDiagram
    object libro1 : Libro
    libro1 : titulo = "Cien años de soledad"
    libro1 : autor = "Gabriel García Márquez"
    libro1 : estaDisponible = false

    object prestamo1 : Prestamo
    prestamo1 : fechaPrestamo = "2025-10-14"
    prestamo1 : fechaVencimiento = "2025-10-28"

    object socio1 : Socio
    socio1 : nombre = "Ana Pérez"
    socio1 : idSocio = "SP-001"
    socio1 : numPrestamos = 1

    libro1 -- prestamo1 : "es_prestado_en"
    socio1 -- prestamo1 : "toma_prestado"
