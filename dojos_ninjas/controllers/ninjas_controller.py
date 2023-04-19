from flask import  render_template, request, redirect, session

from dojos_ninjas.models.ninjas_model import Ninja
from dojos_ninjas.models.dojo_model import Dojo
from dojos_ninjas.controllers.dojo_controller import Dojo

from dojos_ninjas import app


app.secret_key = "poggers"



@app.route('/new_ninja')
def result_ninja():
    return render_template("new_ninja.html",  dojos=Dojo.get_all())


@app.route('/add_ninja', methods=['POST'])
def add_ninja():
    Ninja.create(request.form)
    return redirect(f'/show_dojo/{request.form["dojo_id"]}')



# @app.route('/edit_ninja/<int:id>')
# def edit_user(id):
#     # print(id)
#     Ninja.get_one(id)
#     return render_template('edit_ninja.html', ninja=Ninja.get_one(id))


# @app.route('/save_ninja', methods=['POST'])
# def save_user():
#     Ninja.save(request.form)
#     return redirect('/')


# @app.route('/delete_ninja/<int:id>')
# def delete(id):
    
#     Ninja.delete(id)
    
#     return redirect('/')












@app.route('/reset_session')
def reset():
    session.clear()
    return redirect('/')
