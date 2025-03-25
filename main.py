from flask import Flask, render_template, request, redirect, url_for
import db
from datetime import  datetime
from models import Tarea
app = Flask(__name__)  # servidor virtual


@app.route("/")
def home():
    '''función para iniciar la web principal'''
    mostrar_tareas=db.session.query(Tarea).all()
    for i in mostrar_tareas:
        print(i)

    return render_template("index.html", lista_tareas=mostrar_tareas)

@app.route("/crear-tarea", methods=["POST"])
def crear():
    '''función que crea la tarea y la guarda en la db tareas a través del botón guardar del html'''
    fecha=datetime.strptime(request.form["fecha_tarea"],"%Y-%m-%d")

    print(fecha)

    tarea=Tarea(contenido=request.form["contenido_tarea"] ,categoria=request.form["categoria_tarea"], fecha_limite=fecha, hecha=False)
    db.session.add(tarea) #agregamos la nueva tarea a la db
    db.session.commit()#guardamos los cambios en la db
    return redirect(url_for("home")) #redirige a la home de la web una vez guardada la tarea
@app.route("/eliminar-tarea/<id>")
def eliminar(id):
    '''función para elimiar tarea.
    al clicar el la web, selecciona la tarea y la elimina de la db y de la visualización'''
    tarea=db.session.query(Tarea).filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect((url_for("home")))
@app.route("/marcar-tarea/<id>")
def marcar(id):
    '''función para marcar como hecha una tarea
    cambia a True en la db la columna hecha'''
    tarea=db.session.query(Tarea).filter_by(id=int(id)).first() #seleccionamos la tarea. Para que nos devuelva un objeto ponemos el .first(
    tarea.hecha=not(tarea.hecha) #con el not, cambiamos el valor booleano
    db.session.commit()
    return redirect((url_for("home")))

@app.route("/modificar-tarea/<id>")
def modificar(id):
    tarea= db.session.query(Tarea).filter_by(id=int(id)).first()
    print(tarea.contenido)

    '''función para modificar una tarea'''
    return render_template("modificar-tarea.html", tarea=tarea)

@app.route("/modificada/<id>", methods=["POST"])
def confirmar(id):
    nueva_fecha = datetime.strptime(request.form["fecha_tarea"], "%Y-%m-%d")
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first()
    tarea.contenido=request.form["contenido_tarea"]
    tarea.categoria=request.form["categoria_tarea"]
    tarea.fecha_limite=nueva_fecha
    db.session.commit()
    print("Tarea modificada.")
    return redirect((url_for("home")))





if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)
