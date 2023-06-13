from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultados import Resultados
class RepositorioResultados(InterfaceRepositorio[Resultados]):


    def resultados(self):
        query1 =  {
        '$group': {
            '_id': '$numero_mesa',
            'Total_votos_mesa': {
                '$sum': {
                    '$sum': [
                        '$votos_candidato2', '$votos_candidato1'
                    ]
                }
            },
            'votos_candidato1': {
                '$sum': {
                    '$sum': [
                        '$votos_candidato1'
                    ]
                }
            },
            'votos_candidato2': {
                '$sum': {
                    '$sum': [
                        '$votos_candidato2'
                    ]
                }
            }
        }
    }
        pipeline = [query1]
        return self.queryAggregation(pipeline)
    def resultados_mayor(self):
            query1 =  {
        '$group': {
            '_id': '$null',
            'votos_optenidos': {
                '$max': '$numero_votos'
            },
            'doc': {
                '$max': '$$ROOT'
            }
        }
    }

            pipeline = [query1]
            return self.queryAggregation(pipeline)

