# Sistema Básico de Biblioteca en Python

## Descripción
Programa simple que simula una biblioteca pequeña para demostrar el uso de:

- **Constructores** (`__init__`): inicializan objetos con datos obligatorios, opcionales y estado inicial.
- **Destructores** (`__del__`): ejecutan acciones de limpieza cuando un objeto ya no es referenciado (cierre de archivos, registro de eventos, mensajes de finalización, etc.).

El sistema incluye tres entidades principales:
- `Libro`
- `Usuario`
- `Prestamo` (con manejo de archivo de log para evidenciar limpieza en el destructor)

Utiliza arquitectura básica **Modelos / Servicios** separando responsabilidades.

