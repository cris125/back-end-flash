from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Candidatos import Candidatos
from bson import ObjectId

class RepositorioCandidatos(InterfaceRepositorio[Candidatos]):



    def candidatos(self):
        query1 =  {
        '$group': {
            '_id': '$cedula',
            'doc': {
                '$first': '$$ROOT'
            }
        }
    }




        pipeline = [query1]
        return self.queryAggregation(pipeline)


