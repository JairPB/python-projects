# Python Exercises - Colección de Proyectos de Aprendizaje

Repositorio de ejercicios prácticos en Python que demuestra competencia en programación fundamenta, análisis de datos, lógica de algoritmos y validación de información. Este proyecto forma parte de mi formación en desarrollo de software.

---

## 📋 Descripción General del Proyecto

Este repositorio contiene una serie de pequeños proyectos Python enfocados en:
- **Estructuras de datos y algoritmos**: Optimización de soluciones y análisis de complejidad
- **Aplicaciones interactivas**: Desarrollo de programas con interfaz de usuario
- **Ciencia de datos**: Integración con APIs externas y visualización de información
- **Validación y procesamiento de datos**: Implementación de patrones de validación

---

## 🚀 Proyectos Incluidos

### 1. **Rock Paper Scissors** (`rock-paper-scissors.py`)

**Descripción:**
Implementación de un juego clásico de piedra, papel o tijeras contra la computadora. El programa gestiona puntuaciones acumulativas y continúa hasta que el usuario decide salir.

**Características principales:**
- Interfaz interactiva por línea de comandos
- Sistema de puntuación persistente durante la sesión
- Validación de entradas del usuario
- Lógica de decisión basada en selecciones aleatorias

**Conceptos aplicados:**
- Bucles condicionales (`while`, `if-elif-else`)
- Módulo `random` para selecciones no determinísticas
- Gestión de estado (variables de puntuación)
- Validación de entrada de usuario

**Tecnologías:** Python 3, módulo `random`

---

### 2. **Visualización de Datos Meteorológicos** (`get-data.py`)

**Descripción:**
Script que obtiene datos de pronóstico del clima de los últimos 7 días para una ubicación específica, realiza procesamiento de datos y genera visualizaciones, almacenando los resultados en CSV.

**Características principales:**
- Consumo de API REST (Open-Meteo) para obtener datos de temperatura
- Procesamiento y transformación de datos con pandas
- Generación de gráficos comparativos con matplotlib
- Persistencia de datos en formato CSV
- Manejo de fechas y rangos de tiempo

**Conceptos aplicados:**
- Requests HTTP para integración con APIs externas
- DataFrames de pandas para manipulación de datos tabulares
- Visualización de series de tiempo
- Manejo del sistema de archivos
- Fechas y operaciones de tiempo

**Tecnologías:** Python 3, `requests`, `pandas`, `matplotlib`

---

### 3. **Validador de Datos** (`valid-data.py`)

**Descripción:**
Sistema de validación de información implementado mediante programación orientada a objetos. Valida correos electrónicos y rangos de edad, acumulando errores para su posterior análisis.

**Características principales:**
- Clase `DataValidator` con múltiples métodos de validación
- Validación de formato de correo electrónico
- Validación de rango válido de edades (0-150)
- Sistema de registro de errores
- Capacidad de procesar múltiples validaciones secuencialmente

**Conceptos aplicados:**
- Programación Orientada a Objetos (clases e instancias)
- Métodos de clase y atributos de instancia
- Validación de datos
- Manejo de errores mediante listas de acumulación
- Encapsulación de lógica de validación

**Tecnologías:** Python 3, OOP

---

## 📚 Ejercicios de Algoritmos (Archivos de Notas)

Estos archivos contienen soluciones y análisis profundo de problemas clásicos de programación:

### **Buy and Sell Stock** (`excercises_notes/buy_sell_stock.txt`)
Problema de optimización: Determinar la máxima ganancia posible al comprar y vender una acción una única vez.

**Conceptos clave aprendidos:**
- Patrón de seguimiento de variables ("tracking pattern")
- Algoritmos de una sola pasada (one-pass algorithms)
- Optimización de espacio: O(n) tiempo, O(1) espacio
- Pensamiento estratégico en resolución de problemas

---

### **Two Sum** (`excercises_notes/two_sum.txt`)
Problema clásico de búsqueda: Encontrar dos números en un arreglo que sumen un valor objetivo.

**Conceptos clave aprendidos:**
- Uso de diccionarios para búsqueda eficiente
- La estrategia del "complemento" para reducir complejidad
- Comparación temporal: Fuerza bruta O(n²) vs Diccionario O(n)
- Iteración eficiente con `enumerate()`
- Optimización de uso de memoria

---

### **Merge Sorted Linked Lists** (`excercises_notes/nodes.txt`)
Problema de estructuras de datos: Fusionar dos listas enlazadas ordenadas en una sola lista ordenada.

**Conceptos clave aprendidos:**
- Estructura de datos: Linked Lists (nodos y referencias)
- El patrón "dummy node" para simplificar lógica
- Inicializadores (`__init__`) en clases
- Manipulación de referencias entre nodos
- Estrategias de dos punteros (two-pointer technique)

---

## 📊 Datos Incluidos

### `data/paris_weather.csv`
Dataset generado por `get-data.py` contiene:
- **date**: Fecha del registro
- **max_temp**: Temperatura máxima en °C
- **min_temp**: Temperatura mínima en °C

---

## 🛠️ Configuración del Proyecto

### Requisitos
- **Python:** ≥ 3.14
- **Dependencias externas:**
  - `pandas` - Manipulación y análisis de datos
  - `matplotlib` - Visualización de gráficos
  - `requests` - Llamadas HTTP a APIs

### Instalación
```bash
# Clonar o descargar el repositorio
cd python-exercises

# (Opcional) Crear un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install pandas matplotlib requests
```

### Ejecución de Proyectos
```bash
# Juego de piedra, papel o tijeras
python rock-paper-scissors.py

# Obtener y visualizar datos meteorológicos
python get-data.py

# Ejecutar validador de datos
python valid-data.py

# Script principal
python main.py
```

---

## 💡 Habilidades Demostradas

| Habilidad | Proyecto | Descripción |
|-----------|----------|-------------|
| **Lógica condicional** | Rock Paper Scissors | Control de flujo complejo con múltiples condiciones |
| **APIs REST** | Visualización Meteorológica | Integración con servicios web externos |
| **Manipulación de datos** | Visualización Meteorológica | Transformación y limpieza de datos con pandas |
| **Visualización** | Visualización Meteorológica | Generación de gráficos profesionales |
| **POO** | Validador de Datos | Diseño de clases y métodos de instancia |
| **Validación** | Validador de Datos | Lógica de negocio y manejo de errores |
| **Algoritmos** | Archivos de notas | Análisis y optimización de soluciones |
| **Estructuras de datos** | Archivos de notas | Uso eficiente de diccionarios y listas enlazadas |

---

## 📈 Próximos Pasos y Extensiones

- [ ] Implementar interfaz gráfica (tkinter/PyQt) para Rock Paper Scissors
- [ ] Agregar persistencia de puntuaciones en base de datos
- [ ] Expandir validador con más reglas de negocio
- [ ] Implementar completos del problema de algoritmos (Two Sum, Buy-Sell Stock, etc.)
- [ ] Agregar pruebas unitarias (pytest)
- [ ] Documentación API completa

---

## 👨‍💻 Autor

Jair Perez  
Portfolio de ejercicios prácticos - Formación en Desarrollo de Software

---

## 📝 Notas Finales

Este proyecto refleja mi dedicación al aprendizaje práctico de programación en Python, combinando ejercicios fundamentales con aplicaciones del mundo real. Cada proyecto ha sido desarrollado con el objetivo de dominar conceptos clave y mejores prácticas de desarrollo.
