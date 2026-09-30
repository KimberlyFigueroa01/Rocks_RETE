# Sistema experto de clasificacion de rocas

Esqueleto modular para un sistema basado en conocimiento que utilizara el motor Rete de [Experta](https://pypi.org/project/experta/). Esta version establece las dependencias, los hechos base, el punto de entrada y una prueba de arranque. **Todavia no incluye reglas de clasificacion geologica.**

## Arquitectura

```text
Rocks_RETE/
|-- main.py
|-- requirements.txt
|-- src/
|   |-- __init__.py
|   |-- facts.py
|   |-- engine.py
|   `-- utils.py
`-- tests/
    `-- test_rules.py
```

- `src/facts.py`: declara las subclases base de `Fact`: `Evidencia`, `Origen`, `Clasificacion` y `Recomendacion`. Aun no tienen campos definidos; estos se concretaran al modelar el dominio.
- `src/engine.py`: contiene `RockClassificationEngine`, subclase de `KnowledgeEngine`. Incluye en comentarios la forma orientativa de una regla `@Rule`, sin activar reglas todavia.
- `src/utils.py`: ofrece un punto de extension para mostrar la memoria de trabajo y la agenda. La salida es deliberadamente un marcador hasta que se decida el formato y se incorporen reglas.
- `src/__init__.py`: identifica `src` como paquete Python.
- `main.py`: crea el motor, lo reinicia, declara un hecho vacio de prueba y llama a `run()`.
- `tests/test_rules.py`: prueba inicial con `unittest` que verifica que el motor acepta un hecho y puede ejecutarse.
- `requirements.txt`: fija Experta y restringe `frozendict` a la serie compatible requerida por Experta 1.9.4.

## Python y compatibilidad

Experta 1.9.4 es una version antigua. Sus metadatos en PyPI declaran clasificadores hasta Python 3.8; por tanto, **este proyecto debe ejecutarse con Python 3.8**. `requirements.txt` incluye `frozendict<2.0`; Experta 1.9.4 fija internamente `frozendict==1.2`, asi que la resolucion normal terminara usando esa version.

Python 3.9 a 3.11 puede funcionar en algunos entornos, pero no esta cubierto por los clasificadores publicados de Experta. La dependencia antigua `frozendict==1.2` puede dar problemas en Python 3.10 y posteriores por cambios en `collections` de la biblioteca estandar. Python 3.12+ tampoco debe considerarse compatible de forma directa. Si el proyecto debe usar esas versiones:

1. Preferir Python 3.8 para ejecutar Experta 1.9.4 sin modificar dependencias.
2. Como alternativa, mantener un fork de Experta que permita una version moderna de `frozendict` y verificar sus cambios con las pruebas del proyecto.
3. Un parche local de compatibilidad para `collections` antes de importar Experta puede servir como medida temporal, pero no es una solucion garantizada y debe probarse con el entorno objetivo.

No se debe asumir que cambiar solo la restriccion de `frozendict` en `requirements.txt` actualiza la dependencia: Experta 1.9.4 solicita la version 1.2 de forma exacta.

## Instalacion

Instala Python 3.8 y, desde la carpeta raiz del repositorio, instala Experta. **No es necesario crear ni activar un entorno virtual** para ejecutar este proyecto.

En Windows PowerShell, usa el launcher para asegurar que el paquete se instale en Python 3.8:

```powershell
py -3.8 -m pip install experta
```

Tambien puedes usar el comando corto si `pip` corresponde a Python 3.8:

```powershell
pip install experta
```

Para instalar las dependencias declaradas en el archivo del proyecto:

```powershell
py -3.8 -m pip install -r requirements.txt
```

En macOS o Linux, el equivalente es `python3.8 -m pip install experta`. Un entorno virtual sigue siendo opcional si deseas aislar las dependencias. En VS Code, selecciona el interprete global de Python 3.8 mediante **Python: Select Interpreter**.

## Ejecucion

Desde la raiz del repositorio, ejecuta el programa con Python 3.8:

```powershell
py -3.8 main.py
```

El motor se inicia, acepta un hecho de prueba y ejecuta `run()`. Como aun no hay reglas, no se deriva ninguna clasificacion; se imprimen marcadores para la memoria de trabajo y la agenda.

## Pruebas

`unittest` forma parte de Python, por lo que no requiere instalar pytest. Ejecuta la prueba con Python 3.8:

```powershell
py -3.8 -m unittest discover -s tests -v
```

Las pruebas actuales solo cubren el arranque del motor y la declaracion del hecho de prueba. Las reglas, sus prioridades y los resultados de clasificacion se incorporaran en una etapa posterior.
