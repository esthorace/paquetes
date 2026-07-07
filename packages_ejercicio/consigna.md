# Consigna de ejercicio

## Paquete  

Crear un paquete llamado `clientes`

## Módulos del paquete

Crear 2 módulos para el paquete:

- **`datos`**: contiene el diccionario variable base_datos

- **`busqueda`**: contiene una función que recibe el nombre de un cliente, itera sobre la lista de clientes, y si el parámetro existe en la lista, entonces devolver el nombre del cliente, de lo contrario devolver None.

## Script principal

Crear un script principal llamado **`app`**. Debe contener importaciones correspondientes. Una función `main()` que pregunte al usuario el nombre de un cliente a buscar. Si el cliente es encontrado, mostrar su nombre, de lo contrario, mostrar "Cliente no encontrado".

## Diagramas

### 1. Estructura del Proyecto (Módulos y Paquete)

Este diagrama muestra cómo se relacionan el script principal, los módulos y los datos dentro del paquete clientes.

```mermaid
graph TD
    subgraph Paquete: clientes
        M_Datos[Módulo: datos] -->|Contiene| BD[(Diccionario: base_datos)]
        M_Busqueda[Módulo: busqueda]
    end

    App[Script: app] -.->|Importa| M_Busqueda
    M_Busqueda -.->|Consulta| BD
```

### 2. Diagrama de flujo: Función de Búsqueda (Módulo busqueda)

Representa la lógica interna de la función que busca al cliente dentro de la base de datos.

```mermaid
flowchart TD
    A([Inicio: funcion_busqueda]) --> B{¿Quedan clientes en la lista?}
    
    B -- Sí --> C[Leer el siguiente cliente de la lista]
    C --> D{¿El nombre del cliente coincide?}
    
    D -- Sí --> E([Retornar: nombre del cliente])
    D -- No --> B
    
    B -- No --> F([Retornar: None])
```

### 3. Diagrama de flujo: Script Principal (Script app - Función main)

Representa la interacción con el usuario y cómo se maneja el resultado devuelto por el módulo de búsqueda.

```mermaid
flowchart TD
    Inicio([Inicio: main]) --> Ingreso[/Nombre del cliente/]
    Ingreso --> Llamada[Llamar a funcion_busqueda]
    Llamada --> Evaluacion{¿Resultado es diferente de 'None'?}
    
    Evaluacion -- Sí, se encontró --> MostrarExito[/Imprimir: Nombre del cliente/]
    Evaluacion -- No, devolvió 'None' --> MostrarError[/Imprimir: 'Cliente no encontrado'/]
    
    MostrarExito --> Fin([Fin])
    MostrarError --> Fin
```