# Student Management System

Este proyecto tiene como objetivo gestionar un sistema de estudiantes, permitiendo registrar, buscar, actualizar, eliminar estudiantes y generar informes sobre su desempeño académico. Es ideal para escuelas o instituciones educativas que deseen llevar un control eficiente de los estudiantes.

## Funcionalidades

El sistema ofrece las siguientes funcionalidades clave:

1. **Registrar un estudiante**: Permite registrar nuevos estudiantes con información como nombre, edad, grado, promedio y año de ingreso.

2. **Buscar un estudiante**: Permite buscar estudiantes por nombre o grado. La búsqueda es insensible a mayúsculas/minúsculas.

3. **Actualizar un estudiante**: Permite actualizar el grado o el promedio de un estudiante registrado.

4. **Eliminar un estudiante graduado**: Permite eliminar estudiantes que ya se han graduado. Para ello, se confirma la acción antes de proceder.

5. **Generar informes**: Genera dos tipos de informes:
    - Promedio de notas por nivel de grado.
    - Estudiantes destacados (promedio >= 9).

6. **Menú interactivo**: Ofrece una interfaz de usuario interactiva en la consola para realizar diversas operaciones con los estudiantes.

## Cómo funciona

El sistema mantiene una lista de diccionarios (`students`), donde cada diccionario contiene los detalles de un estudiante. Cada estudiante tiene los siguientes atributos:

- **name**: Nombre del estudiante.
- **age**: Edad del estudiante.
- **grade**: Grado o nivel de educación del estudiante (1-12).
- **average**: Promedio de calificaciones del estudiante (0-10).
- **year_of_entry**: Año de ingreso del estudiante.

Las funciones principales del sistema permiten:

- **preload_students**: Inicializa la lista de estudiantes con algunos datos predeterminados.

- **register_student**: Permite registrar un nuevo estudiante validando que la edad y el promedio sean valores válidos.

- **search_student**: Permite buscar estudiantes por nombre o grado.

- **update_student**: Permite actualizar el grado o el promedio de un estudiante.

- **delete_graduate**: Permite eliminar un estudiante graduado después de confirmar la acción.

- **generate_reports**: Genera un informe con el promedio de notas por grado y una lista de estudiantes con un promedio superior o igual a 9.

- **menu**: Muestra un menú interactivo donde el usuario puede seleccionar qué operación realizar.

## Uso

### Requisitos

Este proyecto requiere Python 3.x para ejecutarse correctamente.

### Ejecución

1. Clona o descarga este repositorio.
2. Ejecuta el archivo `student_management.py` en tu terminal o entorno de desarrollo Python.
3. El sistema mostrará un menú interactivo en la consola donde podrás elegir entre las diferentes opciones para gestionar los estudiantes.

### Ejemplo de flujo

1. **Registrar un estudiante**:
   - El usuario ingresa los detalles del estudiante (nombre, edad, grado, promedio y año de ingreso), y el estudiante se registra en el sistema.

2. **Buscar un estudiante**:
   - El usuario puede buscar estudiantes por nombre o grado, y se mostrarán los resultados coincidentes.

3. **Actualizar un estudiante**:
   - El usuario puede actualizar el grado o el promedio de un estudiante específico en el sistema.

4. **Eliminar un estudiante graduado**:
   - El usuario puede eliminar un estudiante graduado (un estudiante de grado 12) después de confirmar la eliminación.

5. **Generar informes**:
   - El sistema muestra el promedio de las calificaciones por grado y una lista de estudiantes destacados con un promedio de 9 o más.

## Objetivo

El objetivo de este proyecto es proporcionar una solución sencilla y efectiva para gestionar la información de estudiantes. Permite a las instituciones educativas realizar un seguimiento de los datos académicos de sus estudiantes de manera organizada y eficiente.

## Contribuciones

Si deseas contribuir al proyecto, puedes hacer un fork y enviar un pull request. Las mejoras y sugerencias son siempre bienvenidas.
