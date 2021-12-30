from flask import Flask, request, jsonify
#import json

alumnos =[]

app= Flask(__name__)

@app.route("/")
def test():
    return "Esto es una prueba de servidor Flask"

@app.route("/student")
def mostrar_alumnos():
    return jsonify({"students":alumnos}),200

@app.route("/student", methods=['POST'])
def post_alumno():
    #POST request
    body = request.get_json() #obtener el contenido del cuerpo de la solicitud
    if 'name' not in body:
        return 'You need to specify the first_name',400
        if 'courses' not in body:
            return 'You need to specify the last_name',400
        alumnos.append({"alumno_id":len(alumnos),"nombre":body["name"],"cursos":body["courses"]})
        return jsonify({"mensaje":"Agregado","alumno":body}),200

    if __name__ == "__main__":
        app.run(debug=True)
