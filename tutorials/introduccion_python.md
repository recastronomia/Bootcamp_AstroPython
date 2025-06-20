# Tutorial: Introducción a Python y Git

## 1. Configuración del entorno

### Instalación de Python
Para comenzar, asegúrate de tener Python instalado en tu sistema. Puedes descargar la última versión desde [python.org](https://www.python.org/downloads/).

### Configuración de Git
1. Instala Git desde [git-scm.com](https://git-scm.com/downloads)
2. Configura tu identidad:
   ```bash
   git config --global user.name "Tu Nombre"
   git config --global user.email "tu.email@example.com"
   ```

### Conceptos básicos de Python
```
def saludar(nombre):
    return f"¡Hola, {nombre}!"

# Ejemplo de uso
print(saludar("Estudiante de RECA"))
```

### Ejecutar pruebas
```
pytest
```
###  Comandos básicos de Git

```
# Clonar un repositorio
git clone https://github.com/usuario/repositorio.git

# Crear una rama
git checkout -b nombre-rama

# Revisar cambios
git status

# Agregar cambios
git add .

# Confirmar cambios
git commit -m "Descripción del cambio"

# Enviar cambios al repositorio remoto
git push origin nombre-rama
```

###  Ejercicio práctico

1) Modifica la función `get_phrase()` para que devuelva un mensaje personalizado
2) Ejecuta las pruebas para asegurarte de que todo funciona
3) Crea una nueva rama y sube tus cambios

###  Actualiza la estructura del proyecto en el README para incluir la nueva carpeta:
```
Bootcamp_AstroPython/
├── src
│   ├── __init__.py
│   └── [main.py](http://_vscodecontentref_/1)
├── tests
│   ├── __init__.py
│   └── test_main.py
├── .github
│   └── workflows
│       └── pytest.yml
├── images
│   └── Logo_RECA.png
├── tutorials
│   └── introduccion_python.md
├── requirements.txt
├── pytest.ini
└── README.md

```