from flask import Flask, request, jsonify
#import json

alumnos =[]

app= Flask(__name__)

@app.route("/")
def test():
    return "Error, no se encuentra el servicio",404

@app.route("/student", methods=['GET'])
def mostrar_alumnos():
    return jsonify({"students":alumnos}),200

@app.route('/student/<int:dato_id>',methods=['GET'])
def get_uno(dato_id):
    try:
        return jsonify(alumnos[dato_id]),200
    except:
        return jsonify({"Mensaje":"Error, no se encuentra ese dato","id":dato_id}),404

@app.route('/student', methods=['POST'])
def post_alumno():
    #POST request
    body = request.get_json() #obtener el contenido del cuerpo de la solicitud
    if "name" not in body:
        return jsonify({"Mensaje":"No hay campo nombre"}),400
    if "courses" not in body:
        return jsonify({"Mensaje":"No hay campo curso"}),400
    alumnos.append({"alumno_id":len(alumnos),"nombre":body["name"],"cursos":body["courses"]})
    return jsonify({"mensaje":"Agregado","alumno":body}),201

@app.route('/student/<int:dato_id>', methods=['PUT'])
def put_alumno(dato_id):
    #PUT request
    dato= request.get_json() #obtener el contenido del cuerpo de la solicitud
    if "name" in dato:
        alumnos[dato_id]["nombre"]=dato["name"]
        return jsonify({"Mensaje":"Modificado","id":dato_id,"dato":dato}),201
    elif "courses" in dato:
        alumnos[dato_id]["Cursos"]= dato["courses"]
        return jsonify({"Mensaje":"Modificado","id":dato_id,"dato":dato}),201
    else:
        return jsonify({"Mensaje":"No existe el campo","dato":dato}),404

@app.route("/student/<int:dato_id>",methods=["DELETE"])
def delete_alumno(dato_id):
    try:
        del alumnos[dato_id]
        return jsonify({"Mensaje":"Borrado","id":dato_id}),204
    except:
        return jsonify({"Mensaje":"Error, no se encontro"}),404


if __name__ == "__main__":
    app.run(debug=True)
