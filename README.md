# Actividad-evaluable-equipo1-T1

# 🌌 Galaxy Defenders

Un simple shooter arcade 2D creado en Python y Pygame. Este proyecto sirve como ejemplo de un flujo de trabajo colaborativo para un equipo de 4 personas utilizando Git y GitHub, basado en el desafío ficticio de "BiteForge Studios".

[Image of Galaxy Defenders gameplay]

---

## 🚀 Empezando (Instalación)

Sigue estos pasos para descargar y ejecutar el juego en tu máquina local.

### Prerrequisitos

Necesitarás tener dos cosas instaladas en tu sistema:

1.  **Python 3:** El lenguaje de programación que usamos.
    * Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
    * Durante la instalación en Windows, **asegúrate de marcar la casilla "Add Python to PATH"**.

2.  **Git:** El sistema de control de versiones para clonar el repositorio.
    * Puedes descargarlo desde [git-scm.com](https://git-scm.com/downloads).
3. **Visual Studio Code :** NO necesitas el VS Code para jugar a Gallaxy Defenders

1.  **Clona el repositorio:**
    Abre una terminal o Git Bash y clona el proyecto. (Reemplaza `tu-usuario/tu-repositorio` con la URL real de tu repositorio en GitHub).
    ```bash
    git clone [https://github.com/tu-usuario/galaxy-defenders.git](https://github.com/tu-usuario/galaxy-defenders.git)
    cd galaxy-defenders
    ```

2.  **(Recomendado) Crea un entorno virtual:**
    Esto crea un espacio aislado para las dependencias de tu proyecto, lo cual es una buena práctica.
    ```bash
    # En Windows
    python -m venv venv
    .\venv\Scripts\activate
    
    # En macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```
    (Verás `(venv)` al principio de la línea de tu terminal si funcionó).

3.  **Instala las dependencias:**
    El proyecto depende de la biblioteca `Pygame`.
    ```bash
    pip install pygame
    ```

---

## 🎮 Cómo Jugar (Uso)

Una vez que hayas instalado las dependencias, puedes ejecutar el juego con un simple comando:

```bash
python main.py
