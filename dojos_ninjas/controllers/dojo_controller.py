from flask import  render_template, request, redirect, session
from dojos_ninjas.models.dojo_model import Dojo
from dojos_ninjas.controllers.ninjas_controller import Ninja
from dojos_ninjas import app

@app.route('/dojos')
def result_form():
    dojo = Dojo.get_all()
    print(dojo)
    return render_template("dojos.html", dojos=Dojo.get_all())

@app.route('/add', methods=['POST'])
def add_dojo():
    Dojo.create(request.form)
    return redirect('/dojos')

@app.route('/show_dojo/<int:id>')
def show_dojo(id):
    dojo = Dojo.get_one_with_ninjas(id)
    return render_template('show_dojo.html', dojo=dojo)