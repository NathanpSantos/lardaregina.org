import os, sys

ROOT = os.path.dirname(os.path.dirname(__file__))  # volta pra raiz do projeto
sys.path.insert(0, ROOT)

from app import create_app

app = create_app()
