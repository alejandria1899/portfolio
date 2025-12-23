# Portfolio PRL - Técnico en Prevención de Riesgos Laborales

Portfolio web profesional desarrollado con Flask para técnicos en Prevención de Riesgos Laborales.

## 🚀 Características

- Diseño moderno y profesional
- Totalmente responsive (adaptado a móviles, tablets y escritorio)
- Secciones: Inicio, Sobre Mí, Experiencia, Formación, Proyectos, Contacto
- Animaciones suaves y transiciones
- Fácil de personalizar y actualizar

## 📋 Requisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

## 🛠️ Instalación

1. **Clonar o descargar el proyecto**

2. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Ejecución

1. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```

2. **Abrir en el navegador:**
   ```
   http://localhost:5000
   ```

## ✏️ Personalización

### Modificar tus datos

Edita el archivo `app.py` y modifica el diccionario `portfolio_data` con tu información:

- **Información personal**: nombre, título, email, teléfono, ubicación
- **Redes sociales**: LinkedIn, GitHub
- **Sobre mí**: descripción personal
- **Experiencia**: trabajos anteriores y actuales
- **Formación**: estudios y cursos
- **Certificaciones**: certificados profesionales
- **Habilidades**: con niveles de 0 a 100
- **Proyectos**: proyectos destacados

### Cambiar colores

Edita el archivo `static/css/style.css` y modifica las variables CSS en `:root`:

```css
:root {
    --primary-color: #2563eb;    /* Color principal */
    --secondary-color: #1e40af;  /* Color secundario */
    --accent-color: #3b82f6;     /* Color de acento */
    /* ... más colores */
}
```

### Agregar tu foto

Reemplaza el placeholder en `templates/index.html`:

```html
<div class="hero-image">
    <img src="{{ url_for('static', filename='img/foto.jpg') }}" alt="Tu nombre" class="profile-photo">
</div>
```

Y agrega la imagen en `static/img/foto.jpg`

## 📁 Estructura del Proyecto

```
portfolio-prl/
│
├── app.py                 # Aplicación Flask principal
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Este archivo
│
├── templates/            # Plantillas HTML
│   ├── base.html        # Plantilla base
│   ├── index.html       # Página principal
│   └── contacto.html    # Página de contacto
│
└── static/              # Archivos estáticos
    ├── css/
    │   └── style.css    # Estilos CSS
    └── js/
        └── main.js      # JavaScript
```

## 🌐 Despliegue

Para poner tu portfolio en producción, puedes usar servicios como:

- **Heroku**: https://www.heroku.com
- **PythonAnywhere**: https://www.pythonanywhere.com
- **Render**: https://render.com
- **Vercel**: https://vercel.com

## 📝 Licencia

Este proyecto es de código abierto y está disponible para uso personal y comercial.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de hacer fork y mejorar este proyecto.

## 📧 Contacto

Para preguntas o sugerencias, puedes contactar a través del formulario en el portfolio.

---

¡Buena suerte con tu portfolio! 🎉



"# portfolio" 
