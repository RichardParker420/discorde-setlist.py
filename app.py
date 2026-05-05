import os
from flask import Flask, render_template

app = Flask(__name__)

# --- CONFIGURACIÓN DE TU BANDA ---
DATOS_BANDA = {
    "nombre": "TU BANDA AQUÍ",
    "imagen_url": "https://placehold.co/400x200",  # Cambia esto por un link real
    "setlist": [
        {"titulo": "Canción 1", "letra": "Letra de la primera canción...\nVerso 1\nCoro..."},
        {"titulo": "Canción 2", "letra": "Letra de la segunda canción...\nVerso 1\nCoro..."},
        {"titulo": "Canción 3", "letra": "Letra de la tercera canción...\nVerso 1\nCoro..."}
    ]
}

@app.route('/')
def home():
    return render_template('index.html', banda=DATOS_BANDA)

if __name__ == '__main__':
    # FIX: debug=True nunca en producción — se controla con variable de entorno
    debug_mode = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug_mode)
