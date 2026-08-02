

![github-banner](https://github.com/user-attachments/assets/ce50be88-5c05-4060-bf00-f3d1706241c8)

# Code2LLM

**Code2LLM** es una herramienta para preparar bases de código para su análisis por modelos de lenguaje (LLM). Extrae el código de un directorio especificado, lo divide en fragmentos de tamaño manejable y lo formatea para su entrada en LLM. Esta herramienta proporciona tanto una interfaz de línea de comandos (CLI) como una interfaz web para interactuar con el código extraído.

## Tabla de contenidos

- [Características](#features)
- [Instalación](#installation)
- [Uso](#usage)
  - [Interfaz de línea de comandos (CLI)](#command-line-interface-cli)
  - [Interfaz web](#web-interface)
<!-- - [Files and Directories](#files-and-directories) -->
- [Contribuciones](#contributing)
  - [Instrucciones para usuarios](#user-instructions)
  - [Instrucciones para contribuidores](#contributor-instructions)
- [Licencia](#license)
- [Contacto](#contact)

## Características

- **Extracción de código:** Extrae y formatea el código desde un directorio.
- **Fragmentación (Chunking):** Divide el código en fragmentos de un tamaño especificado para ajustarse a las restricciones de entrada de los LLM.
- **Interfaz web:** Visualiza, copia e interactúa con los fragmentos de código extraídos.
- **Soporte CLI:** Inicializa y ejecuta el proceso de extracción desde la línea de comandos.
- **Exclusiones personalizables:** Define patrones para excluir archivos y directorios del procesamiento.

## Instalación

Puedes instalar Code2LLM usando `pipx`:

```bash
pipx install git+https://github.com/adhilroshan/code2llm.git
```

`pipx` es una herramienta para instalar y ejecutar aplicaciones de Python en entornos aislados. Garantiza que Code2LLM y sus dependencias no interfieran con otros proyectos de Python en tu sistema.

## Uso

### Interfaz de línea de comandos (CLI)

1. **Inicializar patrones de exclusión:**

   Inicializa los patrones de exclusión predeterminados y añade patrones adicionales si es necesario:

   ```bash
   code2llm init --additional-excludes '*.tmp' 'test_dir/'
   ```

2. **Iniciar extracción y servidor web:**

   Ejecuta el proceso de extracción e inicia el servidor web de Flask:

   ```bash
   code2llm --directory /path/to/your/code --max-chars 3000 --port 2277
   ```

   - `--directory`: Directorio base para escanear.
   - `--max-chars`: Número máximo de caracteres por fragmento (el valor predeterminado es 3000).
   - `--port`: Número de puerto para la aplicación Flask (el valor predeterminado es 2277).

### Interfaz web

Después de iniciar el servidor web, accede a la interfaz web en:

```
http://localhost:2277
```

Aquí podrás visualizar e interactuar con los fragmentos de código extraídos.

<!-- ## Files and Directories

- **`pyproject.toml`**: Project configuration and dependencies.
- **`app.py`**: Flask application and server logic.
- **`code2llm/`**: Package containing initialization and CLI logic.
- **`lib/`**: Library with utilities for code extraction and chunking.
- **`static/`**: Static files (JavaScript and CSS) for the web interface.
- **`templates/`**: HTML templates for the web interface.
- **`tests/`**: Unit tests for the project. -->

## Contribuciones

Damos la bienvenida a contribuciones para mejorar Code2LLM. Por favor, sigue las siguientes directrices:

### Instrucciones para usuarios

1. **Reportar problemas:** Si encuentras algún error o problema, por favor abre un issue en la página de [GitHub Issues](https://github.com/adhilroshan/code2llm/issues).
2. **Solicitudes de características:** Si tienes sugerencias para nuevas funcionalidades, no dudes en abrir una solicitud.
3. **Comentarios y retroalimentación:** Para comentarios generales o preguntas, puedes contactarnos por correo electrónico o abrir una discusión en la sección de [GitHub Discussions](https://github.com/adhilroshan/code2llm/discussions).

### Instrucciones para contribuidores

1. **Hacer fork del repositorio:** Realiza un fork del repositorio en GitHub y clónalo en tu máquina local.
2. **Crear una rama:** Crea una nueva rama para tus cambios:

   ```bash
   git checkout -b feature-branch
   ```

3. **Realizar cambios:** Implementa tus cambios o correcciones.
4. **Escribir pruebas:** Asegúrate de que tus cambios estén cubiertos por pruebas.
5. **Confirmar cambios (Commit):** Realiza commit de tus cambios con un mensaje descriptivo:

   ```bash
   git add .
   git commit -m "Describe your changes"
   ```

6. **Enviar a GitHub (Push):** Envía tus cambios a tu repositorio bifurcado:

   ```bash
   git push origin feature-branch
   ```

7. **Crear una Pull Request:** Abre una pull request desde tu repositorio bifurcado hacia el repositorio principal, describiendo tus cambios y por qué deberían ser integrados.

8. **Proceso de revisión:** Participa en el proceso de revisión y realiza los ajustes necesarios según los comentarios recibidos.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Para preguntas o comentarios, por favor contacta a [Adhil Roshan](mailto:adhilroshann@gmail.com).

## Blog

Consulta nuestra [entrada de blog](https://blog.adhilroshan.me/introducing-code2llm-seamless-interaction-with-your-codebase-using-gpt-4o-and-claude-35-sonnet) para obtener más información y detalles sobre Code2LLM!
