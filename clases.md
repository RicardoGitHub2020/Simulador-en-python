```mermaid
classDiagram
    Persona <|-- Alumno
    Persona <|-- Profesor
    Persona <|-- Administrativo
    Persona : + edad
    Persona : + nombre
    Persona: +actividad() {abstract}
    class Alumno{
      +String beakColor
      +swim()
      +quack()
    }
    class Profesor{
      -int sizeInFeet
      -canEat()
    }
    class Administrativo{
      +bool is_wild
      +run()
    }
