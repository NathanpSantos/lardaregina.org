from flask import render_template
from . import system_bp

@system_bp.get("/")
def index():
    return render_template("base.html", title="Sistema (em construção)")
