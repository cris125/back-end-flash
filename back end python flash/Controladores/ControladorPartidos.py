from Repositorios.RepositorioPartidos import RepositorioPartidos
from Modelos.Partidos import Partidos
class ControladorPartidos():
    def __init__(self):
        self.repositorioPartidos = RepositorioPartidos()

    def partidos(self):
        return self.repositorioPartidos.partidos()


    def index(self):
        return self.repositorioPartidos.findAll()
    def create(self,infoPartidos):
        nuevoPartidos=Partidos(infoPartidos)
        return self.repositorioPartidos.save(nuevoPartidos)
    def show(self,id):
        elPartidos=Partidos(self.repositorioPartidos.findById(id))
        return elPartidos.__dict__
    def update(self,id,infoPartidos):
        PartidosActuales=Partidos(self.repositorioPartidos.findById(id))
        PartidosActuales.numero_partidos =infoPartidos["numero_partidos"]
        PartidosActuales.nombre = infoPartidos["nombre"]
        PartidosActuales.lema = infoPartidos["lema"]
        return self.repositorioPartidos.save(PartidosActuales)
    def delete(self,id):
        return self.repositorioPartidos.delete(id)