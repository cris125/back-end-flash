from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve






app = Flask(__name__)
cors = CORS(app)


from Controladores.ControladorMesa import ControladorMesa
miControladorMesa=ControladorMesa()

from Controladores.ControladorPartidos import ControladorPartidos
miControladorPartidos=ControladorPartidos()

from Controladores.ControladorCandidatos import ControladorCandidatos
miControladorCandidatos=ControladorCandidatos()

from Controladores.ControladorResultados import ControladorResultados
miControladorResultados=ControladorResultados()





@app.route("/listado_candidatos_mas_votados",methods=['GET'])
def listadoCandidatos():
    json  = miControladorCandidatos.candidatos()
    json2 = miControladorResultados.resultados()
    json3 = miControladorPartidos.partidos()
    return jsonify(json,json2,json3)

@app.route("/listado_mayor_participacion",methods=['GET'])
def listadoCandidatos_mayor():

    json2 = miControladorResultados.resultados_mayor()

    return jsonify(json2)



@app.route("/candidatos/partidos",methods=['GET'])
def listadoCandidatos_mayorsdasd():

    candi = miControladorCandidatos.index()
    part=miControladorPartidos.index()
    hola = []

    for x in candi:
        for b in x:

            for xx in part:

                for bb in xx:
                    if xx[bb] == x[b]:
                        hola.append(xx)
            hola.append({b: x[b]})

    return jsonify(hola)








@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)


################################################################



@app.route("/mesa",methods=['GET'])
def getMesas():
    json=miControladorMesa.index()
    return jsonify(json)
@app.route("/mesa",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)
@app.route("/mesa/<string:id>",methods=['GET'])
def getMesa(id):
    json=miControladorMesa.show(id)
    return jsonify(json)
@app.route("/mesa/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json=miControladorMesa.update(id,data)
    return jsonify(json)

@app.route("/mesa/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)
######################################################################
@app.route("/partidos",methods=['GET'])
def getPartidos():
    json=miControladorPartidos.index()
    return jsonify(json)
@app.route("/partidos",methods=['POST'])
def crearPartidos():
    data = request.get_json()
    json=miControladorPartidos.create(data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorPartidos.show(id)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartidos(id):
    data = request.get_json()
    json=miControladorPartidos.update(id,data)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartidos(id):
    json=miControladorPartidos.delete(id)
    return jsonify(json)
###############################################################


@app.route("/candidatos",methods=['GET'])
def getCandidatos():
    json=miControladorCandidatos.index()
    return jsonify(json)
@app.route("/candidatos",methods=['POST'])
def crearCandidatos():
    data = request.get_json()
    json=miControladorCandidatos.create(data)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
    json=miControladorCandidatos.show(id)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarCandidatos(id):
    data = request.get_json()
    json=miControladorCandidatos.update(id,data)
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidatos(id):
    json=miControladorCandidatos.delete(id)
    return jsonify(json)

############################################################
@app.route("/resultados",methods=['GET'])
def getResultados():
    json=miControladorResultados.index()
    return jsonify(json)
@app.route("/resultados",methods=['POST'])
def crearResultados():
    data = request.get_json()
    json=miControladorResultados.create(data)
    return jsonify(json)
@app.route("/resultados/<string:id>",methods=['GET'])
def getResultado(id):
    json=miControladorResultados.show(id)
    return jsonify(json)
@app.route("/resultados/<string:id>",methods=['PUT'])
def modificarResultados(id):
    data = request.get_json()
    json=miControladorResultados.update(id,data)
    return jsonify(json)

@app.route("/resultados/<string:id>",methods=['DELETE'])
def eliminarResultados(id):
    json=miControladorResultados.delete(id)
    return jsonify(json)






def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data
if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])

