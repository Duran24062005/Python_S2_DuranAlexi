# HomeWork 2 Día 9 Persistencia en Datos con Json

## Resumen

LimeWire desea implementar un sistema integral de gestión que permita manejar todas las operaciones
relacionadas con la administración de datos de artistas musicales, países, géneros musicales, así como la
generación de informes relevantes.

Especificaciones (Funcionalidades):
A continuación se muestra una propuesta para los archivos JSON a construir:

## Artistas

- JSON propuesto

```cmd
Datos en la ruta /db/datos.json
```
El programa debe realizar, desde un/unos archivo/s JSON almacenado, la gestión de la siguiente información:

### Gestión de Datos de Artistas Musicales:

Artistas: El sistema debe permitir registrar cada dato de artistas musicales con la siguiente información:

- Nombre del artista.
- País de origen (nombre, código ISO3).
- Años de actividad.
- Año de lanzamiento del primer disco que llegó a las listas.
- Género musical.
- Unidades certificadas totales.
- Ventas reclamadas.
- Estado del artista (si está activo o no).

### Interacción con Países y Géneros Musicales:

Países: Registro y gestión de la información de los países incluyendo:

- Nombre del país.
- Código ISO del país.
- Código ISO3 del país.

### Géneros Musicales: Registro y gestión de la información de los géneros musicales incluyendo:

- ID del género.
- Descripción del género.

### Generación de Informes:
Informes de artistas: Listado de todos los datos de artistas musicales para un país específico en un período de
tiempo específico, incluyendo detalles de años de actividad y unidades certificadas. Informes de ventas
musicales: Listado de las unidades certificadas y ventas reclamadas año a año para un artista específico.

### Módulo de Reportes:

El módulo de reportes debe generar las siguientes solicitudes:
1. Obtener todos los datos de artistas musicales para Reino Unido desde 1960 hasta 1970.
2. Datos de artistas musicales para el género 'Rock/pop’
3. Obtener los datos de artistas musicales de los últimos 10 años para todos los países.
4. Número de registros de artistas por año.
5. Unidades certificadas totales registradas para todos los países en 2023.