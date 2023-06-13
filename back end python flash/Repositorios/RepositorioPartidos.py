from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Partidos import Partidos
class RepositorioPartidos(InterfaceRepositorio[Partidos]):

    def partidos(self):
        query1 = {
            '$group': {
                '_id': '$nombre',
                'doc': {
                    '$first': '$$ROOT'
                }
            }
        }

        pipeline = [query1]
        return self.queryAggregation(pipeline)

