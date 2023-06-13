from Repositorios.RepositorioCandidatos import RepositorioCandidatos
from Modelos.Candidatos import Candidatos
class ControladorCandidatos():
    def __init__(self):
        self.repositorioCandidatos = RepositorioCandidatos()

    "Obtener todos los inscritos en una materia"






    def candidatos(self):
        return self.repositorioCandidatos.candidatos()




    def index(self):

        return self.repositorioCandidatos.findAll()

    def create(self,infoCandidatos):
        nuevoCandidato=Candidatos(infoCandidatos)
        return self.repositorioCandidatos.save(nuevoCandidato)

    def show(self,id):
        elCandidato=Candidatos(self.repositorioCandidatos.findById(id))
        return elCandidato.__dict__

    def update(self,id,infoCandidatos):
        CandidatosActuales= Candidatos(self.repositorioCandidatos.findById(id))
        CandidatosActuales.cedula =infoCandidatos["cedula"]
        CandidatosActuales.numero_resolucion = infoCandidatos["numero_resolucion"]
        CandidatosActuales.nombre = infoCandidatos["nombre"]
        CandidatosActuales.apellido = infoCandidatos["apellido"]
        return self.repositorioCandidatos.save(CandidatosActuales)
    def delete(self,id):
        return self.repositorioCandidatos.delete(id)