from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

portfolio_data = {
    "nombre": "Roger Esteve Martín",
    "titulo": "Futuro Técnico de Prevención de Riesgos Laborales",
    "email": "rogeresteve5@hotmail.com",
    "ubicacion": "Barcelona, España",
    "linkedin": "https://www.linkedin.com/in/rogeresteve/",
    "github": "https://github.com/alejandria1899",

    # Texto corto para el HERO
    "resumen": (
    "A raíz de mi experiencia profesional en entornos de almacén y logística, "
    "he ido desarrollando una mayor sensibilización con la seguridad y la prevención "
    "en el trabajo. Esta vivencia me llevó a tomar la decisión de formarme en "
    "Prevención de Riesgos Laborales, con el objetivo de contribuir a entornos de "
    "trabajo más seguros y saludables."
),


    # Sobre mí ahora va al final y es más personal
    "sobre_mi": (
    "Además de mi formación en Prevención de Riesgos Laborales, tengo interés por la "
    "tecnología y la programación, ámbito en el que realizo proyectos personales. "
    "Entre ellos, he desarrollado PRL-Tech, una idea orientada al uso de sensores "
    "para mejorar la seguridad en entornos de trabajo, FP Quiz, una aplicación de "
    "cuestionarios para el estudio, y Card Genius, una app de flashcards para el "
    "aprendizaje progresivo. "
    "Además, soy un amante del deporte, durante años practiqué intensamente running, lo que me llevó a completar una maratón y una media maratón de montaña. "
    "Por otro lado, me motiva seguir probando nuevos retos deportivos y actualmente me interesa especialmente la natación en aguas abiertas."
),


    "intereses_badges": [
        "Deporte y entrenamiento",
        "Aprendizaje continuo",
        "Tecnología y programación",
        "Organización y disciplina"
    ],

    "experiencia": [
        {
            "puesto": "Operaciones de almacén",
            "empresa": "Quadis Recambios",
            "periodo": "2025 - actualidad",
            "descripcion": [
                "Trabajo en equipo y coordinación de tareas",
                "Gestión de materiales y organización del almacén",
                "Cumplimiento de procedimientos y seguridad"
            ]
        },
        {
            "puesto": "Mozo de Almacén",
            "empresa": "Amazon Fulfillment Center - Barcelona y Zaragoza",
            "periodo": "2020 - 2024",
            "descripcion": [
                "Preparación de pedidos y control de stock",
                "Uso de herramientas de registro y control",
                "Orden y limpieza del área de trabajo"
            ]
        },
        {
            "puesto": "Recepcionista",
            "empresa": "Synthon Hispania",
            "periodo": "2019",
            "descripcion": [
                "Apoyo en tareas operativas",
                "Responsabilidad y puntualidad",
                "Trabajo bajo presión en picos de actividad"
            ]
        }
    ],

    "formacion": [
    {
        "titulo": "Máster Gestión de la Prevención de Riesgos Laborales de las tres especialidades",
        "centro": "UOC",
        "periodo": "2026 - 2028"
    },
    {
        "titulo": "Grado Superior en Prevención de Riesgos Profesionales",
        "centro": "Davante - Medac",
        "periodo": "2025 - 2027"
    },
    {
        "titulo": "Grado Universitario (Turismo)",
        "centro": "EU Mediterrani",
        "periodo": "2016 - 2020"
    },
    {
        "titulo": "Bootcamp de Programación (850 horas)",
        "centro": "Factoria F5",
        "periodo": "2024"
    }
],


    "certificaciones": [
        "En proceso: formación complementaria en PRL",
        "Interés en ISO 45001",
        "Formación interna / cursos (añade los tuyos cuando quieras)"
    ],

    "habilidades": [
        {"nombre": "Organización y disciplina", "nivel": 90},
        {"nombre": "Trabajo en equipo", "nivel": 88},
        {"nombre": "Responsabilidad y constancia", "nivel": 92},
        {"nombre": "Comunicación", "nivel": 80},
        {"nombre": "Nociones de programación", "nivel": 65},
        {"nombre": "Aprendizaje continuo", "nivel": 95}
    ],

    "proyectos": [
  {
        "titulo": "Card Genius (Flashcards)",
        "descripcion": "App web de flashcards con anverso/reverso para memorizar vocabulario y conceptos. Organiza mazos por temas, guarda progreso de estudio y usa IA para generar frases de práctica con las palabras aprendidas.",
        "tecnologias": ["React", "TypeScript", "Supabase", "PostgreSQL", "IA"],
        "url": "https://card-genius-weld.vercel.app/",
        "github": "https://github.com/alejandria1899/card_genius",
        "imagen": "img/card-genius.png"
  },
  {
        "titulo": "FP Quiz",
        "descripcion": "Plataforma de cuestionarios del centro formativo para que mis compañeros practiquen por temas, hagan simulacros y descarguen los tests en PDF. Incluye registro de preguntas falladas y explicación con IA cuando fallas una pregunta.",
        "tecnologias": ["Python", "Streamlit", "SQLite", "IA"],
        "url": "https://fpquizapp-ygbx38tv2hg4n3qevoh9qr.streamlit.app/",
        "github": "https://github.com/alejandria1899/fp_quiz_app",
        "imagen": "img/fp-quiz.png"
  },
  {"titulo": "PRL - Tech",
        "descripcion": "Aplicación web para monitorizar temperatura y humedad en tiempo real y generar informes automáticos en PDF. Lectura con sensor DHT22 y microcontrolador ESP32, con registro de datos en la nube. Posbilidad de monitorización de monóxido de carbono u otros gases.",
        "tecnologias": ["Python", "Streamlit", "ThingSpeak", "Arduino"],
        "url": "https://temperaturecontrol.streamlit.app/",
        "github": "https://github.com/alejandria1899/prl_tech",
        "imagen": "img/prl-tech.png"
        
  }
]
}


@app.route("/")
def index():
    current_year = datetime.now().year
    return render_template("index.html", data=portfolio_data, year=current_year)


@app.route("/contacto")
def contacto():
    current_year = datetime.now().year
    return render_template("contacto.html", data=portfolio_data, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
