# 🧮 Calculadora Básica en Consola con Python

Este proyecto es una calculadora interactiva por consola desarrollada en Python. Permite realizar operaciones matemáticas básicas como **suma**, **resta**, **multiplicación** y **división**, con una interfaz de usuario mejorada visualmente gracias a la librería `colorama`.

---

## 🚀 Funcionalidades

- Menú interactivo para seleccionar operaciones.
- Admite tanto **números enteros** como **decimales**.
- Validación de entradas numéricas.
- Manejo de errores comunes como la **división por cero**.
- Resultados mostrados con formato adaptativo (por ejemplo, `5 + 2 = 7`, pero `5 + 2.5 = 7.5`).
- Interfaz colorida y amigable con `colorama`.
- Permite realizar múltiples operaciones en un mismo flujo.

---

## 📦 Instalación

1. Asegurate de tener **Python 3.6 o superior** instalado. Para comprobarlo, ejecutá en la consola:

```bash
python --version
```

2. Cloná el repositorio o descargá el archivo `calculator.py`.
3. Instalá la dependencia `colorama` ejecutando en la consola:

```bash
pip install colorama
```

4. Ejecutá el script:

```bash
python calculator.py
```

---

## 🎨 ¿Qué es `colorama` y para qué se utiliza?

[`colorama`](https://pypi.org/project/colorama/) es una librería de Python que permite agregar **colores y estilos al texto** mostrado en la terminal, de forma compatible con sistemas operativos como Windows, Linux y macOS.

### En este proyecto, `colorama` se usa para:

- Resaltar el **menú de opciones**.
- Diferenciar **mensajes informativos, errores y resultados**.
- Mejorar la experiencia del usuario al hacer la interfaz más clara y visualmente agradable.

Ejemplo visual:

- `Opción inválida` se muestra en rojo.
- `Resultado:` se muestra en azul.
- `Menú de opciones:` en cian.

---

## 🧠 Conclusión

Se logró utilizar las estructuras de datos aprendidas en Programacion 1 aplicadas a un caso real:

- Uso de estructuras de control (`if`, `while`).
- Validación de entradas del usuario.
- Creación de funciones reutilizables.
- Manejo de errores (`try-except`, división por cero).
- Interacción por consola.
- Integración de librerías externas como `colorama`.
  Además, al mostrar los resultados con formato adaptativo (entero o decimal según corresponda), mejora la claridad sin perder precisión.

---

## Autores

Desarrollado por **Kevin Gastaldello** y **Franco Ghilardi**.

---

## Profesor y tutor

- Profesor de la comision 14 de Arquitectura y Sistemas Operativos **Diego Lobos**.
- Tutor de la comision 14 de Arquitectura y Sistemas Operativos **Nicolas Carcaño**.

---
