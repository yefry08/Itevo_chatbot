# Itevo_chatbot
Chatbot de Traducción Avanzado
Descripción
Este proyecto implementa un chatbot de traducción en tiempo real utilizando Python, Gradio para la interfaz de usuario, y la API de Google Translate para las traducciones. El chatbot permite a los usuarios seleccionar idiomas de origen y destino, enviar mensajes y recibir traducciones instantáneas.
Características

Interfaz de chat intuitiva
Soporte para múltiples idiomas
Almacenamiento de historial de chat en base de datos SQLite
Manejo de privacidad mediante hash de IDs de usuario
Pruebas unitarias para garantizar la funcionalidad

Requisitos previos

Python 3.7+
pip (gestor de paquetes de Python)

Instalación
Ve a esta URL: https://huggingface.co/spaces/ElDoctor/translate


Estructura del proyecto
Copychatbot-traduccion-avanzado/
│
├── advanced_translation_chatbot.py  # Archivo principal del chatbot
├── chat_history.db                  # Base de datos SQLite (creada al ejecutar)
├── README.md                        # Este archivo
└── requirements.txt                 # Dependencias del proyecto
Arquitectura de la aplicación

Interfaz de usuario: Implementada con Gradio, proporciona una interfaz web interactiva para el chatbot.
Motor de traducción: Utiliza la biblioteca deep_translator para interactuar con la API de Google Translate.
Almacenamiento de datos: Utiliza SQLite para almacenar el historial de chat y la información del usuario.
Manejo de privacidad: Implementa hashing de IDs de usuario para proteger la privacidad.
Sistema de logging: Utiliza el módulo logging de Python para registrar eventos y errores.
Pruebas unitarias: Implementadas con el módulo unittest de Python.

Cómo usar

Ejecutar el chatbot:
Copypython advanced_translation_chatbot.py

Abrir el navegador y acceder a la URL proporcionada (generalmente http://localhost:7860).
En la interfaz:

Seleccionar el idioma de origen y destino.
Introducir un ID de usuario (para fines de demostración).
Escribir un mensaje y presionar Enter para recibir la traducción.



Pruebas
Las pruebas unitarias se ejecutan automáticamente al iniciar el script. Para ejecutarlas manualmente:
Copypython -m unittest advanced_translation_chatbot.py
Consideraciones de seguridad y privacidad

Los IDs de usuario se hash-ean antes de almacenarse.
No se almacenan datos personales identificables.
Se recomienda implementar autenticación de usuarios en un entorno de producción.

Escalabilidad y mejoras futuras

Implementar autenticación de usuarios.
Migrar a una base de datos más robusta para entornos de producción.
Añadir más pruebas y configurar integración continua.
Implementar límites de tasa y manejo de errores más exhaustivo.

Contribuciones
Las contribuciones son bienvenidas. Por favor, abra un issue para discutir cambios mayores antes de enviar un pull request.
Licencias
No aplica

![image](https://github.com/user-attachments/assets/d7cc5132-b136-4e8a-a3c6-fd370cc6e238)

