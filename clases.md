```mermaid
classDiagram
    Persona <|-- Alumno
    Persona <|-- Profesor
    Persona <|-- Administrativo
    Persona : + edad
    Persona : + nombre
    Persona: + {abstract} actividad() 
    class Alumno{
      +actividad()
    }
    class Profesor{
      +actividad()
    }
    class Administrativo{
      +actividad()
    }
