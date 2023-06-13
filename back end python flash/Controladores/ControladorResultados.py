from Repositorios.RepositorioResultados import RepositorioResultados
from Modelos.Resultados import Resultados
class ControladorResultados():
    def __init__(self):
        self.repositorioResultados = RepositorioResultados()


    def resultados(self):
        return self.repositorioResultados.resultados()

    def resultados_mayor(self):
        return self.repositorioResultados.resultados_mayor()



    def index(self):
        return self.repositorioResultados.findAll()
    def create(self,infoResultados):
        nuevoResultados=Resultados(infoResultados)
        return self.repositorioResultados.save(nuevoResultados)
    def show(self,id):
        elResultado=Resultados(self.repositorioResultados.findById(id))
        return elResultado.__dict__
    def update(self,id,infoResultados):
        ResultadosActuales= Resultados(self.repositorioResultados.findById(id))
        ResultadosActuales.numero_mesa =infoResultados["numero_mesa"]
        ResultadosActuales.cedula_candidato = infoResultados["cedula_candidato"]
        ResultadosActuales.numero_votos = infoResultados["numero_votos"]

        return self.repositorioResultados.save(ResultadosActuales)
    def delete(self,id):
        return self.repositorioResultados.delete(id)