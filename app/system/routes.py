<<<<<<< HEAD
from flask import render_template
from . import system_bp

@system_bp.get("/")
def index():
    return render_template("base.html", title="Sistema (em construção)")
=======
from flask import render_template
from . import system_bp

@system_bp.get("/")
def index():
    return render_template("base.html", title="Sistema (em construção)")
>>>>>>> 821acfce0df8476ea6d7009ab01ba996be0d033d
